# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:53:23 2020

@author: muler

Next, implement the function getGuessedWord that takes in two parameters - 
a string, secretWord, and a list of letters, lettersGuessed. 
This function returns a string that is comprised of letters and underscores, 
based on what letters in lettersGuessed are in secretWord. This shouldn't be 
too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""

# Example parameters
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    #create a list to put the guessed letters 
    Guessed_letters_list = []
    
    for char in secretWord:
        if char in lettersGuessed:
            #if the character is present att
            Guessed_letters_list.append(char)
        else:
            Guessed_letters_list.append('_')
            
    return ''.join(Guessed_letters_list)
            
print(getGuessedWord(secretWord, lettersGuessed))


















            
            