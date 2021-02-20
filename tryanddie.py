# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:41:27 2021

@author: sheng
"""
class Person():
    def __init__(self,name,energy):
        self.name = name
        self.energy = energy
        
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
            
    def reset(self):
        print("I suddenly feel strength flowing through my body again.")
        print("*Gasp* I am alive!")
        self._name = 'Shen'
        self._energy = 10
        return self
    
    def fidget(self):
        print("Fidgeting doesn't really help but it's my natural reaction right now.")

class Enviro():
    def __init__(self,deathstate):
        self.deathstate = 0
        self.person = Person('Shen',10)
        
    @property
    def deathstate(self):
        return self._deathstate
    
    @deathstate.setter
    def deathstate(self,val):
        self._deathstate = val
        
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
            self.person = self.person.reset()

if __name__ == '__main__':
    print("---------------------------------------------------------")
    print("Welcome to Try and Die - A Text Game of Possible Death")        
    print("A weird sensation struck me once I gained awareness. I look around and I see that I am in a dark cave lit up by mushrooms.")
    print("'What the hell? Is this a dream?' I asked myself.")

    # shen = Person('Shen',10)
    # print('Current energy: ', shen.energy)
    enviro = Enviro(0)
    
    loop = 1
    while True:
        # first input loop
        while loop == 1:
            if loop==1:
                input_one = input("Whatever it may be, I don't want to stay in this dark any longer than I need to.\n> ")
                
            if input_one.lower() in ['shout', 'yell', 'scream']:
                print("I yelled in fear and confusion! The echoes came back. There was no other response.")
                print("Wow, that was quite the waste of energy, I thought.")                
                enviro.personenergy -=1
            elif input_one.lower() in ['eat mushroom', 'eat', 'mushroom']:
                print("I ate the mushroom and I instantly started shrinking. Also, I feel a bit stronger.")
                enviro.personenergy +=1
                print("Now that I am the size of a mouse, I can see that in front of me there is a small tunnel.")
                print("It is possibly made by a small rodent.")
                loop=2
            else:
                enviro.person.fidget()                
                
        while loop == 2:
            if loop==2:
                print("Well, this is pretty tight but I think I can squeeze in.")
                input_two = input("Should I climb in?\n> ")
                
            if input_two.lower() in ['climb', 'yes']:
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
                input_three = input("Should I go towards the light or eat mushrooms?")
            
            if input_three.lower() in ['eat mushroom', 'eat', 'mushroom']:
                print("Yum! Just kidding. That was really gross but I did it any way.")
                print("I started to grow larger like Alice in Wonderland.")
                print("Time to get out of here!")
                loop=4
            elif input_three.lower() in ['leave', 'outside', 'light']:
                print("I chose to ignore the mushrooms and go directly outside.")
                loop=4
            else:
                enviro.person.fidget()
                
        while loop == 4:
            if loop==4:
                print("Stepping into the light, I quickly realized that I am about to step off of a cliff.")
                print("'Woah!' I exclaim as I hurriedly back up from the edge.")
            