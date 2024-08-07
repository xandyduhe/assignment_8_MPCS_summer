# Week 7
# Problem 2

import re
import itertools
from itertools import permutations
import os
from words import points_for_letter

def open_scrabble_words(file):
    ''' Opens file containing scrabble words and crates list of words'''
    try: 
        with open(file, 'r') as file:
            words = []
            # write each line as an index in a llist 
            for line in file:
                line = line.strip().lower()
                words.append(line)
        return(words)
    except:
        print("Could not open file")
        return False

class Word:   
    """Attributes:    
            - characters: str of letter charecters 
            - length: int represening length of charecters string 
            - score: int representing score of letters in charecters 
        """   
    def __init__(self, character):
        self.character = character
        self.length = len(character)
        self.score = self.calculate_score()

    def calculate_score(self):
        ''' Calculate score per word based on letters in tile_score dictionary'''

        # scores for each letter charecter 
        tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
            "x": 8, "z": 10}
        score = 0

        try:
            # calculates total score of charecters  
            for letter in self.character:
                score += tile_score[letter]
            return score 
        
        except:
            print('Could not produce word score')
            return False
  

class InputValidator:
    ''' Attributes:
        - letters: input string of 7 letters with spaces and ","
        '''

    def validate_tiles(self, letters):
        ''' Takes 7 letters and makes a list with each leters as a sparate index '''
        
        # checks for non-letter charecters 
        for i in letters:
            if re.fullmatch(r'[^a-z]', i):
                print(f'Entry {i} is not a letter.')
                # there is a non-letter charecter
                return False
            
        # checks length == 7
        if len(letters) != 7:
            print(f'{len(letters)} is not 7. Enter 7 characters.')
            return False
        return True
    
    def validate_entry(self):
        ''' Take user tile entry of 7 letters '''

        letters = input('Please enter your 7 tiles: ').lower()
        # remove spaces and commas charecters 
        if ' ' in letters:
            letters = letters.replace(" ", "")
        elif ',' in letters:
            letters = letters.replace(',', '')
        else: 
            letters = letters 

        # if tiles could not be validated by validate_tiles() 
        if not self.validate_tiles(letters):
            print("Invalid input.\n")
            return self.validate_entry()

        return letters
    
class WordGenerator:
    '''
    Attributes:
    - scrabble words: list of str contiaining valid scrabble words 
    - tiles: str of 7 letter charecters represening scrabble tiles
    '''
    def __init__(self, scrabble_words):
        self.scrabble_words = scrabble_words

    def tile_combinations(self, tiles):
        '''finds possible scrabble words from entered tiles 
        '''
        # empty list of valid words from tiles  
        possible_words = []
        try:
            # generate list of possible scrabble words from tiles 
            for length in range(1, len(tiles) + 1): # word from 2 to 8 letters 
                for perm in permutations(tiles, length):
                    word = ''.join(perm)

                    if word in self.scrabble_words:
                        possible_words.append(word)
            return possible_words
        except:
            print('Could not find possible combinations')
            return False 

def main():

    # load scrabble words 
    s_words = (open_scrabble_words(f'{os.getcwd()}\\scrabble_list.txt'))
    if not s_words:
        return
    
    # validate tile entry 
    tiles = InputValidator().validate_entry()

    # generate possible words that can be formed from tiles 
    # based on scrabble words text file
    tile_word_combinations = WordGenerator(s_words).tile_combinations(tiles)
    
    if not tile_word_combinations:
        print('No combinations were found')
        return

    # empty dictionary to store words and scores 
    dict_t ={}
    try:
        # score possible words 
        for word in tile_word_combinations:
            score = Word(word).calculate_score()
            dict_t.update({word:score})

        # sort possible words by score 
        combination_scores = sorted(dict_t.items(), key=lambda item: (item[1]))
    except: 
        print('Could not produce combination scores')

    # print scores 
    max_langth = len(combination_scores[-1][0]) # longest word 
    min_length = len(combination_scores[0][0]) # shortest word 
    for i in range(min_length, max_langth + 1):
        print(f'\n\n{i} Letter Words \n----------')
        for n in combination_scores:
            if len(n[0]) == i: 
                print(f'{n[0]} - {n[1]} points')


if __name__ == '__main__':
    main()

