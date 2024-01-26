"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finds a word"""

    def __init__(self, file_path):
        """Creates a new WordFinder object"""

        self.words = list()
        self.word_count = 0

        self.file = open(file_path, "r")
        self.get_words(file_path)
        self.file.close()

        print(f"{self.word_count} words read")

    def get_words(self, file_path):
        """Counts how many words are in a file"""

        for line in self.file:
            self.words.append(line.strip())
            self.word_count = len(self.words)

    def random(self):
        """Returns random word from list"""

        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Finds a special word"""

    def get_words(self, file_path):
        """Returns all non-category words and non-blank lines"""
        
        for line in self.file:
            if line.strip() and not line.startswith("#"):
                self.words.append(line.strip())
                self.word_count = len(self.words)