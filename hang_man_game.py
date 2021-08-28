# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 19:43:03 2021

@author: wajee
"""

import random

from hang_man_init import logo
from hang_man_init import stages

from hang_man_wordlist import word_list

def get_word_blanklist():
    
    get_word=random.choice(word_list)
    blank_list=[]
    
    for word_len in range(len(get_word)):
        blank_list.append('__')
    
    return (get_word,blank_list)


def draw_hang_man(user,word,blank,counter):
    
    
    for index,letter in enumerate(word):
        if(user==letter):
            blank[index]=user
            
    if(word.find(user)==-1):
        print(stages[counter])
        counter+=1
    
    
    if(counter==6):
        print("Sorry you did not guess the word correctly")
        print(stages[counter])
        return(counter)
    
    final="".join(blank)
    
    if(word==final):
        print("Congratulations you have guess the word correctly")
        print('The word is ')
        print(word)
        counter=6
        return(counter)
        
    else:
       print(blank)
       return(counter)

def main():
    
    print(logo)
    print("Welcome to Hangman")
    [answer,blank]=get_word_blanklist()
    stages.reverse()
    counter=0
    
    while counter < 6:
        user_input=input("Please select the character:")
        char=user_input.lower()
        counter=draw_hang_man(char, answer, blank, counter)
        
    print("Game over ")


main()

