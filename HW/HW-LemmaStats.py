import spacy
from collections import Counter

class LemmaStats:

    def __init__(self, doc):
        self.doc = doc
        self.spacy = spacy.load("en_core_web_sm")

    def lemmatize(self):
        text = self.spacy(self.doc)
        # вводим условие, чтобы исключить лемматизацию и вывод знаков препинания
        lemmatized_text = [token.lemma_ for token in text if token.text != '.']
        freq_dict = Counter(lemmatized_text)
        return freq_dict

    def display_most_common_lemmas(self, n):
        most_freq_lemmas = self.lemmatize().most_common(n)
        print("Most frequent lemmas here are:")
        for lemma in most_freq_lemmas:
            print(f'{lemma[0]}')

a = LemmaStats("Kate went to the shop and bought fruits. Then she went to school. After school she went for lunch").display_most_common_lemmas(3)


