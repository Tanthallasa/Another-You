#event class

###How Events Happen and Work:
##1. Player walks in real life, which makes them move a direction
##2. A region in entered, and an event selected randomly
##3. That event's intro text and picture are displayed
##4. The player's options are displayed (how and where TBD)
##5. The player selects one of the options. That option causes either:

#6a. Outcome of decision displayed.
#7a. Consequences (loss of health, reward accrued, etc.)
#8a. End of Event

##Or:

#6b. New event called, start cycle from 3.

import au_classes
from random import randrange

class Event:
    def __init__(self, char : "Character", intro : str, options : [str], picture : "???", region : "Region"):
        self._char = char   #Event classes need to be aware of the
                            #character to affect him/her.
        self._intro_text = intro
        self._options = options
        self._picture = picture #Don't know how to handle this yet
        self._region = region

    def get_intro_text(self):
        return self._intro_text

    def get_options(self) -> ["List of Options"]:
        return self._options

    def get_num_of_options(self) -> int:
        '''So we don't have to format buttons and text blindly.'''
        return len(self._options)

    def get_picture(self):
        return self._picture

    def get_region(self):
        return self._region

    def select_option(self, selection : int):
        '''An option is selected (0-3?), and its appropriate
    function called. select_option() will return what it receives
    from these functions. That function will return a str if it
    signifies the end of the sequence of events. If there are more
    events to play through, it returns that event object instead.

    Whatever ends up calling this (World class?) will need to be
    able to handle both.'''

        if(selection == 0):
            return self.option_zero()
        elif(selection == 1):
            return self.option_one()
        elif(selection == 2):
            return self.option_two()
        elif(selection == 3):
            return self.option_three()

    def option_zero(self):
        pass
    def option_one(self):
        pass
    def option_two(self):
        pass
    def option_three(self):
        pass

#Naming Convention:
#Ev_<REGION>_Tier<TIER NUMBER>_<EVENT TITLE/DESCRIPTION>
    #Forest Fairy: Mischevious Fairies, Randomness
    #Forest Dark: Creepy evil lurking in shadows: Benefits are rare
    #Dungeon: Ominous potential. <>
    #Desert: Hints at true nature. <>
    #City: Superficial niceties. Nothing bad happens... but nothing good.
        #They aren't real.
    #Plains Lonely: Alt. Player battles with introspection.
    #Plains Illusion: Pretends to be above. <>
    #Arctic: Literally hates the Alt. Player and is trying to murder him/her.
    #Mountain: Everything is either the difficulties of hiking or jerkass trolls.
class Ev_Forest_TierOne_TreeFallsDown(Event):
    def __init__(self, char : "Character"):
        name = char.get_name()
        intro_text = "{0} hears a whicker-snap nearby... oh no!\n"+\
                     "A nearby tree is about to collapse onto {0}'s\n"+\
                     "head, and {1} hasn't noticed!"
        intro_text = intro_text.format(name, char.personal().lower())
        
        option_0 = "Use mana to forcibly push the tree away from {}. [-1 Mana]".format(name)
        option_1 = "Project a subtle (but urgent) warning into {}'s mind.".format(name)
        option_2 = "Do nothing, let {} handle it.".format(name)

        options = [option_0,option_1,option_2]

        picture = "forest_tier1_treefallsdown.jpg"
        region = "The forest, but will this be a str or a class or what? TBD!"

        super(Ev_Forest_TierOne_TreeFallsDown,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.mp_down()
        outcome = "You push the tree out of the way for {0}. {0} is none\n"+\
                "the wiser."
        return outcome.format(self._char.get_name())

    def option_one(self) -> str:
        self._char.str_up()
        outcome = "You gently nudge {0}'s awareness, and {0} takes action!\n"+\
                  "{1} successfully dodges the falling tree, and feels pretty\n"+\
                  "good about {2}. {0} feels a little stronger."
        return outcome.format(self._char.get_name(),self._char.personal(),self._char.reflexive().lower())

    def option_two(self) -> str:
        self._char.hp_down()
        self._char.hp_down()
        outcome = "Deciding not to take action, the incredibly heavy tree\n"+\
                  "falls down onto unsuspecting {}'s head. Ouch!"
        return outcome.format(self._char.get_name())


class Ev_Forest_TierOne_WildBoar(Event):
    def __init__(self, char : "Character"):
        name = char.get_name()
        intro_text = "An enraged wild boar emerges from the underbrush!\n"+\
                     "{0} is in danger, but draws a sword in preparation"
        intro_text = intro_text.format(name)
        
        option_0 = "Use mana to strike the boar with a falling tree branch. [-1 Mana]".format(name)
        option_1 = "Urge {0} to attack the boar head-on.".format(name)
        option_2 = "Do nothing, let {0} handle it.".format(name)

        options = [option_0,option_1,option_2]

        picture = "picture_of_boar_attacking"
        region = "The forest, but will this be a str or a class or what? TBD!"

        super(Ev_Forest_TierOne_WildBoar,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.mp_down()
        self._char.str_up()
        outcome = "You strike the beast down in front of {0}'s eyes! {0} wonders\n"+\
                  "at their luck, but nevertheless takes some meat to make a strength-\n"+\
                  "enhancing stew."
        return outcome.format(self._char.get_name())

    def option_one(self) -> str:
        self._char.hp_down()
        outcome = "Goaded by your simple idea, {0} charges the boar!\n"+\
                  "{0} suffers a scratch on the arm, but successfully defeats\n"+\
                  "the beast."
        return outcome.format(self._char.get_name())

    def option_two(self) -> str:
        outcome = "{0} waits for the boar to charge and gracefully dodges\n"+\
                  "to the side. {0}'s first strike kills the beast!"
        return outcome.format(self._char.get_name())


##class Ev_Region_Tier_Desc(Event):
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome  
        
class Ev_Forest_Fairy_TierOne_FairyRing(Event):
    def __init__(self, char : "Character"):
        name = char.get_name()
        intro_text = "While passing through the woods, {0} notices a\n"+\
                     "peculiar ring of mushrooms. The mushrooms shimmer\n"+\
                     "faintly, and {0} is drawn towards them."
        intro_text = intro_text.format(name)
        
        option_0 = "Do nothing. They're only mushrooms!"
        option_1 = "Destroy the mushrooms before {0} can reach them. [-1 Mana]".format(name)
        option_2 = "Encourage {0} to eat them.".format(name)

        options = [option_0,option_1,option_2]

        picture = "forest_fairy_tier1_fairyring.jpg"
        region = ""

        super(Ev_Forest_Fairy_TierOne_FairyRing,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        rand_int = randrange(4)
        rand_int2 = randrange(3)
        rand_color = "black"

        if rand_int2 == 0:
            rand_color = "pink"
        elif rand_int2 == 1:
            rand_color = "light blue"
        elif rand_int2 == 2:
            rand_color = "blood red"
            
        if rand_int == 0 or 1:
            self._char.cha_up()
            outcome = "{0} steps into the ring of mushrooms, and for an instant,\n"+\
                      "they glow {1}. {0} feels blessed somehow."
            outcome = outcome.format(self._char.get_name(),rand_color)
            
        elif rand_int == 2:
            self._char.hp_down()
            outcome = "{0} steps into the ring of mushrooms, and for an instant,\n"+\
                      "they glow {1} before popping out of the ground and lunging\n"+\
                      "towards {0}! {0} successfully fends the malevolent mushrooms\n"+\
                      "off, but not before suffering from several painful bites."
            outcome = outcome.format(self._char.get_name(),rand_color)
        elif rand_int == 3:
            outcome = "{0} steps into the ring of mushrooms, and for an instant,\n"+\
                      "they glow {1}. {0} doesn't *think* {2} feels any different..."
            outcome = outcome.format(self._char.get_name(),rand_color,self._char.personal())
        

        return outcome

    def option_one(self) -> str:
        self._char.mp_down()
        outcome = "You use a smidgeon of your trans-dimensional magic power to burn\n"+\
                  "small mushrooms to ashes. {0} can hear tiny, high-pitched squeels of despair."
        return outcome.format(self._char.get_name())

    def option_two(self) -> str:
        rand_int = randrange(2)
        rand_int2 = randrange(3)
        rand_flavor = "salty"
        if rand_int2 == 0:
            rand_flavor = "sweet"
        elif rand_int2 == 1:
            rand_flavor = "sour"
        elif rand_int2 == 2:
            rand_flavor = "bitter"
            
        if rand_int == 0:
            self._char.hp_down()
            self._char.hp_down()
            outcome = "{0} picks one of the mushrooms from the ground and takes a bite. It tastes\n"+\
                      "unbearably {1}! {0} spits it out, gagging."
            outcome = outcome.format(self._char.get_name(), rand_flavor)
        elif rand_int == 1:
            self._char.hp_up()
            self._char.hp_up()
            outcome = "{0} picks one of the mushrooms from the ground and takes a bite. It tastes\n"+\
                      "deliciously {1}! {0} gulps the rest down with a grin."
            outcome = outcome.format(self._char.get_name(), rand_flavor)

        return outcome
    
        
class Ev_Forest_Fairy_TierOne_TrappedFairy(Event):
    def __init__(self, char : "Character"):
        name = char.get_name()
        pronoun_per = char.personal().lower()
        pronoun_pos = char.possessive().lower()
        pronoun_ref = char.reflexive().lower()

        self._fairy_color = "Purple"

        rand_int = randrange(2)
        if rand_int == 0:
            self._fairy_color = "Red"
        elif rand_int == 1:
            self._fair_color = "Blue"
        
        intro_text = "Walking through the woods, {0} hears the faint sound of weeping\n"+\
                     "in the distance. {1} heads toward it, and finds a small, {2}. She\n"+\
                     "pleads with {0} for assistance!"
        intro_text = intro_text.format(
                         name, pronoun_per, self._fairy_color.lower())
        
        option_0 = "Fairies are bad news. Send {0} bad vibes so he walks away.".format(name)
        option_1 = "Fairies can be very generous when helped. Nudge {0} towards helping.".format(name)
        option_2 = "Why is the fairy in there? Have {0} investigate.".format(name)

        options = [option_0,option_1,option_2]

        picture = "forest_fairy_tier1_fairycage.jpg"
        region = ""

        super(Ev_Forest_Fairy_TierOne_TrappedFairy,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        rand_int = randrange(2)
        rand_int2 = randrange(3)
        rand_color = "black"

        if rand_int2 == 0:
            rand_color = "pink"
        elif rand_int2 == 1:
            rand_color = "light blue"
        elif rand_int2 == 2:
            rand_color = "blood red"
            
        if rand_int == 0:
            outcome = "{0} walks away from the {1} fairy. Her plaintive weeping slowly\n"+\
                      "fades away until it is inaudible."
            outcome = outcome.format(
                          self._char.get_name(),self._fairy_color.lower())
            
        elif rand_int == 1:
            self._char.hp_down()
            outcome = '{0} walks away from the {1} fairy. "Well screw you too, ya jerk!"\n'+\
                      'she yells, throwing a small, {2} bolt of magic at {0}. Ouch!'
            outcome = outcome.format(
                          self._char.get_name(),self._fairy_color.lower(),rand_color)

        

        return outcome

    def option_one(self) -> str:
        name = self._char.get_name()
        pronoun_p = self._char.personal().lower()
        
        rand_int = randrange(5)
        outcome = "Just as you wanted, {0} is influenced into helping the {1} fairy out. {2}\n"+\
                  "makes short work of the cage's paltry lock, and the fairy is free!\n"
        if rand_int == 0 or rand_int == 1:
            self._cha_up()
            outcome += "She is truly grateful, and rewards {0} with a kiss on the cheek.\n"+\
                       "{0} feels like a better person!"
            outcome = outcome.format(name,self._fairy_color.lower(),pronoun_p)
        elif rand_int == 2 or rand_int == 3:
            self._hp_down()
            outcome += '"Sucker!" the mischevious fairy cries. {0} is "rewarded" only\n'+\
                       'with a bolt of painful magic to the nose. "Never trust a {1} fairy, fool!\n'+\
                       '{0} flees.'
            outcome = outcome.format(name,self._fairy_color.lower(),pronoun_p)
        elif rand_int == 4:
            outcome += '''"Thanks!" says the fairy. She then explodes in a burst of glitter
                       and confetti. {0} is baffled and confused.'''
            outcome = outcome.format(name, self._fairy_color.lower(),pronoun_p)
            
        
        return outcome

    def option_two(self) -> str:
        name = self._char.get_name()
        cha = self._char.get_cha()
        if cha > 3:
            outcome = '"Why are you even in that cage?" {0} gently asks.\n'+\
                      '"Oh, well," begins the fairy, "I stole medicine from fairy orphans. Why?"\n'+\
                      '{0} promptly leaves without helping the caged fairy.'
            outcome = outcome.format(name)
        else:
            self._char.hp_down()
            outcome = '"So, uh, why are you in there, exactly, fairy?" {0} nervously asks.\n'+\
                      '"Waiting for losers like you!" cackles the fairy. She promptly lobs\n'+\
                      '''a bolt of painful magic at {0}'s nose. Ouch!'''
            outcome = outcome.format(name)

        return outcome

class Ev_Forest_Dark_TierOne_SpiderAttack(Event):
    def __init__(self, char : "Character"):
        name = char.get_name()
        pronoun_p = char.personal().lower()
        pronoun_r = char.reflexive().lower()
        intro_text = "{0} walks through dark forest, visibly shaking. While nervously\n"+\
                     "glancing around, {1} walks straight into a huge spider-web and becomes stuck.\n"+\
                     "A hungry, gigantic spider crawls down from above..."
        intro_text = intro_text.format(name,pronoun_p)
        
        option_0 = "Quickly make {0} fight! {1} can escape!".format(name, pronoun_p)
        option_1 = "{0} won't be able to help {1}. Use mana to burn the web! [-2 Mana]".format(name, pronoun_r)
        option_2 = "Scream silently to yourself. Spiders are scary."

        options = [option_0,option_1, option_2]

        picture = "Forest_Dark_Tier1_SpiderAttack.jpg"
        region = ""

        super(Ev_Forest_Dark_TierOne_SpiderAttack,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        name = self._char.get_name()
        pronoun_pos = self._char.possessive().lower()
        outcome = '''{0} attempts to use {1} pure strength to break free from the spider's web...\n'''
        if self._char.get_str() > 3:
            outcome += "And it works! {0} breaks free, then quickly spins to scare off the spider\n"+\
                      "with {1} sword. The spider makes angry clicking noises, then retreats."
            outcome = outcome.format(name,pronoun_pos)
        else:
            self._hp_down(2)
            outcome += "But {0} can't break free in time! The malicious spider scurries down and punctures\n"+\
                       "{0}'s flesh with its fangs. This gives {0} enough adrenaline to escape and scare\n"+\
                       "the spider off, but not without significant pain."
            outcome = outcome.format(name, pronoun_pos)
                       
        return outcome

    def option_one(self) -> str:
        self._char.mp_down(2)
        outcome = "You fry the spider with firey magic. {0} breaks free from the now\n"+\
                  "burning web and watches, bewildered and amazed, at the spider that, from\n"+\
                  "{1} point of view, spontaneously combusted. {0} watches until the embers\n"+\
                  "eventually die out with a whimper."

        return outcome.format(self._char.get_name(),self._char.possessive().lower())

    def option_two(self) -> str:
        name = self._char.get_name()
        pronoun_pos = self._char.possessive().lower()
        outcome = '''{0} attempts to use {1} pure strength to break free from the spider's web...\n'''
        if self._char.get_str() > 3:
            outcome += "And it works! {0} breaks free, then quickly spins to scare off the spider\n"+\
                      "with {1} sword. The spider makes angry clicking noises, then retreats."
            outcome = outcome.format(name,pronoun_pos)
        else:
            self._hp_down(2)
            outcome += "{0} can't break free in time! The malicious spider scurries down and punctures\n"+\
                       "{0}'s flesh with its fangs. This gives {0} enough adrenaline to escape and scare\n"+\
                       "the spider off, but not without significant pain."
            outcome = outcome.format(name, pronoun_pos)
        return outcome

class Ev_Forest_Dark_Tier1_Darkness(Event): #Alt char gets lost in extreme shadow
    def __init__(self, char : "Character"):
        name = char.get_name()
        pronoun_p = char.personal().lower()
        intro_text = "The way forward is pitch black. The path {0} came from\n"+\
                     "is even darker. If that even is the way {1} came from...\n"+\
                     "{1} is no longe sure. {1} is lost.\n"
        intro_text = intro_text.format(name, pronoun_p)
        
        option_0 = "Light the way. [-2 Mana]".format(name)
        option_1 = "Conjure a map for {0}. [-1 Mana]".format(name)
        option_2 = "Urge {0} onward.".format(name)

        options = [option_0,option_1,option_2]

        picture = "Forest_Dark_Tier1_Darkness.jpg"
        region = ""

        super(Ev_Forest_Dark_Tier1_Darkness,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.mp_down(2)
        outcome = "The world around {0} miraculously lights up. Sinister creatures that\n"+\
                  "had been stalking {0} fall over themselves in fright and flee. {0}\n"+\
                  "is shocked, but quickly takes advantage of the sudden illumination\n"+\
                  "to flee the forest safely."
        return outcome.format(self._char.get_name())

    def option_one(self) -> str:
        self._char.hp_down()
        outcome = "You conjure a map for {0}. Unfortunately, a map can't help\n"+\
                  "a person lost in darkness. Fortunately, the creepy-crawlies\n"+\
                  "stalking {0} are just as bewildered by this sudden map that they\n"+\
                  "leave {0} alone on their confusion. Mostly."
        return outcome.format(self._char.get_name())

    def option_two(self) -> str:
        rand_int = randrange(3)
        name = self._char.get_name()
        if rand_int == 0 or rand_int == 1:
            self.char.hp_down(2)
            outcome = "Your guidance proves to be useless; you don't know where {0}\n"+\
                      "either! {0} wanders, lost, before eventually emerging from the\n"+\
                      "dark forest much worse for wear."
            outcome = outcome.format(name)
        elif rand_int == 2:
            outcome = '''Amazingly, your subtle guidance of {0}'s actions bears fruit. {0} escapes unharmed!'''.format(name)

        return outcome


class Ev_Dungeon_Tier1_EntranceSearch(Event):
    def __init__(self, char : "Character"):
        name = char.get_name()
        obj = char.personal_obj().lower()
        intro_text = "{0} thinks that there *must* be a way into this place. After an hour of searching,\n"+\
                     "{1} only manages to find three things of interest: a discolored brick, a hole in the ground\n"+\
                     "and a shard of glass. Slim pickings."
        intro_text = intro_text.format(name, char.personal().lower())
        
        option_0 = "Have {0} investigate the brick.".format(obj)
        option_1 = "Have {0} investigate the hole.".format(obj)
        option_2 = "Have {0} investigate the glass shard".format(obj)

        options = [option_0,option_1,option_2]

        picture = ""
        region = ""

        super(Ev_Dungeon_Tier1_EntranceSearch,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.hp_up()
        outcome = "{0}'s investigations reveal nothing. Except for its slight miscoloration,\n"+\
                  "the brick is like all the other bricks that form the castle's exterior. Of note,\n"+\
                  "however, is the peculiar lack of vines on the walls; you'd think some would\n"+\
                  "have grown on something so ancient."
        return (outcome + "\n At least the hour spent was very relaxing.").format(self._char.get_name())

    def option_one(self) -> str:
        self._char.hp_up()
        outcome = "{0}'s investigations reveal nothing. The hole seems to have been made by an animal\n"+\
                  "of some sort... and then abandoned. Odd, but ultimately a dead-end."
        return (outcome + "\n At least the hour spent was very relaxing.").format(self._char.get_name())

    def option_two(self) -> str:
        self._char.hp_up()
        outcome = "{0}'s investigations reveal nothing. The glass shard is mundane, and {0} is\n"+\
                  "unable to find any explanation for why it's there. Maybe someone else was here?\n"+\
                  "But then, why is there only a single shard? Strange."
        return (outcome + "\n At least the hour spent was very relaxing.").format(self._char.get_name())


class Ev_Dungeon_Tier1_MysteriousPuzzle(Event):
    def __init__(self, char : "Character"):
        name = char.get_name()
        intro_text = "{0} finds a poem etched into the castle's walls! It reads:\n"+\
        "'Parallel existance\n"+\
        "Movements mirrored\n"+\
        "Two in a dance\n"+\
        "One with doomed wyrd'\n"+\
        "{0} can't make heads or tails of it."
        intro_text = intro_text.format(name)
        
        option_0 = "What does 'wyrd' mean?"
        option_1 = "I don't like the implications.".format(name)
        option_2 = "{0} should stop reading that. Make {1} stop reading that.".format(name,char.personal_obj())
        
        options = [option_0,option_1,option_2]

        picture = ""
        region = ""

        super(Ev_Dungeon_Tier1_MysteriousPuzzle,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.hp_up()
        outcome = '''"Destiny," your screen reads.\n "Oh. Uh. Okay," you think.'''
        return outcome

    def option_one(self) -> str:
        self._char.hp_up()
        outcome = '''"Good," displays your game. \n It also displays that.\n And this.'''
        return outcome

    def option_two(self) -> str:
        self._char.hp_up()
        outcome = '''"No," reads the text. \n And {0} does not stop until {1} {2} wishes to. It takes half an hour for {3} to leave.'''.format(
            self._char.get_name(),self._char.personal().lower(),self._char.reflexive().lower(),self._char.personal_obj().lower())
        return outcome


class Ev_Desert_Tier1_ShiftingSands(Event): #The sand shifts in ways it's not supposed to
    def __init__(self, char : "Character"):
        name = char.get_name()
        pronoun_p = char.possessive().lower()
        intro_text = "{0} hikes through burning desert. The blazing hot sun glares down\n"+\
                     "at the sweating wanderer. Suddenly, the sand under {0} shifts and gives way to\n"+\
                     "reveal a heretofore hidden chasm! {0} loses {1} balance and begins to slide\n"+\
                     "toward the dark unknown."
        intro_text = intro_text.format(name, pronoun_p)
        
        option_0 = "Project encouraging words into {0}'s mind.".format(name)
        option_1 = "Use your trans-dimensional abilities to lift {0} to safety.[-1 Mana]".format(name)
        option_2 = "Use your parallel-universe magic to stop the shifting sands [-1 Mana]".format(name)

        options = [option_0,option_1,option_2]

        picture = ""
        region = ""

        super(Ev_Desert_Tier1_ShiftingSands,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        strength =  self._char.get_str()
        name = self._char.get_name()
        pronoun_p = self._char.possessive().lower()
        pronoun_o = self._char.personal_obj().lower()
        pronoun_r = self._char.reflexive().lower()

        if strength >= 5:
            outcome = "{0} manages to use {1} strength to pull {2} to safety.\n"+\
                      "You're certain your words of encouragement made a difference."
            outcome = outcome.format()
        else:
            self._char.hp_down(2)
            outcome = "{0} falls down, landing painfully. It takes an entire\n"+\
            "hour of effort for {1} to climb back up again."
            outcome = outcome.format(name,pronoun_o)
        return outcome

    def option_one(self) -> str:
        self._char.mp_down()
        outcome = "{0} is incredibly perplexed, but safe. {1} sits down on the stand,\n"+\
                  "panting, and looking up at the sky."
        return outcome.format(self._char.get_name(),self._get.personal())

    def option_two(self) -> str:
        self._char.mp_down()
        strength =  self._char.get_str()
        name = self._char.get_name()
        pronoun_p = self._char.possessive().lower()

        if strength >= 3:
            outcome = "You stop the shifting sands long enough for {0} to use {1} strength\n"+\
                      "and escape. In {1} desperate scramble, {0} did not notice your assistance,\n"+\
                      "and is none the wiser."
            outcome = outcome.format(name,pronoun_p)
        else:
            self._char.hp_down(2)
            outcome = "Your try to subtly assist {0}, but it isn't enough! {0} is just too weak\n"+\
                      "to overcome the sand's momentum, and falls down the small chasm, landing\n"+\
                      "painfully. It takes an entire hour of effort for {1} to climb back up again."
            outcome = outcome.format(name, self._char.personal_obj().lower())
        return outcome


##class Ev_Desert_Tier1_AbandonedHarbor(Event): #A harbor... in the desert?
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome

class Ev_City_Tier1_HappyInn(Event): #Regen HP... but people are strange. {0} does not notice.
    def __init__(self, char : "Character"):
        name = char.get_name()
        intro_text = "{0} finds one of the city's inns and asks the innkeeper for a room.\n"+\
                     '"Yes. Of course you may, {0}. You are always welcome here." says the\n'+\
                     'innkeeper, grinning too wide. "Aaalwaaays," he continues.\n'+\
                     "{0} did not give out {1} name, but does not notice that, pleased\n"+\
                     "with the innkeeper's hospitality."
        intro_text = intro_text.format(name, char.possessive().lower())
        
        option_0 = "Uh, run, {0}. Run so, so far away.".format(name)
        option_1 = "Use your cross-dimension voodoo to punch the innkeeper immediately [-1 Mana]"
        option_2 = "Project a though into the innkeeper's mind: 'Stop being so creepy, man. Come on.'"

        options = [option_0,option_1,option_2]

        picture = ""
        region = ""

        super(Ev_City_Tier1_HappyInn,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.hp_up(2)
        outcome = "{0} does indeed run! However, the place {1} runs to is the room {1}\n"+\
                  "just paid for, where {1} rests peacefully. You hope {1} is not brutally\n"+\
                  "stabbed in {2} sleep."
        return outcome.format(self._char.get_name(), self._char.personal(),self._char.possessive().lower())

    def option_one(self) -> str:
        self._char.hp_up(2)
        outcome = "You violently use magic to punch the innkeeper's nose. The innkeeper does\n"+\
                  'not react save to say, "Oh dear, I have appeared to have gotten a nose bleed,"\n'+\
                  "his grin never faltering. {0} accepts this easily, and rests in the room {1}'s\n"+\
                  "rented."
        return outcome.format(self._char.get_name(),self._char.personal())

    def option_two(self) -> str:
        self._char.hp_up(2)
        outcome = '''"I don't know what you mean," the innkeeper says to no one in particular, grinning.\n'''+\
                  "{0}, though, takes it as confusion, and repeats {1} request for a room. The innkeeper obliges,\n"+\
                  "and {0} rests in the city of grinning, always grinning people."
        return outcome.format(self._char.get_name(),self._char.possessive().lower())


##class Ev_City_Tier1_HappyStreets(Event): #Everyone is so smiley and happy! regen hp
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome

class Ev_Plains_Lonely_Tier1_IntrospectionOne(Event): #What am I? Who am I?
    def __init__(self, char : "Character"):
        name = char.get_name()
        pronoun_obj = char.personal_obj()
        intro_text = "{0} walks through the empty plains.\n"+\
                     "There is nothing around except {1} thoughts.\n"+\
                     '"Who am I?" {2} thinks. Do you answer?'
        intro_text = intro_text.format(name, char.possessive().lower(),char.personal().lower())
        
        option_0 = '"A warrior," you tell {0}'.format(pronoun_obj.lower())
        option_1 = '"A good person," you tell {0}'.format(pronoun_obj.lower())
        option_2 = "You say nothing."

        options = [option_0,option_1,option_2]

        picture = ""
        region = ""

        super(Ev_Plains_Lonely_Tier1_IntrospectionOne,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        name = self._char.get_name()
        self._char.str_up()
        outcome = "{0} nods to {1} and journeys on.".format(name,self._char.reflexive().lower())
        return outcome

    def option_one(self) -> str:
        name = self._char.get_name()
        self._char.cha_up()        
        outcome = "{0} nods to {1} and journeys on.".format(name,self._char.reflexive().lower())
        return outcome

    def option_two(self) -> str:
        name = self._char.get_name()
        self._char.mp_up(2)
        outcome = "{0} thinks to {1} for a long time, and finds {2} answers... unsatisfactory.".format(name,self._char.reflexive().lower(),self._char.possessive().lower())
        return outcome


##class Ev_Plains_Lonely_Tier1_IntrospectionTwo(Event): #Am I in control of my life? What is out there?
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome

##class Ev_Arctic_Tier1_MenacingAttention(Event):
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome

##class Ev_Arctic_Tier1_FreezingSnow(Event):
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome

##class Ev_Plains_Illusion_Tier1_Idiot(Event):
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome

##class Ev_Plains_Illusion_Tier1_Trick(Event): #I bet if you do this [dumb thing] you'll get stronger!
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome


class Ev_MountainRange_TierOne_MysteriousBoulder(Event):
    def __init__(self, char : "Character"):
        name = char.get_name()
        intro_text = "{0} is hiking through the mountains and comes across\n"+\
                     "a huge boulder with a jagged crack down the middle of it.\n"+\
                     "Something valuable could be inside... Or something dangerous!"
        intro_text = intro_text.format(name)
        
        option_0 = "Use mana to break the rock open, revealing whatever lies inside. [-2 Mana]".format(name)
        option_1 = "Urge {0} to leave the boulder alone.".format(name)
        option_2 = "Do nothing, let {} handle it.".format(name)

        options = [option_0,option_1,option_2]

        picture = "picture_of_boulder"
        region = "The mountain range, but will this be a str or a class or what? TBD!"

        super(Ev_MountainRange_TierOne_MysteriousBoulder,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.mp_down()
        self._char.mp_down()
        self._char.hp_down()
        self._char.cha_up()
        outcome = "As the boulder shatters, a snake lunges out at {0}. {0} gets bitten but\n"+\
                  "manages to kill the snake. Inside the wreckage of the boulder, {0} finds a\n"+\
                  "potion, which is swiftly quaffed"
        return outcome.format(self._char.get_name())

    def option_one(self) -> str:
        outcome = "{0} is receptive of your gentle guidance. {0} ignores the\n"+\
                  "boulder and moves on."
        return outcome.format(self._char.get_name())

    def option_two(self) -> str:
        self._char.hp_down()
        outcome = "{0} decides to look in the crack in the boulder. A snake lunges\n"+\
                  "out and bites {0}!"
        return outcome.format(self._char.get_name())
    
##class Ev_Mountain_Tier1_TrollCannonball(Event):
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome  

##class Ev_Mountain_Tier1_TrollsThrowRocks(Event):
##    def __init__(self, char : "Character"):
##        name = char.get_name()
##        intro_text = ''''''.format(name)
##        
##        option_0 = "".format(name)
##        option_1 = "".format(name)
##        option_2 = "".format(name)
##        option_3 = "".format(name)
##
##        options = [option_0,option_1,option_2,option_3]
##
##        picture = ""
##        region = ""
##
##        super(Ev_Region_Tier_Desc,self).__init__(char,intro_text,options,picture,region)
##
##    def option_zero(self) -> str:
##        self._char.<>
##        outcome = ''''''.format(self._char.get_name())
##        return outcome
##
##    def option_one(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_two(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome
##
##    def option_three(self) -> str:
##        self._char.<><
##        outcome = ''''''
##        return outcome  
