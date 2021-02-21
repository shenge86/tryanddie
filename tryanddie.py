# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:41:27 2021

@author: Shen Ge
@name: Try and Die - A Text Game
"""

import os, sys
if sys.platform == "win32":
    os.system('color')
    
from sty import fg, bg, ef, rs

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
        self.inventory = ['cellphone','pen']
    
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
        self._inventory = ['cellphone','pen']
        return self
    
    # human actions
    def action(self,input_action):
        if input_action.lower() in ['jump','hop','leap']:
            self.jump()
        elif input_action.lower() in ['call']:
            self.call()
        elif input_action.lower() in ['drop']:
            obj = self.drop()
            return obj
        elif input_action.lower() in ['fuck']:
            self.fuck()
        elif input_action.lower() in ['lick']:
            self.lick()
        elif input_action.lower() in ['pick','pickup']:
            obj = self.pick()
            return obj
        elif input_action.lower() in ['system']:
            self.system()
        elif input_action.lower() in ['punch','attack']:
            self.punch()
        elif input_action.lower() in ['write']:
            self.write()
        else:
            self.fidget()

    def call(self,signal='bad'):
        if 'cellphone' in self.inventory:
            print("I pulled out my cellphone to try to make a call.")
            if signal == 'bad':
                print("No signal? This is not helpful.")
            else:
                pass
        else:
            print("I don't have a phone!")
    
    def drop(self):
        print("I want to drop something.")
        print(*self.inventory,sep=' ')
        obj = input("I chose to drop:\n> ")
        if obj in self.inventory:
            print(f"I dropped the {obj} on to the floor.")
            self.inventory.remove(obj)
            return obj
        else:
            print("I am not carrying that object.")
    
    def eat(self,edible,energy):
        print(f"I ate the {edible}.")
        self.energy += energy
    
    def fidget(self):
        print("Fidgeting while standing here doesn't really help my current situation.")
        print(person)
    
    def fuck(self):
        print("Since there was no one around to f*ck with, I simply yelled 'f*ck!' as loudly as I could. Whatever I expected didn't happen.")
    
    def jump(self):
        print("I jump straight into the air which accomplishes nothing at all.")
    
    def lick(self):
        print("I licked my mouth. Wow, chapped lips. I definitely need some chapstick.")

    def pick(self):
        print("I want to pick up something.")
        obj = input("I choose to pick up:\n> ")
        return obj
        #self.inventory.append(obj)
    
    def punch(self,target='air'):
        print(f"I punched the {target} as hard as I could.")
        print("Wow, that did absolutely nothing and I think I just used up some energy.")
        self.energy -= 1

    def write(self):
        if 'pen' in self.inventory:
            print("I take out my pen and drew a picture of my face.")
            print("Well, that was fun.")
        else:
            print("I don't have a pen or pencil.")

    
    def yell(self,words):
        print("I yelled as loudly as possible!")
        print(words)
        
    def system(self):
        print(f"Hello {self.name}! Welcome to the System help screen.")
        print("Your stats are as follows:")
        print("Energy: ", self.energy)
        print("Your unique actions possible are as follows:")
        print("call, eat, fidget, fuck, jump, lick, punch, system, write, yell")
        print("Inventory: ")
        print(*self.inventory,sep=' ')
        print("Remember you just need to think of the word system and this will appear!")

# room statuses        
class Room():
    def __init__(self,name,visited):
        self.name = name
        self.visited = visited
        self.corpses = 0
        self.inventory = []
    
    def room_add(self,obj):
        print(f"The {obj} is placed in the room.")
        self.inventory.append(obj)

    def room_drop(self,obj):
        if obj in self.inventory:
            print(f"The {obj} is picked up from the room.")
            self.inventory.remove(obj)
        else:
            print(f"Nothing like {obj} is seen here!")


# overall environment
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
        if name in self.rooms:
            print(f'What? I am at the {name} again?')
        else:
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
        # if self.room_state[roomname].visited:
        #     self.room_state[roomname].visited = False
        # else:
        #     self.room_state[roomname].visited = True
    
    # reset to not visited
    def room_visited_reset(self,roomname):
        self.room_state[roomname].visited = False
    
    def room_pickup(self,roomname,obj):
        if obj in self.person.inventory:
            self.rooms[roomname].room_add(obj)
            self.person.inventory.remove(obj)

    def person_pickup(self,roomname,obj):
        print("Trying to find: ", obj)
        if obj in self.rooms[roomname].inventory:
            self.rooms[roomname].room_drop(obj)
            self.person.inventory.append(obj)
        else:
            print(f"I don't see any item called {obj} that I can pick up.")

#%% events and encounters
def room_cave(loop):
    # first room resets all other rooms to 0
    for key in enviro.rooms:
        # print('resetting all rooms...')
        enviro.room_visited_reset(key)
        
    # first possible event at the cave
    while loop==1:
        # if not visited then create room
        print(mushroom)
        if not enviro.room_visit('cave'):
            print("I look around and I see that I am in a dark cave lit up by mushrooms.")
            print(f"Is that a corpse over there? I think I see {enviro.rooms['cave'].corpses} bodies.")
            print("I shudder and I decide to avoid the sight.")            
            enviro.room_visited_set('cave')
        
        if loop==1:
            print("Aside from the mushrooms, I see a few patches of mold, large boulders and possibly a few other items of interest. Objects of interest:")
            print(*enviro.rooms['cave'].inventory,sep=' ')
            input_one = input("Am I in a virtual reality simulation? Whatever the case is, I don't want to stay in this dark any longer than I need to.\n> ")
        
        if input_one.lower() in ['shout', 'yell', 'scream']:
            enviro.person.yell("The echoes came back. There was no other response.")
            print("Wow, that was quite the waste of energy, I thought.")   
            enviro.personenergy -=1
        elif input_one.lower() in ['eat mushroom', 'eat', 'mushroom', 'yes', 'y']:
            enviro.person.eat("mushroom",1)
            A = "I instantly started shrinking. Also, I feel a bit..."
            A1 = ef.bold + "stronger!" + ef.rs
            B = "Now that I am the size of a mouse, I can see that in front of me there is a small tunnel."
            C = "It is possibly made by a small rodent."
            print(A,A1,B,C)
            loop=2
            return loop
        
        # default actions capture all other actions
        obj = enviro.person.action(input_one)

        # interactions with the environment
        if input_one in ['drop']:
            #enviro.rooms['cave'].inventory.append(obj)
            enviro.rooms['cave'].room_add(obj)
            #print(enviro.rooms['cave'].inventory)

        if input_one in ['pick','pickup']:
            enviro.person_pickup('cave',obj)
        

def win():
    print("Holy moly! I am out of here and I am free. Suddenly, my entire memory comes back and I understand everything now.")
    exit()

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
    print(fg.red + "---------------------------------------------------------" + fg.rs)
    print(bg.blue + "Welcome to Try and Die - A Text Game of Possible Death" + bg.rs)
    print(ef.italic + "In this game, dying may be necessary to ultimately win." + rs.italic)
    print(fg.red + "---------------------------------------------------------" + fg.rs)
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
    
    # create rooms
    enviro.create_room('cave')
    enviro.create_room('outside')
    enviro.create_room('woods_one')
    
    loop = 1
    loop = room_cave(1)
    while True:                
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
                
        while loop == 4:
            if not enviro.room_visit('outside'):
                print("Stepping into the light, I quickly realized that I am about to step off of a cliff.")
                print("'Woah! Let me back up a step here.' I exclaim as I hurriedly back up from the edge.")
                print(cave)
                enviro.room_visited_set('outside')
                
            if loop==4:                
                input_four = input("What should I do now?\n>")
                
            if input_four.lower() in ['look','see','examine']:
                print("I look around and notice a small track to the right of me. It looks like a path down the mountain.")
            elif input_four.lower() in ['track','right']:
                print("I walk towards the track on my right and start descending.")
                loop=6
            elif input_four.lower() in ['jump','j','yes','y']:
                print("Taking a look down I can see that I'm at least a couple of hundred feet above the ground.")
                print("If this is a simulation or a dream, I should be able to survive if I jump right?")
                input_jumpornot = input("Should I try my luck and see if I can land safely?\n> ")                
                if input_jumpornot.lower() in ['yes','y']:                    
                    loop=5
                else:
                    print("I slowly back away from the edge.")
            else:
                enviro.person.fidget()
        
        while loop == 5:
            if not enviro.room_visit('woods_one'):
                enviro.room_visited_set('woods_one')
                if enviro.person.energy <= 11:
                    print("I jump off and in a short while I impacted the ground.")
                    print("OUCH! That really hurts.")
                    enviro.personenergy-=11
                    enviro.rooms['cave'].corpses+=1                    
                    loop=room_cave(1)
                else:
                    enviro.personenergy-=11
                    print("Wow! I can't believe I'm still alive!")
                    print("I looked around and noticed that I'm now in a small meadow surrounded by ominous looking massive trees.")
                    print("From my vantage point here, I can see that I can go north towards the woods or south towards uh ... also the woods.")
                    input_woods=input("Which woods should I head towards?\n> ")
                
        while loop == 6:
            print("The trail is long and tedious to walk down but thankfully not too rough.")
            if enviro.rooms['cave'].corpses < 2:
                loop=room_cave(1)
            else:
                print("I have died enough times. Finally, time to wake up.")
                win()
