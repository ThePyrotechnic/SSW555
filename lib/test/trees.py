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

us04_marr_is_before_div = Builder().build_tree(os.path.join(GED_DIR, 'US04MarrIsBeforeDiv.ged'))
us04_marr_not_before_div = Builder().build_tree(os.path.join(GED_DIR, 'US04MarrNotBeforeDiv.ged'))
us04_div_without_marriage = Builder().build_tree(os.path.join(GED_DIR, 'US04DivWithoutMarriage.ged'))

us09_birt_bef_deaths = Builder().build_tree(os.path.join(GED_DIR, 'US09AllRightFam.ged'))
us09_birt_after_deaths = Builder().build_tree(os.path.join(GED_DIR, 'US09WrongFam.ged'))

us15_more_than_fifteen_siblings = Builder().build_tree(os.path.join(GED_DIR, 'US15MoreThanFifteenSiblings.ged'))
us15_exactly_fifteen_siblings = Builder().build_tree(os.path.join(GED_DIR, 'US15ExactlyFifteenSiblings.ged'))
us15_many_more_than_fifteen_siblings = Builder().build_tree(os.path.join(GED_DIR, 'US15ManyMoreThanFifteenSiblings.ged'))

us23_two_individuals_with_same_name_and_birth_date = Builder().build_tree(os.path.join(GED_DIR, 'US23TwoIndividualsWithSameNameAndBirthDate.ged'))
us23_four_individuals_with_same_name_and_birth_date = Builder().build_tree(os.path.join(GED_DIR, 'US23FourIndividualsWithSameNameAndBirthDate.ged'))

us18_siblings_married = Builder().build_tree(os.path.join(GED_DIR, 'US18SiblingsMarried.ged'))
us18_siblings_not_married = Builder().build_tree(os.path.join(GED_DIR, 'US18SiblingsNotMarried.ged'))

us03_death_before_birth = Builder().build_tree(os.path.join(GED_DIR, 'US03DeathBeforeBirth.ged'))

us06_div_bef_death = Builder().build_tree(os.path.join(GED_DIR, 'help.ged'))
