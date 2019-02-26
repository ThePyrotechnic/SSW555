import os

from lib.GedBuilder import Builder

kristen_tree = Builder().build_tree(os.path.join('ged_files', 'kristen_test.ged'))
michael_tree = Builder().build_tree(os.path.join('ged_files', 'michael_test.ged'))
michael_dup_names = Builder().build_tree(os.path.join('ged_files', 'michael_dup_names.ged'))
