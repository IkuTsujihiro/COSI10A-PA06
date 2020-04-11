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
            word = line[:-1]
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
   return result


def correct_guesses(word, guessed_letters):
   correct_letters = 0
   for letter in word:
      if letter in guessed_letters:
         correct_letters += 1
   return correct_letters


def play_hangman():
   """ this is the python script version of the game """
   want_to_play = True
   print("Welcome to the hangman game!")
   while (want_to_play):
      guessed_letters = []
      guesses_left = 6
      print("\nStarting new game...\n")
      print("You have", guesses_left, "guesses.")
      word = generate_random_word()
      letter = input("Guess a letter! ")
      done = False
      while not done:
         if letter in guessed_letters:
               ##"subtract one from guesses_left"
               guesses_left = guesses_left - 1
               ##"and tell them they already guessed that letter"
               print("This letter has already been guessed.")
               
         elif letter not in word:
               ##"add letter to guessed letters"
               guessed_letters.append(letter)
               ##"tell user the letter is not in the word"
               print("That letter is not in the word.")
               ##"subtract one from the guesses_left"
               guesses_left = guesses_left - 1
         else:
               ##"add letter to guessed letters"
               guessed_letters.append(letter)
               ##"tell user the letter is in the word"
               print("The letter is in the word.")
         
         if correct_guesses(word, guessed_letters) == len(word):
               done = True
               print("You have correctly guessed the word. Congrats!")
               print("The word is:", word)
               ##"all the letters in the word have been guessed":
               ##"set done to be true and tell the user they won!"
         
         ##" elif the number of guesses left is zero"
         elif guesses_left == 0:
               ##"set done to be true and tell the user they lost!"
               done = True
               print("You have no more guesses, you have lost the game!")
               print("The word was:", word)
         else:
               print(print_word(word,guessed_letters))
               print("You have", guesses_left, "guesses.")
               letter = input("Please guess another letter. ")
      answer = input("Would you like to play again? (y/n) ")
      if answer == 'y':
         want_to_play = True
      else:
         want_to_play = False
         print("Thank you for playing!")



if __name__ == '__main__':
    play_hangman()
