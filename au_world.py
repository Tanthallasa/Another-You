#world class

import au_classes
import au_region
import au_event
from random import randrange

class World:
    def __init__(self, char : au_classes.Character, name = None, color = None, gender = None):
        if char == None:
            char == au_clases.Character(name,color,gender) 

        
        self._char = char
        #Initialize Regions
        self._region_city = au_region.Region_City(self._char)
        self._region_dungeon = au_region.Region_Dungeon(self._char)
        self._region_forest_fairy = au_region.Region_Forest_Fairy(self._char)
        self._region_forest_dark = au_region.Region_Forest_Dark(self._char)
        self._region_desert = au_region.Region_Desert(self._char)
        self._region_plains_lonely = au_region.Region_Plains_Lonely(self._char)
        self._region_plains_illusion = au_region.Region_Plains_Illusion(self._char)
        self._region_arctic = au_region.Region_Arctic(self._char)
        self._region_mountain = au_region.Region_Mountain(self._char)


        self._char.set_region(self._region_city)
        #Connect the Regions
        self._region_city.set_North(self._region_forest_fairy)
        self._region_city.set_South(self._region_plains_illusion)
        self._region_city.set_West(self._region_forest_dark)
        self._region_city.set_East(self._region_plains_lonely)

        self._region_dungeon.set_North(self._region_arctic)
        self._region_dungeon.set_South(self._region_forest_dark)
        self._region_dungeon.set_West(self._region_desert)
        self._region_dungeon.set_East(self._region_forest_fairy)

        self._region_forest_fairy.set_North(self._region_plains_illusion)
        self._region_forest_fairy.set_South(self._region_city)
        self._region_forest_fairy.set_West(self._region_dungeon)
        self._region_forest_fairy.set_East(self._region_desert)
        
        self._region_forest_dark.set_North(self._region_dungeon)
        self._region_forest_dark.set_South(self._region_arctic)
        self._region_forest_dark.set_West(self._region_plains_lonely)
        self._region_forest_dark.set_East(self._region_city)

        self._region_desert.set_North(self._region_arctic)
        self._region_desert.set_South(self._region_plains_lonely)
        self._region_desert.set_West(self._region_forest_fairy)
        self._region_desert.set_East(self._region_dungeon)
        
        self._region_plains_lonely.set_North(self._region_desert)
        self._region_plains_lonely.set_South(self._region_mountain)
        self._region_plains_lonely.set_West(self._region_city)
        self._region_plains_lonely.set_East(self._region_forest_dark)

        self._region_plains_illusion.set_North(self._region_city)
        self._region_plains_illusion.set_South(self._region_forest_fairy)
        self._region_plains_illusion.set_West(self._region_arctic)
        self._region_plains_illusion.set_East(self._region_mountain)

        self._region_arctic.set_North(self._region_forest_dark)
        self._region_arctic.set_South(self._region_dungeon)
        self._region_arctic.set_West(self._region_mountain)
        self._region_arctic.set_East(self._region_plains_illusion)

        self._region_mountain.set_North(self._region_plains_lonely)
        self._region_mountain.set_South(self._region_desert)
        self._region_mountain.set_West(self._region_plains_illusion)
        self._region_mountain.set_East(self._region_arctic)

        #Other Important Attributes

        self._journey = []  #A Journey is a list of cardinal directions (e.g. "'N','S','S','E','N')
                            #that is populated on game start up, calculated from the user's
                            #hourly coordinates accumulated since the last time the game was played
        

    def next_event(self) -> au_event.Event:
        '''Called by GUI. Advances the journey and returns the appropriate
        event.'''
        if self._journey != []:
            current_region = self._char.get_region()
            next_region = au_region.move_direction(current_region,self._journey[0])
            self._journey = self._journey[1:]
            self._char.set_region(next_region)
            return next_region.get_random_event()
            
        else:
            return None

    def begin_journey(self, new_coords : ["Coordinates"]) -> None:
        '''Takes a list of coordinates and calculates the appropriate
        cardinal directions for them. FOR NOW ASSUMES THAT EACH JOURNEY
        STARTS IN THE CITY.'''
##        previous_coord = (0,0)
##        new_journey = []
##        for coord in new_coords:
##            pass

        for cardinal in range(6):
            self._journey.append(get_random_cardinal())
        #Need information from data collection

    def return_default_region(self) -> "Region":
        return self._region_city

def get_random_cardinal() -> str:
    '''Generates a random direction, N, S, E, or W'''
    rand_int = randrange(4)
    if rand_int == 0:
        return au_region.NORTH
    elif rand_int == 1:
        return au_region.SOUTH
    elif rand_int == 2:
        return au_region.WEST
    elif rand_int == 3:
        return au_region.EAST
