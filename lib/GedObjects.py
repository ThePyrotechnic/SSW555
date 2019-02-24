from datetime import datetime
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
                self.married.strftime('%d-%m-%Y') if self.married else 'NA',
                self.divorced.strftime('%d-%m-%Y') if self.divorced else 'NA',
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

    def valid_tree(self) -> bool:
        """Check that all Family object properties line up with all Individual object properties"""
        # TODO
        # Must check that the spouse and child records for each individual line up with all family records
        raise NotImplemented

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
                if (child.name, birthday_string) in name_and_births:
                    success = False
                    print(f'WARNING: FAMILY: {family.id}: Children ')
                else:
                    name_and_births.add((child.name, birthday_string))
        return success
    
    # US16
    def male_last_names(self) -> bool:
        """Check that all males in the same family have the same last name."""
        bool_result = True
        for family in self._families.values():
            husb_name = self.get_indi(family.husband_id).name
            husb_first, husb_last = husb_name.split()
            curr_fam = family.id
            for indi_id in self._individuals:  # Iterate over the keys of the dict of individuals
                if self.get_indi(indi_id).sex =="M" and self.get_indi(indi_id).child == curr_fam:
                    male_indi_name = self.get_indi(indi_id).name
                    first, last = self.get_indi(indi_id).name.split()
                    if (last != husb_last):
#                         print(f'ERROR: FAMILY: US16: Individual {family.husband_id} and Individual {indi_id} are males in the same family with different last names.')
                        print(f'ERROR: FAMILY: US16: Individual {indi_id} has a different last name from other males in the same family.')
                        bool_result = False
        return bool_result
    
    #US21
    def correct_gender_for_role(self) -> bool:
        bool_result = True
        for family in self._families.values():
            if self.get_indi(family.husband_id).sex not in ["M", "m"]:
                print(f'WARNING: INDIVIDUAL: US21: Individual {family.husband_id} is the incorrect gender for their role. The individual is a husband and should be a male.')
                bool_result = False
            if self.get_indi(family.wife_id).sex not in ["F", "f"]:
                print(f'WARNING: INDIVIDUAL: US21: Individual {family.wife_id} is the incorrect gender for their role. The individual is a wife and should be a female.')
                bool_result = False
        return bool_result
    
    def dates_check(self):
        bool_result = True
        current_date = datetime.now()
        for family in self._families.values():
            if family.married > current_date:
                bool_result = False
            if family.divorced != None:
#                 bool_result = True
                if family.divorced > current_date:
                    bool_result = False
        return bool_result

                    
        for individ in self._individuals.values():
            if individ.birthday > current_date:
                bool_result = False
            if individ.death != None:
#                 bool_result = True
                if individ.death > current_date:
                    bool_result = False
        return bool_result

    def individuals(self) -> List:
        """Return a list of all of current Individuals in list form, sorted by ID"""
        individuals_by_id = sorted(self._individuals.values(), key=lambda i: i.id)
        return [i.indi_to_list() for i in individuals_by_id]

    def families(self) -> List:
        """Return a list of all current Families in list form, sorted by ID"""
        families_by_id = sorted([f for f in self._families.values()], key=lambda f: f.id)
        return [f.fam_to_list(self) for f in families_by_id]
    