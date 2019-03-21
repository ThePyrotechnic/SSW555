import os

from lib.GedBuilder import Builder

GED_DIR = os.path.join('lib', 'test', 'ged_files')

kristen_tree = Builder().build_tree(os.path.join(GED_DIR, 'kristen_test.ged'))
michael_tree = Builder().build_tree(os.path.join(GED_DIR, 'michael_test.ged'))
michael_dup_names = Builder().build_tree(os.path.join(GED_DIR, 'michael_dup_names.ged'))

sprint_one_tree = Builder().build_tree(os.path.join(GED_DIR, 'SprintOneDemo.ged'))

sprint_two_tree = Builder().build_tree(os.path.join(GED_DIR, 'SprintTwoDemo.ged'))

us13_mult_sets_close_sibs = Builder().build_tree(os.path.join(GED_DIR, 'US13MultSetsCloseSibs.ged'))
us13_mult_sets_close_sibs2 = Builder().build_tree(os.path.join(GED_DIR, 'US13MultSetsCloseSibs2.ged'))

us36_some_recent_deaths = Builder().build_tree(os.path.join(GED_DIR, 'US36SomeRecentDeaths.ged'))
us36_all_recent_deaths = Builder().build_tree(os.path.join(GED_DIR, 'US36AllRecentDeaths.ged'))
