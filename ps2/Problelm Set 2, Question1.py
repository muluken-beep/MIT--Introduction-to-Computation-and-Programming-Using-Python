# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:39:16 2020

@author: muler
"""

# -*- coding: utf-8 -*-
"""    
First, implement the function is_word_guessed that takes in two parameters a
string, secret_word , and a list of letters (strings), letters_guessed. This function
returns a boolean True
if secret_word has been guessed (i.e., all the letters of
secret_word are in letters_guessed ), and False otherwise. This function will be
useful in helping you decide when the hangman game has been successfully
completed, and becomes an endtest
for any iterative loop that checks letters against
the secret word.

For this function, you may assume that all the letters in secret_word and
letters_guessed are lowercase.
"""
# Example Usage:
secretWord = 'apple' 
lettersGuessed = ['e', 'c', 'p', 'k', 'l', 'f']

# def is_word_guessed(secret_word, letters_guessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: boolean, True if all the letters of secretWord are in lettersGuessed;
#       False otherwise
#     '''
#     for char in secret_word:
#         if char in letters_guessed:
#                 return True
              
#         else:
#                 return False
                
# print(is_word_guessed(secretWord, lettersGuessed))


#another way to implement this is using the remove function

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''    
#create a list from the secret word 
    secretWord_list = list(secretWord)

# # Iterate through each letter from lettersguessed
    for letter in letters_guessed:
        #Check if the letter is there...
        if letter in secretWord_list:
            #While it remains in there(i.e has multiple instances of the same letter), keep removing it until it is done
            while letter in secretWord_list:
                secretWord_list.remove(letter)
    #Return True if all letters are removed, otherwise false 
    return secretWord_list ==[]

print(is_word_guessed(secretWord, lettersGuessed))
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

