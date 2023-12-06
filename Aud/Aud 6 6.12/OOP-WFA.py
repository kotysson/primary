from collections import Counter

class WordFrequencyAnalyzer:

    def __init__(self, text):
        self.text = text
        self.word_frequencies = self._analyze_word_frequencies()

    def _tokenize(self):
        return self.text.lower().split()

    def _analyze_word_frequencies(self):
        words = self._tokenize()
        word_frequencies = Counter(words)
        return word_frequencies

    # _tokenize and _analyze_word_frequencies - скрытые, те инкапсулируемые методы
    # программисты их не видят
    # если ввести класс., пайчарм не подскажет наличие этих методов
    # потому что они нужны только для работы метода display_most_common_words
    # такие скрытые методы мы обозначаем нижним подчеркиванием в начале: _tokenize

    def display_most_common_words(self, n=10):
        most_common_words = self.word_frequencies.most_common(n)
        print(f'Top {n} most common words:')
        for word, frequency in most_common_words:
            print(f'{word}: {frequency}')


text_analyzer = WordFrequencyAnalyzer(
    "Humpty Dumpty sat on a wall.\
    Humpty Dumpty had a great fall. \
    All the king’s horses and all the king’s men \
    couldn’t put Humpty together again."
    )
text_analyzer.display_most_common_words(2)

# output
# Top 2 most common words:
# humpty: 3
# dumpty: 2






