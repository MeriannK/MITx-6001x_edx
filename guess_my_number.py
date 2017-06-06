# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:00:42 2017

@author: Marianna Kovalova

Guess my number between 0 and 100
"""

print("Please think of a number between 0 and 100!")
low = 0
high = 100
user_ans = ''
while True:
    guess = int((low+high)/2)
    print("Is your secret number", end =" ")
    print(guess, "?")
    print("Enter 'h' to indicate the guess is too high.", end = " ")
    user_ans = input("Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_ans == 'h':
        high = guess
    elif user_ans == 'l':
        low = guess
    elif user_ans == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:", guess)