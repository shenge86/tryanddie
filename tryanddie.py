# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:41:27 2021

@author: sheng
"""

#%% ASCII art
person = r"""
        
              ////^\\\\
              | ^   ^ |
             @ (o) (o) @
              |   <   |
              |  ___  |
               \_____/
             ____|  |____
            /    \__/    \
           /              \
          /\_/|        |\_/\
         / /  |        |  \ \
        ( <   |        |   > )
         \ \  |        |  / /
          \ \ |________| / /
"""

mushroom = r"""
                       .-'~~~-.
                     .'o  oOOOo`.
                    :~~~-.oOo   o`.
                     `. \ ~-.  oOOo.
                       `.; / ~.  OO:
                       .'  ;-- `.o.'
                      ,'  ; ~~--'~
                      ;  ;
_______\|/__________\\;_\\//___\|/________

"""

cave = r"""
 ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \            |            \ *
 ********************************************************************************

"""

#%% classes
class Person():
    def __init__(self,name,energy):
        self.name = name
        self.energy = energy
    
    # @property
    # def name(self):
    #     return self._name
    
    @property
    def energy(self):
        return self._energy
    
    @energy.setter
    def energy(self,val):
        self._energy = val
        print("My energy feels like it has changed.")
        print("Energy: ", self._energy)
        
        if self.energy <= 5:
            print("I am starting to feel weak.")
            
        if self.energy <= 0:
            print("Oh my god! I feel faint. I think I might be ...")
            print("DEAD!")
            
    def reset(self,name):
        print("I suddenly feel strength flowing through my body again.")
        print("*Gasp* I am alive!")
        self._name = name
        self._energy = 10
        return self
    
    # human actions
    def eat(self,edible,energy):
        print(f"I ate the {edible}.")
        self.energy += energy
        
    def yell(self,words):
        print("I yelled as loudly as possible!")
        print(words)
    
    def fidget(self):
        print("Fidgeting while standing here doesn't really help my current situation.")
        print(person)
        
    def system(self):
        print(f"Hello {self.name}! Welcome to the System help screen.")
        print("Your stats are as follows:")
        print("Energy:", self.energy)
        print("Your actions possible are as follows:")
        print("eat, fidget, system, yell")
        print("Remember you just need to think of the word system and this will appear!")
        
class Room():
    def __init__(self,name,visited):
        self.name = name
        self.visited = visited

class Enviro():
    def __init__(self,deathstate,person_name):
        self.deathstate = 0
        self.person = Person(" ".join(w.capitalize() for w in person_name.split()),10)
        self.rooms = {}
    
    @property
    def deathstate(self):
        return self._deathstate
    
    @deathstate.setter
    def deathstate(self,val):
        self._deathstate = val
    
    # person classes
    @property
    def personenergy(self):
        return self.person._energy
    
    @personenergy.setter
    def personenergy(self,val):
        self.person.energy = val
        if self.person.energy <= 0:
            print("How many times have I died now?")
            self._deathstate += 1
            print("Oh, ", self.deathstate)
            self.person = self.person.reset(self.person.name)
    
    # room classes
    def create_room(self,name):
        # print(name)
        self.rooms.update({name:Room(name,False)})
    
    @property
    def room_state(self):
        # print(self.rooms)
        return self.rooms
    
    # check whether particular room has been visited
    def room_visit(self,roomname):
        return self.room_state[roomname].visited

    # change room to visited
    def room_visited_set(self,roomname):
        self.room_state[roomname].visited = True

#%% events and encounters
def room_cave(loop):
    if not enviro.room_visit('cave'):
        print("I look around and I see that I am in a dark cave lit up by mushrooms.")
        print(mushroom)
        enviro.room_visited_set('cave')
    
    if loop==1:
        input_one = input("Am I in a virtual reality simulation? Whatever the case is, I don't want to stay in this dark any longer than I need to.\n> ")
        
    if input_one.lower() in ['shout', 'yell', 'scream']:
        enviro.person.yell("The echoes came back. There was no other response.")
        print("Wow, that was quite the waste of energy, I thought.")   
        enviro.personenergy -=1
    elif input_one.lower() in ['eat mushroom', 'eat', 'mushroom', 'yes', 'y']:
        enviro.person.eat("mushroom",1)
        print("I instantly started shrinking. Also, I feel a bit stronger.")
        print("Now that I am the size of a mouse, I can see that in front of me there is a small tunnel.")
        print("It is possibly made by a small rodent.")
        loop=2
    else:
        enviro.person.fidget()


#%% Test
Test = False
if Test:
    enviro = Enviro(0)
    enviro.create_room('study')
    enviro.room_state
    room_visited_state = enviro.room_visit('study')
    print(room_visited_state)
    enviro.room_visited_set('study')
    room_visited_state = enviro.room_visit('study')
    print(room_visited_state)
        
#%%
if __name__ == '__main__':
    print("---------------------------------------------------------")
    print("Welcome to Try and Die - A Text Game of Possible Death")
    print("In this game, dying may be necessary to ultimately win.")
    print("---------------------------------------------------------")
    # shen = Person('Shen',10)
    # print('Current energy: ', shen.energy)
    print("A weird sensation struck me once I regained awareness.")
    print("'What the hell? Is this a dream?' Somehow everything seems strangely familiar. I asked myself.")
    print("Who am I anyway? After a moment of clutching my head, I slowly recalled my name.")
    person_name = input("'I can't remember anything else but at least I know my name is: ")
    enviro = Enviro(0,person_name)
    print(f"Ah, that's right. My name is {enviro.person.name}")
    
    print("Suddenly, a massive blue screen filled my view. It was the most realistic hallucination I have ever seen.")
    enviro.person.system()
    
    loop = 1
    while True:
        # first input loop
        enviro.create_room('cave')
        while loop == 1:
            if not enviro.room_visit('cave'):
                print("I look around and I see that I am in a dark cave lit up by mushrooms.")
                print(mushroom)
                enviro.room_visited_set('cave')
            
            if loop==1:
                input_one = input("Am I in a virtual reality simulation? Whatever the case is, I don't want to stay in this dark any longer than I need to.\n> ")
                
            if input_one.lower() in ['shout', 'yell', 'scream']:
                enviro.person.yell("The echoes came back. There was no other response.")
                print("Wow, that was quite the waste of energy, I thought.")   
                enviro.personenergy -=1
            elif input_one.lower() in ['eat mushroom', 'eat', 'mushroom', 'yes', 'y']:
                enviro.person.eat("mushroom",1)
                print("I instantly started shrinking. Also, I feel a bit stronger.")
                print("Now that I am the size of a mouse, I can see that in front of me there is a small tunnel.")
                print("It is possibly made by a small rodent.")
                loop=2
            else:
                enviro.person.fidget()                
                
        while loop == 2:
            if loop==2:
                print("Well, this is pretty tight but I think I can squeeze in.")
                input_two = input("Should I climb in?\n> ")
            
            if input_two.lower() in ['system']:
                enviro.person.system()
                
            if input_two.lower() in ['climb', 'yes', 'y']:
                print("I start to slowly crawl into the dirt tunnel. It is extremely hard to shuffle in this tunnel.")
                print("Since I am scared of snakes, I move exceedingly slowly.")
                print("Finally I exit into a much larger cavern. To my present size, it was automatically gigantic.")
                print("I look around and try to grasp my bearing. There appears to be light directly in front of me. There are also other mushrooms laying around for me to eat.")
                print("Ugh! Those taste gross but maybe eating one of those will make me bigger again? I'll hate to go outside in my current size.")
                loop=3
            else:
                enviro.person.fidget()
                                
        while loop == 3:
            if loop==3:
                print("I purse my lips and ponder on what to do.")
                input_three = input("Should I go towards the light or eat mushrooms?\n> ")
            
            if input_three.lower() in ['eat mushroom', 'eat', 'mushroom']:
                enviro.person.eat("mushroom",1)
                print("Yum! Just kidding. That was really gross but I did it any way.")
                print("I started to grow larger like Alice in Wonderland.")
                print("Time to get out of here!")
                loop=4
            elif input_three.lower() in ['leave', 'outside', 'light', 'yes', 'y']:
                print("I chose to ignore the mushrooms and go directly outside.")
                loop=4
            else:
                enviro.person.fidget()
                
        enviro.create_room('outside')
        while loop == 4:
            if not enviro.room_visit('outside'):
                print("Stepping into the light, I quickly realized that I am about to step off of a cliff.")
                print("'Woah! Let me back up a step here.' I exclaim as I hurriedly back up from the edge.")
                print(cave)
                enviro.room_visited_set('outside')
                
            if loop==4:                
                input_four = input("What should I do now?\n>")
                
            if input_four.lower() in ['look','see','examine']:
                print("I look around and notice a small track to the right of me. It looks like a path down the nountain.")
                loop=1
            elif input_four.lower() in ['track','right']:
                print("I walk towards the track on my right and start descending.")
                loop=6
            elif input_four.lower() in ['jump','j','yes','y']:
                print("Taking a look down I can see that I'm at least a couple of hundred feet above the ground.")
                print("If this is a simulation or a dream, I should be able to survive if I jump right?")
                jumpornot = input("Should I try my luck and see if I can land safely?")                
                if jumpornot.lower() in ['yes','y']:
                    print("I jump off and in a short while I impacted the ground.")
                    print("OUCH! That really hurts.")
                    enviro.personenergy-=11
                    loop=5
                else:
                    print("I slowly back away from the edge.")
            else:
                enviro.person.fidget()
                
        while loop == 5:
            if enviro.person.energy <= 0:
                room_cave(1)
            else:
                print("Wow! I can't believe I'm still alive!")
                
        while loop == 6:
            print("The trail is long and tedious to walk down but thankfully not too rough.")