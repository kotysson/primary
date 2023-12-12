import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import Counter

class PoSStats:

    def __init__(self, doc):
        self.doc = doc

    def tokenize_and_tag(self):
        tokenized_text = word_tokenize(self.doc)
        tagged_text = pos_tag(tokenized_text)
        return tagged_text

    def display_most_common_pos(self, n):
        pos_list = [element[1] for element in self.tokenize_and_tag()]
        most_freq = Counter(pos_list).most_common(n)
        print("Most frequent parts of speech here are:")
        for i in most_freq:
            print(i[0])

test = PoSStats("This green parrot looks fantastic. I really love its soft feathers and amazingly huge beak").display_most_common_pos(3)