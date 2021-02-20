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
        if self.energy <= 0:
            print("Oh my god! I feel faint. I think I might be ...")
            print("DEAD!")



print("---------------------------------------------------------")
print("Welcome to Try and Die - A Text Game of Possible Death")        
print("A weird sensation struck me once I gained awareness. I look around and I see that I am in a dark cave lit up by mushrooms.")
print("'What the hell? Is this a dream?' I asked myself.")
    

if __name__ == '__main__':
    shen = Person('Shen',10)
    print('Current energy: ', shen.energy)
    shen.energy -= 10
    
    loop = 1
    while True:
        # first input loop
        while loop == 1:
            if loop==1:
                input_one = input("What the heck am I gonna do? ")
            else:
                print("---------------------------------------------------------")
                
            if input_one.lower() in ['shout', 'yell']:
                print("I yelled in fear and confusion! The echoes came back. There was no other response.")
                print("Wow, that was quite the waste of energy, I thought.")
            elif input_one.lower() in ['eat mushroom']:
                print("I ate the mushroom and I instantly started shrinking.")
                print("Now that I am the size of a mouse, I can see that in front of me there is a small tunnel.")
                print("It is possibly made by a small rodent.")
                loop=2
            else:
                print("---------------------------------------------------------")
                
        while loop == 2:
            if loop==2:
                print("Well, this is pretty tight but I think I can squeeze in.")
                input_two = input("Should I climb in? ")