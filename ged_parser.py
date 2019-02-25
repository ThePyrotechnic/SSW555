"""
Michael Manis, Kristen Tan, Nneka Udeagbala, Angelica Torres
I pledge my honor that I have abided by the Stevens Honor system
"""
import argparse
import logging
from typing import List

from prettytable import PrettyTable

from lib.GedBuilder import Builder


def create_prettytable(l: List, field_names: List[str]):
    table = PrettyTable()
    table.field_names = field_names
    for row in l:
        table.add_row(row)
    return table


def main(args):
    log_level = getattr(logging, args.log.upper())
    if isinstance(log_level, int):
        logging.basicConfig(level=log_level)

    filename = args.file

    tree = Builder().build_tree(filename)

    indi_table = create_prettytable(
        tree.individuals(),
        field_names=['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    )

    fam_table = create_prettytable(
        tree.families(),
        ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    )

    print('Individuals')
    print(indi_table)
    print()
    print('Families')
    print(fam_table)


    tree.validate()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The GEDCOM file to parse')
    parser.add_argument('--log', default='CRITICAL', help='Logging level')
    main(parser.parse_args())
