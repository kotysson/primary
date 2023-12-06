class WordTokenizer:
    class_type = "tokenizer"
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        return self.text.lower().split()

    @classmethod
    def sentence_tokenizer(cls, text):
        return text.lower().split('. ')

    @staticmethod
    def describe():
        print('This is a tokenizer.')

tokenizer = WordTokenizer('This is a sample text')
tokenizer.describe()

sentences = WordTokenizer.sentence_tokenizer('This is a sample text. This is another sentence')
print(sentences)