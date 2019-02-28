import os

from lib.GedBuilder import Builder

GED_DIR = os.path.join('ged_files')

kristen_tree = Builder().build_tree(os.path.join(GED_DIR, 'kristen_test.ged'))
michael_tree = Builder().build_tree(os.path.join(GED_DIR, 'michael_test.ged'))
michael_dup_names = Builder().build_tree(os.path.join(GED_DIR, 'michael_dup_names.ged'))

sprint_one_tree = Builder().build_tree(os.path.join(GED_DIR, 'SprintOneDemo.ged'))

sprint_two_tree = Builder().build_tree(os.path.join(GED_DIR, 'SprintTwoDemo.ged'))
