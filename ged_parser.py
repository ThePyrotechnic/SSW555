"""
Michael Manis
I pledge my honor that I have abided by the Stevens Honor system
"""
import argparse
from typing import Tuple


class InvalidLineException(Exception):
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
    with open(filename) as gedcom_file:
        for n, line in enumerate(gedcom_file):
            line = line.strip('\n')

            print(f'--> {line}')
            level, tag, args, valid = parse(line)
            print(f'<-- {level}|{tag}|{"Y" if valid else "N"}|{args if args else ""}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The GEDCOM file to parse')
    main(parser.parse_args())
