"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

import random
import os

def generate_random_word():
   """ read a list of words from a file and pick a random one to return """
   curr_dir = os.path.dirname(os.path.abspath(__file__))
   word_list_path = os.path.join(curr_dir, 'usa.txt')
   with open(word_list_path,'r') as word_list: 
      rand_num = random.randint(0, 61336 - 1)

      count = 0
      word = ""
      for line in word_list:
         if count == rand_num:
            word = line
            break
         count += 1

   return word

def print_word(word, guessed_letters):
   """ given a word and a list of guessed letters, print - for every letter that hasn't been guessed in word """
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += '-'
    print(result)

def play_hangman():
   """ this is the python script version of the game """
   print("The hangman app is under construction. Try again later!")

if __name__ == '__main__':
    play_hangman()

#This is a test
print(generate_random_word())