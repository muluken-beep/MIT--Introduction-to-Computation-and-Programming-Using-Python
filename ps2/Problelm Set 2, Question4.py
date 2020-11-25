# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:49:24 2020

@author: muler
"""

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''    
#create a list from the secret word 
    secretWord_list = list(secret_word)

# # Iterate through each letter from lettersguessed
    for letter in letters_guessed:
        #Check if the letter is there...
        if letter in secretWord_list:
            #While it remains in there(i.e has multiple instances of the same letter), keep removing it until it is done
            while letter in secretWord_list:
                secretWord_list.remove(letter)
    #Return True if all letters are removed, otherwise false 
    return secretWord_list ==[]


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
            #if the character guesed is present in the secret word, add it to the list
            Guessed_letters_list.append(char + ' ')
            #otherwise add an underscore for every character that is missing
        else:
            Guessed_letters_list.append('_ ')

  # Concatenate all the items into a string.  
  
    Guessed_letters_list = ''.join(Guessed_letters_list)
    return Guessed_letters_list




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

secret_word = 'happy'

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
   
    #Create the necessary variables 
    numOfGuesses = 6
    lettersGuessed = []
    
    #Introductory text when starting the game 
    print('WELCOME TO THE GAME, HANGMAN!')
    print('I am thinking of a word that is' + str(len(secretWord)) + ' letters long')
    
    while True:
        print('- - - - - - - - - - - - - - - - - - - - - -')
        print('You have' + str(len(secretWord)) + 'guesses left.')
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        playerGuess = input('Please guess a letter: ')
        playerGuess = playerGuess.lower()
        
        
  # if the letter if already guessed by the player, let the player know
        if playerGuess in lettersGuessed:
            print ("oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            
  #if the player is right, let him/her know 
        elif playerGuess in secretWord:
            lettersGuessed.append(playerGuess)
            print ("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
            
 #if the letter is incorrect, decrease the number of guesses by 1 and let the player know 
        else:
             numOfGuesses -=1
             lettersGuessed.append(playerGuess)
             print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
             
   # if the player guessed enough times, end game 
    
    lettersguessed = input('Please guess a letter: ')       
    while  (is_word_guessed(secretWord,lettersguessed) ==False):
        Guess -= 1
        if lettersguessed in secretWord:
            guess_with_spaces = getGuessedWord(secretWord,lettersguessed)
            print('GOOD GUESS:' + guess_with_spaces) 
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - ')  
            
            getAvailableLetters2 =getAvailableLetters(lettersguessed)
            print('AVAILABLE LETTERS: ' + getAvailableLetters2)
            print('YOU HAVE ' + str(Guess) + ' GUESSES LEFT')       
       
            getAvailableLetters2 -=  getAvailableLetters.remove(lettersguessed)
        else:
            print('OOOPS! That letter is not in my word') 
            print('AVAILABLE LETTERS: ' + getAvailableLetters(lettersguessed))
            lettersguessed = input('Please guess a letter: ')
           
         
                 
            
hangman(secret_word)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    