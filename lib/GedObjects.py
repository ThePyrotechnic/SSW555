from datetime import datetime, timedelta
from typing import List, Dict

import attr


class DuplicateIndividualException(Exception):
    """A Tree already contains an Individual with the ID of the Individual being added"""


class DuplicateFamilyException(Exception):
    """A Tree already contains an Family with the ID of the Family being added"""


class IndividualNotFoundException(Exception):
    """No individual with the given ID exists in the current Tree"""


class IndividualException(Exception):
    """There was an error when parsing this individual in the current context"""


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
        :return: A timedelta representing the difference between now and the individual's birth date if they are alive,
        or their death date and birth date if they are dead.
        :raises IndividualException: If this individual has no birthday
        """
        if not self.birthday:
            raise IndividualException('Individual has no birthday')
        if self.alive:
            return int((datetime.now() - self.birthday).days / 365.25)
        else:
            return int((self.death - self.birthday).days / 365.25)

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
                self.divorced.strftime('%d-%m-%Y') if self.divorced else 'NA',
                self.husband_id or 'NA',
                tree.get_indi(self.husband_id).name if self.husband_id else 'NA',
                self.wife_id or 'NA',
                tree.get_indi(self.wife_id).name if self.wife_id else 'NA',
                self.children if len(self.children) > 0 else 'NA']


@attr.s
class Tree:
    _DAYS_IN_MONTH = 30
    _DATE_FORMAT = '%d-%m-%Y'

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
        :raises IndividualNotFoundException: If the individual is not in this Tree
        """
        try:
            return self._individuals[id]
        except KeyError:
            raise IndividualNotFoundException

    def siblings_by_age(self) -> List:
        siblings = []
        for family in self._families.values():
            for id in family.children:
                cur_individual = self.get_indi(id)
                if cur_individual.birthday is not None and cur_individual.alive:
                    siblings.append(cur_individual)

        siblings.sort(key=lambda s: s.age)
        return [s.indi_to_list() for s in siblings]

    def unique_name_and_birth(self) -> bool:
        success = True
        for family in self._families.values():
            name_and_births = set()
            for child_id in family.children:
                child = self.get_indi(child_id)
                birthday_string = child.birthday.strftime('%Y-%m-%d')
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
                        if (male_indi.last_name != husb.last_name):
                            #                         print(f'ERROR: FAMILY: US16: Individual {family.husband_id} and Individual {indi_id} are males in the same family with different last names.')
                            print(
                                f'ERROR: FAMILY: US16: Individual {indi_id} has a different last name from other males in the same family.')
                            bool_result = False
        return bool_result

    # US21
    def correct_gender_for_role(self) -> bool:
        bool_result = True
        seen_husbands = set()
        seen_wives = set()
        for family in self._families.values():
            if family.husband_id is not None and self.get_indi(family.husband_id).sex not in ["M", "m"]:
                if (family.husband_id not in seen_husbands):
                    print(
                        f'WARNING: INDIVIDUAL: US21: Individual {family.husband_id} is the incorrect gender for their role. The individual is a husband and should be a male.')
                    seen_husbands.add(family.husband_id)
                bool_result = False
            if family.wife_id is not None and self.get_indi(family.wife_id).sex not in ["F", "f"]:
                if (family.wife_id not in seen_wives):
                    print(
                        f'WARNING: INDIVIDUAL: US21: Individual {family.wife_id} is the incorrect gender for their role. The individual is a wife and should be a female.')
                    seen_wives.add(family.wife_id)
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
            marriage_str = family.married.strftime(self._DATE_FORMAT)
            if (husband.name, wife.name, marriage_str) in seen_parents:
                print(f'ERROR: FAMILY: US24: {husband.name} and {wife.name} appear married in two families at the same date ({marriage_str}).')
                return False
            seen_parents.add((husband.name, wife.name, marriage_str))
        return True

    def dates_check(self):
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

    def marriage_age(self) -> bool:

        """Verify that all people who are married are at least 14 years of age.

        Marriage should be at least 14 years after birth for both spouses (parents must be at least 14 years of age)"""

        of_age_when_married = True

        for family in self._families.values():
            #             print(family.husband_id)
            if family.married is not None:
                husband = self.get_indi(family.husband_id)
                wife = self.get_indi(family.wife_id)
                if family.married - husband.birthday < timedelta(days=5110):
                    of_age_when_married = False
                    print(
                        f'WARNING: INDIVIDUAL: US10: Individual {family.husband_id} in family {family.id} is below the minimum marriage age.')
                if family.married - wife.birthday < timedelta(days=5110):
                    of_age_when_married = False
                    print(
                        f'WARNING: INDIVIDUAL: US10: Individual {family.wife_id} in family {family.id} is below the minimum marriage age.')
            if len(family.children) > 0:
                father = self.get_indi(family.husband_id)
                mother = self.get_indi(family.wife_id)
                for child in family.children:
                    kid = self.get_indi(child)
                    if kid.birthday - father.birthday < timedelta(days=5110):
                        of_age_when_married = False
                        print(
                            f'WARNING: INDIVIDUAL: US1: Individual {family.husband_id} in family {family.id} is below the minimum age to have a child.')
                    if kid.birthday - mother.birthday < timedelta(days=5110):
                        of_age_when_married = False
                        print(
                            f'WARNING: INDIVIDUAL: US1: Individual {family.wife_id} in family {family.id} is below the minimum age to have a child.')
        return of_age_when_married

    # US02
    def birth_pre_marriage(self) -> bool:
        born_when_married = True
        for family in self._families.values():
            husband = self.get_indi(family.husband_id)
            wife = self.get_indi(family.wife_id)
            if family.married is not None and wife.birthday < family.married:
                born_when_married = False
                print(f'ERROR: FAMILY: US1: Family {wife.id} marriage date is before birth.')
            if family.married is not None and husband.birthday < family.married:
                born_when_married = False
                print(f'ERROR: FAMILY: US1: Family {husband.id} marriage date is before birth.')
        return born_when_married
    
    #US17
    def parent_not_spouse(self) -> bool:
        not_incest = True
        for family in self._families.values():
            husband = self.get_indi(family.husband_id)
            wife = self.get_indi(family.wife_id)
            if family.married is not None and len(family.children) > 0:
                for child in family.children:
                    if child.id == wife.id or husband.id:
                        not_incest = False
                        print(f'ERROR: INDIVIDUAL: US17: Individual {family.id} parent is married to child.')
        return not_incest

    # US31 List all living singles over 30
    def living_single(self) -> list:
        singleList = []
        for individual in self._individuals.values():
            if individual.birthday and individual.age > 30 and individual.spouse is None and individual.alive:
                singleList.append(individual.name)
        return singleList

    # US38 list of upcoming birthdays
    def upcoming_birthday(self) -> list:
        birthdayList = []
        for individual in self._individuals.values():
            if individual.alive and individual.birthday is not None:
                birthdate = individual.birthday.replace(year=datetime.now().year)
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if 0 < (birthdate - today).days <= 30:
                    birthdayList.append([individual.name, individual.birthday.strftime('%d-%m-%Y')])
        return birthdayList

    # US13 Sibling Spacing
    def check_sibling_spacing(self) -> bool:
        for family in self._families.values():
            for curr_id in family.children:
                curr_individual = self.get_indi(curr_id)
                for other_id in family.children:
                    other_individual = self.get_indi(other_id)
                    if timedelta(days=2) <= abs(curr_individual.birthday - other_individual.birthday) <= timedelta(
                            days=self._DAYS_IN_MONTH * 8):
                        print(f'WARNING: INDIVIDUAL: US13: Individual {curr_id} and Individual {other_id} were born too close to one another. ')
                        return False
        return True

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
                self.unique_name_and_birth(),
                self.marriage_age(),
                self.dates_check(),
                self.check_sibling_spacing(),
                self.unique_families_by_spouse(),
                self.birth_pre_marriage(),
            ]
        )
