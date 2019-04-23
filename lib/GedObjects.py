from datetime import datetime, timedelta
from itertools import combinations
from typing import List, Dict

import attr

import lib.GedConstants as gc

class DuplicateIndividualException(Exception):
    """A Tree already contains an Individual with the ID of the Individual being added"""


class DuplicateFamilyException(Exception):
    """A Tree already contains an Family with the ID of the Family being added"""


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
        :return: An integer representing this individual's age in years.
        :raises AttributeError: If this individual has no birthday
        """
        if not self.birthday:
            raise AttributeError('Individual has no birthday')
        if self.alive:
            return int((datetime.now() - self.birthday).days / gc.DAYS_IN_YEAR)
        else:
            return int((self.death - self.birthday).days / gc.DAYS_IN_YEAR)

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

    @property
    def first_name(self):
        return self.name.split('/')[0].strip()

    @property
    def last_name(self):
        return self.name.split('/')[1].strip()


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
                self.married if self.married else 'NA',
                self.divorced.strftime(gc.DATE_FORMAT) if self.divorced else 'NA',
                self.husband_id or 'NA',
                tree.get_indi(self.husband_id).name if self.husband_id else 'NA',
                self.wife_id or 'NA',
                tree.get_indi(self.wife_id).name if self.wife_id else 'NA',
                self.children if len(self.children) > 0 else 'NA']


@attr.s
class Tree:
    _families: Dict[str, Family] = attr.ib(init=False, factory=dict)
    _individuals: Dict[str, Individual] = attr.ib(init=False, factory=dict)

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

    def get_indi(self, id: str) -> Individual:
        """
        Get an individual by the specified ID
        :param id: The ID of the individual to retrieve
        :return: The requested Individual
        :raises ValueError: If the individual is not in this Tree
        """
        try:
            return self._individuals[id]
        except KeyError:
            raise ValueError('Individual not found')

    def siblings_by_age(self) -> List:
        siblings = []
        for family in self._families.values():
            for id in family.children:
                cur_individual = self.get_indi(id)
                if cur_individual.birthday is not None and cur_individual.alive:
                    siblings.append(cur_individual)

        siblings.sort(key=lambda s: s.age)
        return [s.indi_to_list() for s in siblings]

    # US25
    def unique_children(self) -> bool:
        success = True
        for family in self._families.values():
            name_and_births = set()
            for child_id in family.children:
                child = self.get_indi(child_id)
                birthday_string = child.birthday.strftime(gc.DATE_FORMAT)
                if (child.first_name, birthday_string) in name_and_births:
                    success = False
                    print(
                        f'WARNING: FAMILY: US25: {family.id}: Children have the same name and birthday (name: {child.first_name}, birthday: {birthday_string}).')
                else:
                    name_and_births.add((child.first_name, birthday_string))
        return success

    # US16
    def male_last_names(self) -> bool:
        """Check that all males in the same family have the same last name."""
        bool_result = True
        for family in self._families.values():
            if family.husband_id is not None:
                husb = self.get_indi(family.husband_id)
                curr_fam = family.id
                for indi_id in self._individuals:  # Iterate over the keys of the dict of individuals
                    if self.get_indi(indi_id).sex == "M" and self.get_indi(indi_id).child == curr_fam:
                        male_indi = self.get_indi(indi_id)
                        if male_indi.last_name != husb.last_name:
                            #                         print(f'ERROR: FAMILY: US16: Individual {family.husband_id} and Individual {indi_id} are males in the same family with different last names.')
                            print(
                                f'ERROR: FAMILY: US16: Individual {indi_id} has a different last name from other males in the same family.')
                            bool_result = False
        return bool_result

    # US21
    def correct_gender_for_role(self) -> bool:
        bool_result = True
        seen_people = set()
        for family in self._families.values():
            if (family.husband_id is not None) and (self.get_indi(family.husband_id).sex not in ["M", "m"]) and (family.husband_id not in seen_people):
                print(
                    f'WARNING: INDIVIDUAL: US21: Individual {family.husband_id} is the incorrect gender for their role. The individual is a husband and should be a male.')
                seen_people.add(family.husband_id)
                bool_result = False
            if (family.wife_id is not None) and (self.get_indi(family.wife_id).sex not in ["F", "f"]) and (family.wife_id not in seen_people):
                print(
                    f'WARNING: INDIVIDUAL: US21: Individual {family.wife_id} is the incorrect gender for their role. The individual is a wife and should be a female.')
                seen_people.add(family.wife_id)
                bool_result = False
        return bool_result

    # US24
    def unique_families_by_spouse(self):
        seen_parents = set()
        for family in self._families.values():
            if None in (family.married, family.husband_id, family.wife_id):
                continue
            husband = self.get_indi(family.husband_id)
            wife = self.get_indi(family.wife_id)
            marriage_str = family.married.strftime(gc.DATE_FORMAT)
            if (husband.name, wife.name, marriage_str) in seen_parents:
                print(f'ERROR: FAMILY: US24: {husband.name} and {wife.name} appear married in two families at the same date ({marriage_str}).')
                return False
            seen_parents.add((husband.name, wife.name, marriage_str))
        return True

    # US33
    def list_orphans(self):
        orphans = list()
        for family in self._families.values():
            if family.husband_id and family.wife_id and not self.get_indi(family.husband_id).alive and not self.get_indi(family.wife_id).alive:
                for child_id in family.children:
                    child = self.get_indi(child_id)
                    if child.age and child.age < 18 and child not in orphans:
                        orphans.append(child)

        return [o.indi_to_list() for o in orphans]

    def all_dates_before_today(self):
        bool_result = True
        current_date = datetime.now()
        for family in self._families.values():
            if family.married is not None and family.married > current_date:
                bool_result = False
                print(f'ERROR: FAMILY: US1: Family {family.id} marriage date is in the future.')
            if family.divorced is not None and family.divorced > current_date:
                print(f'ERROR: FAMILY: US1: Family {family.id} divorce date is in the future.')
                bool_result = False

        for individ in self._individuals.values():
            if individ.birthday is not None and individ.birthday > current_date:
                bool_result = False
                print(f'ERROR: INDIVIDUAL: US1: Individual {individ.id} birthday is in the future.')
            if individ.death is not None and individ.death > current_date:
                bool_result = False
                print(f'ERROR: INDIVIDUAL: US1: Individual {individ.id} death date is in the future.')
        return bool_result

#  US 10
    def marriage_age(self) -> bool:
        """Verify that all people who are married are at least 14 years of age.
        Marriage should be at least 14 years after birth for both spouses (parents must be at least 14 years of age)"""
        of_age_when_married = True

        fourteen_years = gc.DAYS_IN_YEAR * 14

        for family in self._families.values():
            #             print(family.husband_id)
            if family.married and family.husband_id and family.wife_id:
                husband = self.get_indi(family.husband_id)
                wife = self.get_indi(family.wife_id)
                if family.married - husband.birthday < timedelta(days=fourteen_years):
                    of_age_when_married = False
                    print(
                        f'WARNING: INDIVIDUAL: US10: Individual {family.husband_id} in family {family.id} is below the minimum marriage age.')
                if family.married - wife.birthday < timedelta(days=fourteen_years):
                    of_age_when_married = False
                    print(
                        f'WARNING: INDIVIDUAL: US10: Individual {family.wife_id} in family {family.id} is below the minimum marriage age.')
            if len(family.children) > 0 and family.husband_id and family.wife_id:
                father = self.get_indi(family.husband_id)
                mother = self.get_indi(family.wife_id)
                for child in family.children:
                    kid = self.get_indi(child)
                    if kid.birthday - father.birthday < timedelta(days=fourteen_years):
                        of_age_when_married = False
                        print(
                            f'WARNING: INDIVIDUAL: US1: Individual {family.husband_id} in family {family.id} is below the minimum age to have a child.')
                    if kid.birthday - mother.birthday < timedelta(days=fourteen_years):
                        of_age_when_married = False
                        print(
                            f'WARNING: INDIVIDUAL: US1: Individual {family.wife_id} in family {family.id} is below the minimum age to have a child.')
        return of_age_when_married

    # US18
    def siblings_not_married(self) -> bool:
        result = True
        for fam_a, fam_b in combinations(self._families.values(), 2):
            if fam_a.husband_id in fam_b.children and fam_a.wife_id in fam_b.children:
                print(f'WARNING: FAMILY: US18: Family {fam_a.id} parents are siblings in {fam_b.id}.')
                result = False
        return result

    # US31 List all living singles over 30
    def living_single(self) -> list:
        singleList = []
        for individual in self._individuals.values():
            if individual.birthday and individual.age > 30 and individual.spouse is None and individual.alive:
                singleList.append([individual.name, individual.age])
        return singleList

    #US29
    def list_deceased(self) -> list:
        obituary = []
        for individual in self._individuals.values():
            if not individual.alive:
                obituary.append([individual.name, individual.age])
        return obituary

    # US38 list of upcoming birthdays
    def upcoming_birthday(self) -> list:
        birthdayList = []
        for individual in self._individuals.values():
            if individual.alive and individual.birthday is not None:
                birthdate = individual.birthday.replace(year=datetime.now().year)
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if 0 < (birthdate - today).days <= 30:
                    birthdayList.append([individual.name, individual.birthday.strftime(gc.DATE_FORMAT), individual.age])
        return birthdayList

    def dates_within(self, date1, date2, limit, units):
        conversion = {'days': 1, 'months': 30.4, 'years': 365.25}
        return (abs((date1-date2).days) / conversion[units]) <= limit

    # US13 Sibling Spacing
    def check_sibling_spacing(self) -> bool:
        result = True
        for family in self._families.values():
            for indi_a, indi_b in combinations(map(self.get_indi, family.children), 2):
                if self.dates_within(indi_a.birthday, indi_b.birthday, 8, 'months') and not self.dates_within(indi_a.birthday, indi_b.birthday, 2, 'days'):
                    print(f'WARNING: INDIVIDUAL: US13: Individual {indi_a.id} and Individual {indi_b.id} were born too close to one another. ')
                    result = False
        return result

    # US36 List Recent Deaths
    def list_recent_deaths(self) -> List:
        recent_death_list = []
        for individual in self._individuals.values():
            if individual.death is not None:
                if abs(individual.death - datetime.now()) <= timedelta(days=30):
                    recent_death_list.append(individual)
        return [indi.indi_to_list() for indi in recent_death_list]

    #US17
    def parent_not_spouse(self) -> bool:
        not_incest = True
        for family in self._families.values():
            if family.husband_id and family.wife_id:
                husband = self.get_indi(family.husband_id)
                wife = self.get_indi(family.wife_id)
                if family.married is not None and len(family.children) > 0:
                    for child in family.children:
                        # if child == wife or husband:
                        child_indi = self.get_indi(child)
                        if child_indi.id == husband.id or child_indi.id == wife.id:
                            not_incest = not_incest and False
                            if child_indi.id == husband.id:
                                print(f'ERROR: INDIVIDUAL: US17: Individual {husband.id} parent is married to her child.')
                            else:
                                print(f'ERROR: INDIVIDUAL: US17: Individual {wife.id} parent is married to his child.')
        return not_incest

    # US02
    def birth_pre_marriage(self) -> bool:
        born_when_married = True
        for family in self._families.values():
            if family.husband_id and family.wife_id:
                husband = self.get_indi(family.husband_id)
                wife = self.get_indi(family.wife_id)
                if family.married is not None and wife.birthday > family.married:
                    born_when_married = born_when_married and False
                    print(f'ERROR: FAMILY: US02: Individual {wife.id} marriage date is before birth.')
                if family.married is not None and husband.birthday > family.married:
                    born_when_married = born_when_married and False
                    print(f'ERROR: FAMILY: US02: Individual {husband.id} marriage date is before birth.')
        return born_when_married

    # US4- Marriage Before Divorce
    def marr_bef_div(self):
        """Marriage should occur before divorce of spouses, and divorce can only occur after marriage"""
        right_order = True
        for family in self._families.values():
            if family.divorced and (family.married is None):
                right_order = right_order and False
                print(f"WARNING: US04: FAMILY {family.id}: DIVORCE OCCURS WITHOUT MARRIAGE.")
            elif family.divorced is not None and family.divorced < family.married:
                right_order = right_order and False
                print(f"WARNING: US04: FAMILY {family.id}: DIVORCE OCCURS BEFORE MARRIAGE.")
        return right_order

    # US09
    def birth_before_parents_death(self) -> bool:
        """Child should be born before death of mother and before 9 months after death of father"""
        valid_bday = True
        for family in self._families.values():
            if family.children is not None and family.husband_id and family.wife_id:
                for child in family.children:
                    mom = self.get_indi(family.wife_id)
                    dad = self.get_indi(family.husband_id)
                    kid = self.get_indi(child)
                    if kid.birthday is not None and mom.death is not None:
                        # if (kid.birthday - mom.death).days > 1:
                        if kid.birthday > mom.death:
                            valid_bday = valid_bday and False
                            print(f"WARNING: US 09 : INDIVIDUAL {kid.id} HAS AN INVALID BIRTHDAY BECAUSE THEY WERE BORN AFTER THEIR MOTHER'S DEATH")
                    if kid.birthday is not None and dad.death is not None:
                        if (kid.birthday - dad.death).days > 273:
                            valid_bday = valid_bday and False
                            print(f"WARNING: US 09: INDIVIDUAL {kid.id} HAS AN INVALID BIRTHDAY BECAUSE THEY WERE BORN MORE THAN 9 MONTHS AFTER THEIR FATHER'S DEATH")
        return valid_bday

    #US 32
    def multiple_births(self):
        """List all multiple births in a GEDCOM file"""
        multi_birth_list = []
        for family in self._families.values():
            i = 0
            while i < len(family.children)-1 and len(family.children) >= 2:
                kid1 = self.get_indi(family.children[i])
                kid2 = self.get_indi(family.children[i+1])
                if kid1.birthday == kid2.birthday:
                    multi_birth_list.append([kid1.name, kid1.birthday.strftime('%d-%m-%Y'), kid1.age])
                    multi_birth_list.append([kid2.name, kid2.birthday.strftime('%d-%m-%Y'), kid2.age])
                i += 1
        return multi_birth_list

    # US 05
    def marriage_before_death(self):
        valid = True
        for family in self._families.values():
            if family.married:
                if family.husband_id:
                    husband = self.get_indi(family.husband_id)
                    if husband.death and husband.death < family.married:
                        print(f'ERROR: FAMILY: US05: Family {family.id}: Husband death occurs before marriage date')
                        valid = False
                if family.wife_id:
                    wife = self.get_indi(family.wife_id)
                    if wife.death and wife.death < family.married:
                        print(f'ERROR: FAMILY: US05: Family {family.id}: Wife death occurs before marriage date')
                        valid = False
        return valid

    #US 06
    def div_bef_deat(self):
        """Divorce can only occur before the death of both spouses"""
        possible = True
        for family in self._families.values():
            if family.divorced is not None:
                spouse1 = self.get_indi(family.husband_id)
                spouse2 = self.get_indi(family.wife_id)
                if spouse1.death is not None and spouse1.death < family.divorced:
                    print(f'WARNING: INDIVIDUAL: US6: Individual {spouse1.id} died before divorce. ')
                    possible = possible and False
                if spouse2.death is not None and spouse2.death < family.divorced:
                    print(f'WARNING: INDIVIDUAL: US6: Individual {spouse2.id} died before divorce. ')
                    possible = possible and False
        return possible

    #US 34
    def list_large_age_difference(self):
        """List all couples who were married when the older spouse was more than twice as old as the younger spouse"""
        big_age_diff = []
        for family in self._families.values():
            if family.husband_id and family.wife_id:
                spouse1 = self.get_indi(family.husband_id)
                spouse2 = self.get_indi(family.wife_id)
                if family.married is not None and spouse1.birthday is not None and spouse2.birthday is not None:
                    s1_marriage_age = family.married - spouse1.birthday
                    s2_marriage_age = family.married - spouse2.birthday
                    if s1_marriage_age >= 2*s2_marriage_age or s2_marriage_age >= 2*s1_marriage_age:
                        big_age_diff.append([spouse1.name, spouse1.birthday.strftime('%d-%m-%Y'), family.married.strftime('%d-%m-%Y'), spouse1.age])
                        big_age_diff.append([spouse2.name, spouse2.birthday.strftime('%d-%m-%Y'), family.married.strftime('%d-%m-%Y'), spouse2.age])
        return big_age_diff

    #US 30
    def list_living_married(self):
        """List all living married people in a GEDCOM file"""
        living_and_married = []
        for individual in self._individuals.values():
            if individual.spouse is not None and individual.alive:
                living_and_married.append([individual.name, individual.age])
        return living_and_married

    #US12
    def par_not_old(self) -> bool:
        parents_not_old = True
        for family in self._families.values():
            if family.husband_id and family.wife_id:
                father = self.get_indi(family.husband_id)
                mother = self.get_indi(family.wife_id)
                for child in family.children:
                    child = self.get_indi(child)
                    if mother.age >= 60 + child.age:
                        parents_not_old = False
                        print(f"WARNING: INDIVIDUAL: US12: mother in {family.id} too old")
                    elif father.age >= 80 + child.age:
                        print(f"WARNING: INDIVIDUAL: US12: father in {family.id} too old")
                        parents_not_old = False
        return parents_not_old

    #US15
    def fewer_than_fifteen_siblings(self) -> bool:
        okay_num_of_siblings = True
        for family in self._families.values():
            sibling_count = 0
            if family.children is not None:
                for child in family.children:
                    sibling_count += 1
                if sibling_count >= 15:
                    okay_num_of_siblings = False and okay_num_of_siblings
                    print(f"WARNING: FAMILY: US 15: Family {family.id} has 15 or more children.")
        return okay_num_of_siblings

    #US23
    def unique_name_birthday_pairs(self) -> bool:
        all_unique_name_birth_pairs = True
        duplicate_groups = []
        for current_indi in self._individuals.values():
            duplicates = []
            for other_indi in self._individuals.values():
                if other_indi.id != current_indi.id and other_indi.name == current_indi.name and other_indi.birthday == current_indi.birthday:
                    all_unique_name_birth_pairs = False and all_unique_name_birth_pairs
                    duplicates.append(other_indi)
            if duplicates:
                total_list = [current_indi.id] + [curr.id for curr in duplicates]
                havent_printed_yet = True
                for group in duplicate_groups:
                    if all(elem in total_list for elem in group):
                        havent_printed_yet = False
                        break
                if havent_printed_yet:
                    print(f"WARNING: INDIVIDUAL: US 23: INDIVIDUALS {[current_indi.id] + [current.id for current in duplicates]} have the same name and birthday.")
                    duplicate_groups.append(total_list)
        return all_unique_name_birth_pairs

    #US03
    def birth_before_death(self) -> bool:
        valid = True
        for current_indi in self._individuals.values():
            if current_indi.birthday is not None and current_indi.death is not None:
                if current_indi.death < current_indi.birthday:
                    valid = False
                    print(f"WARNING: US 03: INDIVIDUAL {current_indi.id} died before they were born.")
        return valid

    #US35
    def list_recent_births(self) ->List:
        recent_birth_list = []
        for individual in self._individuals.values():
            if individual.birthday is not None:
                if abs(individual.birthday - datetime.now()) <= timedelta(days=30):
                    recent_birth_list.append(individual)
        return [indi.indi_to_list() for indi in recent_birth_list]

    #US08
    def birth_occurs_at_valid_date(self) -> bool:
        valid_birthday = True
        for family in self._families.values():
            for id in family.children:
                curr_child = self.get_indi(id)
                if family.divorced is not None:
                    if curr_child.birthday - family.divorced > timedelta(9 * gc.DAYS_IN_MONTH):
                        valid_birthday = False
                        print(f"WARNING: US 08: INDIVIDUAL {curr_child.id} was born more than 9 months after parents' divorce.")
                if family.married is not None:
                    if curr_child.birthday < family.married:
                        valid_birthday = False
                        print(f"WARNING: US 08: INDIVIDUAL {curr_child.id} was born before parents' marriage.")
        return valid_birthday

    def individuals(self) -> List:
        """Return a list of all of current Individuals in list form, sorted by ID"""
        individuals_by_id = sorted(self._individuals.values(), key=lambda i: i.id)
        return [i.indi_to_list() for i in individuals_by_id]

    def families(self) -> List:
        """Return a list of all current Families in list form, sorted by ID"""
        families_by_id = sorted([f for f in self._families.values()], key=lambda f: f.id)
        return [f.fam_to_list(self) for f in families_by_id]

    def validate(self) -> bool:
        return all(
            [
                self.correct_gender_for_role(),
                self.male_last_names(),
                self.unique_children(),
                self.marriage_age(),
                self.all_dates_before_today(),
                self.check_sibling_spacing(),
                self.unique_families_by_spouse(),
                self.list_recent_deaths(),
                self.parent_not_spouse(),
                self.birth_pre_marriage(),
                self.marr_bef_div(),
                self.birth_before_parents_death(),
                self.fewer_than_fifteen_siblings(),
                self.unique_name_birthday_pairs(),
                self.birth_before_death(),
                self.siblings_not_married(),
                self.par_not_old(),
                self.div_bef_deat(),
                self.birth_occurs_at_valid_date(),
                self.marriage_before_death(),
            ]
        )
