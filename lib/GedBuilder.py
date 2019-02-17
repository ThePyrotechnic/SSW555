from datetime import datetime
import logging
import traceback
from typing import Tuple

from lib.GedObjects import Tree, Family, Individual, DuplicateIndividualException, DuplicateFamilyException


class InvalidLineException(Exception):
    """A line in the GEDCOM file is invalid"""


class InvalidEntryException(Exception):
    """A Family or Individual record in the GEDCOM file is incomplete"""


class ChildException(Exception):
    """There was an error adding a child to a Tree"""


class SpouseException(Exception):
    """There was an error adding a spouse to a Tree"""


class Builder:
    """Contains stateful logic for building a Tree"""

    FAMILY_TAGS = ['DIV', 'CHIL', 'WIFE', 'HUSB', 'MARR']
    INDIVIDUAL_TAGS = ['FAMS', 'FAMC', 'DEAT', 'BIRT', 'SEX', 'NAME']
    TOP_LEVEL_TAGS = ['INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE']

    def __init__(self):
        self._creating_indi: bool = False
        self._creating_fam: bool = False
        self._creating_birth: bool = False
        self._creating_death: bool = False
        self._creating_marr: bool = False
        self._creating_div: bool = False

        self._current_indi_data: dict = {}
        self._current_fam_data = {'children': []}

    def evaluate(self, tree: Tree, level: int, tag: str, args: str):
        """
        Evaluate a valid line and add information to the tree if necessary
        :param tree: The Tree currently being built
        :param level: (unused) The level of the line to evaluate
        :param tag: The tag of the line to evaluate
        :param args: The args of the line to evaluate
        :return: None
        """
        # If we are creating an individual and the next tag is invalid for an individual
        if self._creating_indi and (tag in Builder.FAMILY_TAGS or tag in Builder.TOP_LEVEL_TAGS):
            self._creating_indi = False
            # Try to add the individual
            try:
                tree.add_individual(Individual(**self._current_indi_data))
            except (TypeError, DuplicateIndividualException):
                logging.log(logging.DEBUG, traceback.format_exc())

            self._current_indi_data = {}

        # If we are creating a family and the next tag is invalid for a family
        elif self._creating_fam and (tag in Builder.INDIVIDUAL_TAGS or tag in Builder.TOP_LEVEL_TAGS):
            self._creating_fam = False
            # Try to add the family
            try:
                tree.add_family(Family(**self._current_fam_data))
            except (TypeError, DuplicateFamilyException):
                logging.log(logging.DEBUG, traceback.format_exc())

            self._current_fam_data = {'children': []}

        # If we are creating some kind of date and the next tag is not 'DATE' or is invalid
        elif True in (self._creating_birth, self._creating_death, self._creating_marr, self._creating_div) and (tag != 'DATE'):
            self._creating_birth, self._creating_death, self._creating_marr, self._creating_div = False, False, False, False

        # Basic cases for each tag
        if tag == 'INDI':
            self._creating_indi = True
            self._current_indi_data['id'] = args
        elif tag == 'FAM':
            self._creating_fam = True
            self._current_fam_data['id'] = args
        elif tag == 'NAME' and self._creating_indi:
            self._current_indi_data['name'] = args
        elif tag == 'SEX' and self._creating_indi:
            self._current_indi_data['sex'] = args
        elif tag == 'BIRT' and self._creating_indi:
            self._creating_birth = True
        elif tag == 'DEAT' and self._creating_indi:
            self._creating_death = True
        elif tag == 'MARR' and self._creating_fam:
            self._creating_marr = True
        elif tag == 'DIV' and self._creating_fam:
            self._creating_div = True
        elif tag == 'DATE':
            timestamp = datetime.strptime(args, '%d %b %Y')
            if self._creating_birth:
                self._current_indi_data['birthday'] = timestamp
            elif self._creating_death:
                self._current_indi_data['death'] = timestamp
            elif self._creating_marr:
                self._current_fam_data['married'] = timestamp
            elif self._creating_div:
                self._current_fam_data['divorced'] = timestamp
        elif tag == 'FAMC' and self._creating_indi:
            self._current_indi_data['child'] = args
        elif tag == 'FAMS' and self._creating_indi:
            self._current_indi_data['spouse'] = args
        elif tag == 'HUSB' and self._creating_fam:
            self._current_fam_data['husband_id'] = args
        elif tag == 'WIFE' and self._creating_fam:
            self._current_fam_data['wife_id'] = args
        elif tag == 'CHIL' and self._creating_fam:
            self._current_fam_data['children'].append(args)
        elif tag == 'HEAD':
            pass
        elif tag == 'TRLR':
            pass
        elif tag == 'NOTE':
            pass


def parse(line: str) -> Tuple[int, str, str, bool]:
    """
    Check that a string follows the GEDCOM spec
    :param line: The line to check
    :return: A tuple of the following format: (ID, tag, args, valid).
    If any values are missing then any of them may equal None and valid will equal False.
    """
    level, tag, args = None, None, None
    try:
        # Try to split the line into three parts, then try two parts
        try:
            level, tag, args = line.split(' ', maxsplit=2)
        except ValueError:
            try:
                level, tag = line.split(' ', maxsplit=1)
            except ValueError:
                raise InvalidLineException(f'Invalid line: {line}')

        # INDI nor FAM should not be the tag
        if tag in ('INDI', 'FAM'):
            raise InvalidLineException(f'Invalid tag {line}')

        # If INDI or FAM are args, swap the args and tag
        if args in ('INDI', 'FAM'):
            temp = args
            args = tag
            tag = temp

        # Level must be between 0 and 2 inclusive
        if level not in ('0', '1', '2'):
            raise InvalidLineException(f'Invalid level: {level}')
        level = int(level)

        # Allow a trailing space
        if args == '':
            args = None

        if tag == 'INDI':
            assert level == 0
            assert args is not None
        elif tag == 'NAME':
            assert level == 1
            assert args is not None
        elif tag == 'SEX':
            assert level == 1
            assert args in ('M', 'F')
        elif tag == 'BIRT':
            assert level == 1
            assert args is None
        elif tag == 'DEAT':
            assert level == 1
            assert args is None
        elif tag == 'FAMC':
            assert level == 1
            assert args is not None
        elif tag == 'FAMS':
            assert level == 1
            assert args is not None
        elif tag == 'FAM':
            assert level == 0
            assert args is not None
        elif tag == 'MARR':
            assert level == 1
            assert args is None
        elif tag == 'HUSB':
            assert level == 1
            assert args is not None
        elif tag == 'WIFE':
            assert level == 1
            assert args is not None
        elif tag == 'CHIL':
            assert level == 1
            assert args is not None
        elif tag == 'DIV':
            assert level == 1
            assert args is None
        elif tag == 'DATE':
            assert level == 2
            assert args is not None
            # Date must have valid args
            try:
                day, month, year = args.split(' ', maxsplit=2)
            except ValueError:
                raise InvalidLineException(f'Not enough values for DATE: {args}')
            assert day == '0' or not day[0] == '0' and day.isdigit()
            assert month in ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
            assert len(year) == 4 and year.isdigit()
        elif tag == 'HEAD':
            assert level == 0
            assert args is None
        elif tag == 'TRLR':
            assert level == 0
            assert args is None
        elif tag == 'NOTE':
            assert level == 0
        else:
            raise InvalidLineException(f'Unknown Tag: {tag}')
    except (AssertionError, InvalidLineException):
        return level, tag, args, False

    return level, tag, args, True
