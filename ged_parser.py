"""
Michael Manis
I pledge my honor that I have abided by the Stevens Honor system
"""
import argparse
from datetime import datetime, timedelta
from typing import Tuple, List

import attr


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


class ChildException(Exception):
    """There was an error adding a child to a Tree"""
    pass


class SpouseException(Exception):
    """There was an error adding a spouse to a Tree"""
    pass


@attr.s
class Individual:
    """
    :param id: The individual's ID
    :param name: The individual's name
    :param gender: The individual's gender
    :param birthday: The individual's birthday
    :param death: Optional; the individual's date of death
    :param child: Optional; the family ID that this individual is a child of
    :param spouse: Optional; the family ID that this individual is a spouse of
    """
    id: str = attr.ib()
    name: str = attr.ib()
    gender: str = attr.ib()
    birthday: datetime = attr.ib()

    death: datetime = attr.ib(default=None)
    child: str = attr.ib(default=None)
    spouse: str = attr.ib(default=None)

    @property
    def alive(self) -> bool:
        return False if self.death else True

    @property
    def age(self) -> timedelta:
        if self.alive:
            return datetime.now() - self.birthday
        else:
            return self.death - self.birthday


@attr.s
class Family:
    """
    :param id: The ID of this family
    :param married: The date that this family was married
    :param husband_id: The ID of the husband of this family
    :param wife_id: The ID of the wife of this family
    :param children: A list of IDs of children in this family
    :param divorced: Optional; the date that the parents of this family divorced
    """
    id: str = attr.ib()
    married: datetime = attr.ib()
    husband_id: str = attr.ib()
    wife_id: str = attr.ib()
    children: List[str] = attr.ib
    divorced: datetime = attr.ib(default=None)


@attr.s
class Tree:
    _families = attr.ib(init=False, default=dict)
    _individuals = attr.ib(init=False, default=dict)

    def add_individual(self, individual: Individual):
        """Add an individual to the current tree"""
        if self._individuals[individual.id]:
            raise DuplicateIndividualException(f'Individual ID{individual.id} already exists')
        self._families[individual.id] = individual

    def add_family(self, family: Family):
        """Add a family to the current tree"""
        if self._families[family.id]:
            raise DuplicateFamilyException(f'Family ID{family.id} already exists')

    def valid_tree(self) -> bool:
        """Check that all Family object properties line up with all Individual object properties"""
        # TODO
        # Must check that the spouse and child records for each individual line up with all family records
        raise NotImplemented

    def __str__(self):
        """Print individuals and families in a nice table"""
        # TODO
        raise NotImplemented

    def _individuals_str(self) -> List[str]:
        """Return a list of all individuals in string form"""
        return [i.__str__() for i in self._individuals]

    def _families_str(self) -> List[str]:
        """Return a list of all families in string form"""
        return [f.__str__() for f in self._families]


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

        # Level must be between 0 and 3 inclusive
        if level not in ('0', '1', '2', '3'):
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


def main(args):
    filename = args.file
    # Define flags
    indi_creation, fam_creation = False, False
    
    with open(filename) as gedcom_file:
        for n, line in enumerate(gedcom_file):
            line = line.strip('\n')

            # TODO replace printing with logic for building an Individual or Family
            print(f'--> {line}')
            level, tag, args, valid = parse(line)
            print(f'<-- {level}|{tag}|{"Y" if valid else "N"}|{args if args else ""}')

            if tag == 'INDI' and not indi_creation:
                # This is the normal case, but how do we handle case of trying to create an indi while we are already in the process of making one???
                indi_creation = True
                current_indi = Individual()
                # Not sure if this is what we're looking to do
                # Or should I be leveraging the attr module?
                current_indi.id = args
            # Already checked line validity. Now should just 
            elif tag == 'NAME' and indi_creation:
                current_indi.name = args
            elif tag == 'SEX' and indi_creation:
                current_indi.gender = args
            elif (tag == 'BIRT' or tag == 'DEAT') and indi_creation:
                # Maybe we should store a this as a "prev_tag" to check when we're looking at the DATE tag
                prev_tag = tag
                continue
            elif tag == 'DATE' and indi_creation:
                if prev_tag == 'BIRT':
                    current_indi.birthday = args
                else:
                    # Entering else means prev_tag was 'DEAT'
                    current_indi.death = args
                    # Should set alive to True by default and then handle death here
                    current_indi.alive = False
                # Need to handle age somewhere, but not sure how we're using the age property without finishing instantiation
            elif tag == 'FAMC' and indi_creation:
                current_indi.child = args
            elif tag == 'FAMS' and indi_creation:
                current_indi.spouse = args
            elif tag == 'FAM' and not fam_creation:
                # This is the normal case, but how do we handle case of trying to create a fam while we are already in the process of making one???
                fam_creation = True
                curr_fam = Family()
                curr_fam.id = args
            elif (tag == 'MARR' or tag == 'DIV') and fam_creation:
                prev_tag = tag
                continue
            elif tag == 'DATE' and fam_creation:
                if prev_tag == 'MARR':
                    curr_fam.married = args
                else:
                    # Entering else means prev_tag was 'DIV'
                    curr_fam.divorced = args
            elif tag == 'HUSB' and fam_creation:
                curr_fam.husband_id = args
            elif tag == 'WIFE' and fam_creation:
                curr_fam.wife_id = args
            elif tag == 'CHIL' and fam_creation:
                # add the string representing a single child to the children list
                curr_fam.children.append(args)
            elif tag == 'HEAD':
                continue
            elif tag == 'TRLR':
                continue
            elif tag == 'NOTE':
                continue
            
            # NEED TO FIGURE OUT WHERE TO RESET indi_creation and fam_creation TAGS!
                     
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The GEDCOM file to parse')
    main(parser.parse_args())
