"""
Michael Manis, Kristen Tan, Nneka Udeagbala, Angelica Torres
I pledge my honor that I have abided by the Stevens Honor system
"""
import argparse
import logging

from lib.GedBuilder import Builder, parse
from lib.GedObjects import Tree


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The GEDCOM file to parse')
    parser.add_argument('--log', default='CRITICAL', help='Logging level')
    main(parser.parse_args())
