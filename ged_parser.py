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
        if not isinstance(row, list):
            table.add_row([row])
        else:
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
        field_names=["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    )

    siblings_by_age = create_prettytable(
        tree.siblings_by_age(),
        field_names=['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    )
    
    singles_over_30 = create_prettytable(
        tree.living_single(),
        field_names=['Name', 'Age']
    )

    upcoming_birthdays = create_prettytable(
        tree.upcoming_birthday(),
        field_names=['Name', 'Birthday', 'Age']
    )

    recent_deaths = create_prettytable(
        tree.list_recent_deaths(),
        field_names=['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    )

    orphans = create_prettytable(
        tree.list_orphans(),
        field_names=['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    )

    deceased = create_prettytable(
        tree.list_deceased(),
        field_names=['Name', 'Age']
    )

    multi_births = create_prettytable(
        tree.multiple_births(),
        field_names=["Name", "Birthday", "Age"]
    )

    recent_births = create_prettytable(
        tree.list_recent_births(),
        field_names=['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    )

    large_age_difference = create_prettytable(
        tree.list_large_age_difference(),
        field_names=["Name", "Birthday", "Marriage Date", "Age"]
    )

    living_married = create_prettytable(
        tree.list_living_married(),
        field_names=['Name', 'Age']
    )

    print('Individuals')
    print(indi_table)
    print()
    print('Families')
    print(fam_table)
    print()
    print('Siblings By Age')
    print(siblings_by_age)
    print()
    print('Living Singles Over 30')
    print(singles_over_30)
    print()
    print('Upcoming Birthdays')
    print(upcoming_birthdays)
    print()
    print('Recent Deaths')
    print(recent_deaths)
    print()
    print('Orphans')
    print(orphans)
    print()
    print('Deceased')
    print(deceased)
    print('Multiple Births')
    print(multi_births)
    print()
    print('Recent Births')
    print(recent_births)
    print()
    print('Large Age Difference')
    print(large_age_difference)
    print()
    print('Living and Married')
    print(living_married)
    print()

    tree.validate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The GEDCOM file to parse')
    parser.add_argument('--log', default='CRITICAL', help='Logging level')
    main(parser.parse_args())
