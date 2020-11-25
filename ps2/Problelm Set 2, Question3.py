# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:29:34 2020

@author: muler

Next, implement the function get_available_letters that takes in one parameter a
list of letters, letters_guessed . This function returns a string that is comprised of
lowercase English letters all
lowercase English letters that are not in
letters_guessed .
This function should return the letters in alphabetical order. For this function, you may
assume that all the letters in letters_guessed are lowercase.
Hint : You might consider using string.ascii_lowercase , which is a string comprised
of all lowercase letters:
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
"""
#Example usage

letters_guessed = ['e', 'i', 'k', 'p', 'm', 'r', 's', 'k', 'b', 'm']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
   # put the list of a-z small letters in a list
    all_letters ='abcdefghijklmnopqrstuvwxyz'
    all_letters_list = list(all_letters)
    
   #for the leetrs in the in the letters guessed list
    for letter in lettersGuessed:
        #if the letter is in the list of all small letters, remove it 
        if letter in all_letters_list:
            all_letters_list.remove(letter)
       #return the string which contains concatenated letters not in the guessed list
    return str(''.join(all_letters_list))
       

print(getAvailableLetters(letters_guessed))






    
   
