"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    """
    Turns a text file (path param) into a list of words and returns a random word.

    
    """
    
    def __init__(self, path):
        with open(path, 'r') as file:
            self.words = file.read().split('\n')
    
    def random(self):
        return self.words[randint(0, len(self.words) - 1)]

#test = WordFinder('words.txt')

class SpecialWordFinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)
        self.words = self._remove_blanks_and_hashes()

    def _remove_blanks_and_hashes(self):

        new_words = []
        for word in self.words:
            if word[0] == '#' or word == '':
                continue
            else:
                new_words.append(word)
        return new_words