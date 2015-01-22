#AU classes
import tkinter
import au_region

#game app class

#Pronoun Constants
MALE = 'Male'
FEMALE = 'Female'
NEUTRAL = 'Neutral'


class InsufficientManaError(Exception):
    '''
    Raised whenever a player attempts to select an option that
    results in mana dropping below 0.
    '''
    pass


#character class
class Character:
    def __init__(self, name, color, gender):
        self._name = name
        self._gender = gender #Need functions to get appropriate pronouns
                              #Male/Female/Gender Neutral
        self._color = color
        self._hp = 6
        self._mp = 5
        self._str = 1
        self._cha = 1

        self._events = 0
        self._tier = 1 #aka cynicalness attribute

        #needs to be balanced
        self._TIER_ONE_END = 10 
        self._TIER_TWO_END = 15 
        self._TIER_THREE_END = 20 


        ##Tiers:
        #Tier One: "Yay life nothing is wrong"
        #Tier Two: "Wow, suspicious things are happening. Huh."
        #Tier Three: "Something is defs wrong, yo. My life is a sham."
        #Tier Four: "I want OUT. I want YOUR life. Grrrrrrrr."
        
        self._region = au_region.Region

        self._items = []

#Attributes Up/Down

    def str_up(self):
        self._str += 1

    def str_down(self):
        self._str -= 1

    def hp_up(self, amount = 1):
        self._hp += amount

    def hp_down(self, amount = 1):
        self._hp -= amount

    def cha_up(self):
        self._cha += 1

    def cha_down(self):
        self._cha -= 1

    def mp_up(self):
        self._mp += 1

    def mp_down(self, amount = 1):
        if self._mp - amount >= 0:
            self._mp -= amount
        else:
            raise InsufficientManaError()

    def add_item(self, item : str):
        self._items.append(item)

    def remove_item(self, item : str) -> bool:
        '''Remove given item; return true if they have the item,
    return false otherwise.'''
        if item in self._items:
            self._items.remove(item)
            return True

        else:
            return False

    def events_up(self):
        self._events += 1

        if self._events == self._TIER_ONE_END:
            self._tier += 1

        elif self._events == self._TIER_TWO_END:
            self._tier += 1

        elif self._events == self._TIER_THREE_END:
            self._tier += 1

    def set_region(self, new_region : "Region"):
        self._region = new_region

#Get Functions
        
    def get_str(self):
        return self._str

    def get_hp(self):
        return self._hp

    def is_dead(self) -> bool:
        if self._hp <= 0:
            return True
        else:
            return False
        
    def get_cha(self):
        return self._cha

    def get_mp(self):
        return self._mp

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_gender(self):
        return self._gender

    def get_items(self):
        return self._items

    def get_stats(self):
        return self._hp, self._mp, self._str, self._cha

    def get_tier(self):
        return self._tier

    def get_events(self):
        return self._events

    def get_region(self):
        return self._region

#The following functions return the appropriate pronoun for the
#alternate player's gender. If at the beginning of the sentence,
#it can be used unaltered. Otherwise, call lower() on the returned str

    def personal(self):
        if self._gender == MALE:
            return "He"
        elif self._gender == FEMALE:
            return "She"
        elif self._gender == NEUTRAL:
            return "They"
        
    def personal_obj(self):
        if self._gender == MALE:
            return "Him"
        elif self._gender == FEMALE:
            return "Her"
        elif self._gender == NEUTRAL:
            return "Them"
        
    def possessive(self):
        if self._gender == MALE:
            return "His"
        elif self._gender == FEMALE:
            return "Her"
        elif self._gender == NEUTRAL:
            return "Their"
        
    def reflexive(self):
        if self._gender == MALE:
            return "Himself"
        elif self._gender == FEMALE:
            return "Herself"
        elif self._gender == NEUTRAL:
            return "Theirself"

