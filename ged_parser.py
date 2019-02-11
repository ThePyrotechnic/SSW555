"""
Michael Manis, Kristen Tan, Nneka Udeagbala, Angelica Torres
I pledge my honor that I have abided by the Stevens Honor system
"""
import argparse
from datetime import datetime
import logging
import traceback
from typing import Tuple, List

import attr
from prettytable import PrettyTable


class InvalidLineException(Exception):
    """A line in the GEDCOM file is invalid"""
    pass


class InvalidEntryException(Exception):
    """A Family or Individual record in the GEDCOM file is incomplete"""
    pass


class DuplicateIndividualException(Exception):
    """A Tree already contains an Individual with the ID of the Individual being added"""
    pass


class DuplicateFamilyException(Exception):
    """A Tree already contains an Family with the ID of the Family being added"""
    pass


class IndividualException(Exception):
    """There was an error when parsing this individual in the current context"""
    pass


class IndividualNotFoundException(Exception):
    """No individual with the given ID exists in the current Tree"""
    pass


class ChildException(Exception):
    """There was an error adding a child to a Tree"""
    pass


class SpouseException(Exception):
    """There was an error adding a spouse to a Tree"""
    pass


# noinspection PyUnresolvedReferences
@attr.s
class Individual:
    """
    :param id: The individual's ID
    :param name: Optional; The individual's name
    :param sex: Optional; The individual's sex
    :param birthday: Optional; The individual's birthday
    :param death: Optional; the individual's date of death
    :param child: Optional; the family ID that this individual is a child of
    :param spouse: Optional; the family ID that this individual is a spouse of
    """
    id: str = attr.ib()
    name: str = attr.ib(default=None)
    sex: str = attr.ib(default=None)
    birthday: datetime = attr.ib(default=None)

    death: datetime = attr.ib(default=None)
    child: str = attr.ib(default=None)
    spouse: str = attr.ib(default=None)

    @property
    def alive(self) -> bool:
        """:return: True if the individual is alive, False otherwise"""
        return False if self.death else True

    @property
    def age(self) -> int:
        """
        :return: A timedelta representing the difference between now and the individual's birth date if they are alive,
        or their death date and birth date if they are dead.
        :raises IndividualException: If this individual has no birthday
        """
        if not self.birthday:
            raise IndividualException('Individual has no birthday')
        if self.alive:
            return int((datetime.now() - self.birthday).days / 365.25)
        else:
            return int((self.death - self.birthday).days / 365.25)

    def indi_to_list(self) -> list:
        return [self.id,
                self.name or 'NA',
                self.sex or 'NA',
                self.birthday.strftime("%Y-%m-%d") if self.birthday else 'NA',
                self.age if self.birthday else 'NA',
                self.alive,
                self.death.strftime("%Y-%m-%d") if self.death else 'NA',
                self.child or 'NA',
                self.spouse or 'NA']


# noinspection PyUnresolvedReferences
@attr.s
class Family:
    """
    :param id: The ID of this family
    :param married: Optional; The date that this family was married
    :param husband_id: Optional; The ID of the husband of this family
    :param wife_id: Optional; The ID of the wife of this family
    :param children: Optional; A list of IDs of children in this family
    :param divorced: Optional; the date that the parents of this family divorced
    """
    id: str = attr.ib()
    husband_id: str = attr.ib(default=None)
    wife_id: str = attr.ib(default=None)
    children: List[str] = attr.ib(factory=list)
    married: datetime = attr.ib(default=None)
    divorced: datetime = attr.ib(default=None)

    def fam_to_list(self, tree) -> list:
        return [self.id,
                self.married.strftime('%d-%m-%Y') if self.married else 'NA',
                self.divorced.strftime('%d-%m-%Y') if self.divorced else 'NA',
                self.husband_id or 'NA',
                tree.get_indi(self.husband_id).name if self.husband_id else 'NA',
                self.wife_id or 'NA',
                tree.get_indi(self.wife_id).name if self.wife_id else 'NA',
                self.children if len(self.children) > 0 else 'NA']


@attr.s
class Tree:
    _families = attr.ib(init=False, factory=dict)
    _individuals = attr.ib(init=False, factory=dict)

    def add_individual(self, individual: Individual):
        """Add an individual to the current tree"""
        if self._individuals.get(individual.id):
            raise DuplicateIndividualException(f'Individual ID{individual.id} already exists')
        self._individuals[individual.id] = individual

    def add_family(self, family: Family):
        """Add a family to the current tree"""
        if self._families.get(family.id):
            raise DuplicateFamilyException(f'Family ID{family.id} already exists')
        self._families[family.id] = family

    def valid_tree(self) -> bool:
        """Check that all Family object properties line up with all Individual object properties"""
        # TODO
        # Must check that the spouse and child records for each individual line up with all family records
        raise NotImplemented

    def get_indi(self, id: str) -> Individual:
        """
        Get an individual by the specified ID
        :param id: The ID of the individual to retrieve
        :return: The requested Individual
        :raises IndividualNotFoundException: If the individual is not in this Tree
        """
        try:
            return self._individuals[id]
        except KeyError:
            raise IndividualNotFoundException

    def create_indi_table(self):
        """Create a PrettyTable of all of the current Individuals, sorted by ID"""
        indi_table = PrettyTable()
        indi_table.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age',
                                  'Alive', 'Death', 'Child', 'Spouse']

        for indi_id in self._individuals:
            indi_table.add_row(self._individuals[indi_id].indi_to_list())

        indi_table.sortby = 'ID'
        return indi_table

    def create_family_table(self):
        """Create a PrettyTable of all of the current Families, sorted by ID"""
        fam_table = PrettyTable()
        fam_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

        for fam_id in self._families:
            fam_table.add_row(self._families[fam_id].fam_to_list(self))

        fam_table.sortby = 'ID'
        return fam_table


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


def main(args):
    log_level = getattr(logging, args.log.upper())
    if isinstance(log_level, int):
        logging.basicConfig(level=log_level)

    filename = args.file

    tree = Tree()
    builder = Builder()
    with open(filename) as gedcom_file:
        for _, line in enumerate(gedcom_file):
            line = line.strip('\n')

            level, tag, args, valid = parse(line)
            if valid:
                builder.evaluate(tree, level, tag, args)

    print('Individuals')
    print(tree.create_indi_table())
    print()
    print('Families')
    print(tree.create_family_table())
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The GEDCOM file to parse')
    parser.add_argument('--log', default='CRITICAL', help='Logging level')
    main(parser.parse_args())
