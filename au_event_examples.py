


class Ev_Forest_TierOne_WildBoar(Event):
    def __init__(self, char : au_classes.Character):
        name = char.get_name()
        intro_text = '''An enraged wild boar emerges from the underbrush!
                     {0} is in danger, but draws a sword in preparation'''.format(name)
        
        option_0 = "Use mana to strike the boar with a falling tree branch. [-1 Mana]".format(name)
        option_1 = "Urge {0} to attack the boar head-on. [0 Mana]".format(name)
        option_2 = "Do nothing, let {} handle it. [0 Mana]".format(name)

        options = [option_0,option_1,option_2]

        picture = "picture_of_boar_attacking"
        region = "The forest, but will this be a str or a class or what? TBD!"

        super(Ev_Forest_TierOne_WildBoar,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.mp_down()
        self._char.str_up()
        outcome = '''You strike the beast down in front of {0}'s eyes! {0} wonders
                  at their luck, but nevertheless takes some meat to make a strength-
                  enhancing stew.'''.format(self._char.get_name())
        return outcome

    def option_one(self) -> str:
        self._char.hp_down()
        outcome = '''Goaded by your simple idea, {0} charges the boar!
                  {} suffers a scratch on the arm, but successfully defeats
                  the beast.'''.format(self._char.get_name())
        return outcome

    def option_two(self) -> str:
        outcome = '''{0} waits for the boar to charge and gracefully dodges
                  to the side. {0}'s first strike kills the beast!'''.format(self._char.get_name())
        return outcome

class Ev_MountainRange_TierOne_MysteriousBoulder(Event):
    def __init__(self, char : au_classes.Character):
        name = char.get_name()
        intro_text = '''{0} is hiking throught he mountains and comes across
                     a huge boulder with a jagged crack down the middle of it.
                     Something valuable could be inside... Or something dangerous!'''.format(name)
        
        option_0 = "Use mana to break the rock open, revealing whatever lies inside. [-2 Mana]".format(name)
        option_1 = "Urge {0} to leave the boulder alone. [0 Mana]".format(name)
        option_2 = "Do nothing, let {} handle it. [0 Mana]".format(name)

        options = [option_0,option_1,option_2]

        picture = "picture_of_boulder"
        region = "The mountain range, but will this be a str or a class or what? TBD!"

        super(Ev_MountainRange_TierOne_MysteriousBoulder,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.mp_down()
        self._char.mp_down()
        self._char.hp_down()
        self._char.cha_up()
        outcome = '''As the boulder shatters, a snake lunges out at {0}. {0} gets bitten but
                  manages to kill the snake. Inside the wreckage of the boulder, {0} finds a 
                  potion.'''.format(self._char.get_name())
        return outcome

    def option_one(self) -> str:
        outcome = '''{0} is receptive of your gentle guidance. {0} ignores the
                  boulder and moves on.'''.format(self._char.get_name())
        return outcome

    def option_two(self) -> str:
        self._char.hp_down()
        outcome = '''{0} decides to look in the crack in the boulder. A snake lunges
                  out and bites {0}!'''.format(self._char.get_name())
        return outcome

class Ev_MountainRange_TierOne_MysteriousBoulder(Event):
    def __init__(self, char : au_classes.Character):
        name = char.get_name()
        intro_text = '''{0} is hiking throught he mountains and comes across
                     a huge boulder with a jagged crack down the middle of it.
                     Something valuable could be inside... Or something dangerous!'''.format(name)
        
        option_0 = "Use mana to break the rock open, revealing whatever lies inside. [-2 Mana]".format(name)
        option_1 = "Urge {0} to leave the boulder alone. [0 Mana]".format(name)
        option_2 = "Do nothing, let {} handle it. [0 Mana]".format(name)

        options = [option_0,option_1,option_2]

        picture = "picture_of_boulder"
        region = "The mountain range, but will this be a str or a class or what? TBD!"

        super(Ev_MountainRange_TierOne_MysteriousBoulder,self).__init__(char,intro_text,options,picture,region)

    def option_zero(self) -> str:
        self._char.mp_down()
        self._char.mp_down()
        self._char.hp_down()
        self._char.cha_up()
        outcome = '''As the boulder shatters, a snake lunges out at {0}. {0} gets bitten but
                  manages to kill the snake. Inside the wreckage of the boulder, {0} finds a 
                  potion.'''.format(self._char.get_name())
        return outcome

    def option_one(self) -> str:
        outcome = '''{0} is receptive of your gentle guidance. {0} ignores the
                  boulder and moves on.'''.format(self._char.get_name())
        return outcome

    def option_two(self) -> str:
        self._char.hp_down()
        outcome = '''{0} decides to look in the crack in the boulder. A snake lunges
                  out and bites {0}!'''.format(self._char.get_name())
        return outcome
