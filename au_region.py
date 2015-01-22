#region class
import au_event
import au_classes
from random import randrange

NORTH = 'n'
SOUTH = 's'
WEST = 'w'
EAST = 'e'
class InvalidRegionDirectionError(Exception):
    '''If move_direction() is ever given a direction
    that isn't NSWE, this error is raised.'''
    pass

class Region:
    def __init__(self, char : "Character", intro : str, coord : (int,int),events : ["Event"]):
        self._intro = intro #Future versions of AU may have multiple intros,
                         #some for different tiers (reflecting either the alt.
                         #player's new perspective, or an actual change in
                         #the region), and some to differentiate the alt. player's
                         #first time in the region and return trips.
                         #Transitional intros (e.g. Forest to Dungeon intro would
                         #be "You emerge from the woods to a large clearing" or
                         #something instead of something generic.
                         #Oh, also, introductions to reflect time.
        
        self._coord = coord #Row, Column
        self._events = events

        #Must be set by the World class using the set_<Direction> functions.
        self._n_region = None
        self._s_region = None
        self._w_region = None
        self._e_region = None

    def get_into(self) -> str:
        return self._intro

    def get_coord(self) -> (int,int):
        return self._coord

    def get_events(self) -> ["Event"]:
        return self._events

    def get_random_event(self) -> "Event":
        num_of_events = len(self._events)
        random_index = randrange(num_of_events)
        return self._events[random_index]

    def get_North(self) -> "Region":
        return self._n_region
    def get_South(self) -> "Region":
        return self._s_region
    def get_West(self) -> "Region":
        return self._w_region
    def get_East(self) -> "Region":
        return self._e_region

    def set_North(self, region : "Region"):
        self._n_region = region

    def set_South(self, region : "Region"):
        self._s_region = region        
        
    def set_West(self, region : "Region"):
        self._w_region = region

    def set_East(self, region : "Region"):
        self._e_region = region

class Region_City(Region):
    def __init__(self, char : "Character"):
        intro = "{0} enters the city known as City. \
                 Civilization is a beautiful sight!".format(char.get_name)
        coord = 1,1

        events = [au_event.Ev_City_Tier1_HappyInn(char)]

        super(Region_City, self).__init__(char,intro,coord,events)

class Region_Dungeon(Region):
    def __init__(self, char : "Character"):
        intro = "{0} finds {1} in a large clearing dominated \
                by the presence of an gigantic, menacing castle \
                with no visible entrance.".format(char.get_name, "HIMSELF/HERSELF") #MAKE PRONOUN MATCH
        coord = 0,0

        events = [au_event.Ev_Dungeon_Tier1_EntranceSearch(char),
                  au_event.Ev_Dungeon_Tier1_MysteriousPuzzle(char)]

        super(Region_Dungeon,self).__init__(char,intro,coord,events)

class Region_Forest_Fairy(Region):
    def __init__(self, char : "Character"):
        intro = "{0} enters a large forest. Splendorous light \
                light radiates everywhere. {0} could swear that \
                {1} could see some of the light... move?".format(char.get_name, "HE/SHE") #MAKE PRONOUN MATCH
        coord = 0,1

        events = [au_event.Ev_Forest_Fairy_TierOne_TrappedFairy(char),
                  au_event.Ev_Forest_Fairy_TierOne_FairyRing(char),
                  au_event.Ev_Forest_TierOne_TreeFallsDown(char),
                  au_event.Ev_Forest_TierOne_WildBoar(char)]

        super(Region_Forest_Fairy,self).__init__(char,intro,coord,events)

class Region_Forest_Dark(Region):
    def __init__(self, char : "Character"):
        intro = "{0} enters a large forest. Sinister darkness \
                blankets every deformed tree. Unnatural sounds echo \
                in the distance.".format(char.get_name)
        coord = 1,0

        events = [au_event.Ev_Forest_TierOne_TreeFallsDown(char),
                  au_event.Ev_Forest_TierOne_WildBoar(char),
                  au_event.Ev_Forest_Dark_TierOne_SpiderAttack(char),
                  au_event.Ev_Forest_Dark_Tier1_Darkness(char)]

        super(Region_Forest_Dark,self).__init__(char,intro,coord,events)

class Region_Desert(Region):
    def __init__(self, char : "Character"):
        intro = "{0} steps foot onto a blazingly hot sea of sand. \
                the oppressive sun is relentless, and the sand seems \
                unstable... ".format(char.get_name)
        coord = 0,2

        events = [au_event.Ev_Desert_Tier1_ShiftingSands(char)]

        super(Region_Desert,self).__init__(char,intro,coord,events)

class Region_Plains_Lonely(Region):
    def __init__(self, char : "Character"):
        intro = "A virtually empty expanse of plains stretches out in\
        front of {0}. There are maybe a handful of lonely trees, \
        and silence reigns. {0} journeys on, the only visible creature \
        for miles.".format(char.get_name)
        coord = 1,2

        events = [au_event.Ev_Plains_Lonely_Tier1_IntrospectionOne(char)]

        super(Region_Plains_Lonely,self).__init__(char,intro,coord,events)
        
class Region_Plains_Illusion(Region):
    def __init__(self, char : "Character"):
        intro = "A virtually empty expanse of plains stretches out in\
        front of {0}. There are maybe a handful of lonely trees, \
        and silence reigns. {0} journeys on, the only visible creature \
        for miles.".format(char.get_name) #The same as Plains (Lonely) to trick
                                          #player's senses.
        coord = 2,1

        events = [au_event.Ev_Plains_Lonely_Tier1_IntrospectionOne(char)]

        super(Region_Plains_Illusion,self).__init__(char,intro,coord,events)
        
class Region_Arctic(Region):
    def __init__(self, char : "Character"):
        intro = "{0} finds {1} at the border of a land of malevolent \
                ice and snow. Hail immediately pelts {2} as {3} steps \
                foot inside. This won't be fun.".format(
                    char.get_name,"HIMSELF/HERSELF","HIM/HER","HE/SHE")
        coord = 2,0

        events = [au_event.Ev_Forest_TierOne_TreeFallsDown(char)] #TO BE POPULATED

        super(Region_Arctic,self).__init__(char,intro,coord,events)
        
class Region_Mountain(Region):
    def __init__(self, char : "Character"):
        intro = "A series of mountains loom over {0}. A \
                sign is posted at the summit. It reads: \
                'TROLL TERRYTORRY. KEEP OUT!!!' Below that \
                is a crudely drawn butt labeled 'THIS IS U' \
                What obnoxious jerks these trolls. {0} forges on \
                ahead.".format(char.get_name)
        coord = 2,2

        events = [au_event.Ev_MountainRange_TierOne_MysteriousBoulder(char)]

        super(Region_Mountain,self).__init__(char,intro,coord,events)

def move_direction(region : Region, cardinal : str) -> Region:
    '''Returns the region in the cardinal direction of the given region.'''
    if cardinal == NORTH:
        return region.get_North()
    elif cardinal == SOUTH:
        return region.get_South()
    elif cardinal == WEST:
        return region.get_West()
    elif cardinal == EAST:
        return region.get_East()
    else:
        raise InvalidRegionDirectionError()
