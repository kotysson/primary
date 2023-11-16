text = "My friend Genry went to the shop. He bought some apples and a little bit of Dragon Caramels. Apples were tasty."

def tokenization(input_text):
    '''
    функция принимает на вход указанный текст, разбивает его на слова, приводя их к нижнему регистру
    :return: токенизированный текст
    '''
    token = input_text.lower().split()
    return token

tokenized_text = tokenization(text)
print(tokenized_text)

stop_words = ["the", "a", "some", "of"]
def filter_stop_words(tokenized_text, stop_words):
    clean_list = [token for token in tokenized_text if token not in stop_words]
    return clean_list

clean_list = filter_stop_words(tokenized_text, stop_words)
print(clean_list)

def freq_func(input_text_2, stop_words):
    token = tokenization(input_text_2)
    filtered_token = filter_stop_words(token, stop_words)
    freq_dict = {}
    for token in filtered_token:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1

    return freq_dict

frequency = freq_func(text, stop_words)
print(frequency)

print(frequency['apples'])

def tokenizator(text):
    """

    :text: текст для токенизации (str)

    """
    words = text.lower().split()
    return words


tokenized_text = tokenizator('This is a sample sentence')
print(tokenized_text)   # ['this', 'is', 'a', 'sample', 'sentence']

# def clean_text(text):
#     """
#
#     :text: текст для удаления стоп-слов (str)
#
#     """
#     # задаем список стоп-слов
#     stopwords = ["the", "a", "and"]
#     return [word for word in text if word.lower() not in stopwords]
#
#
# print(clean_text(tokenized_text))   # ['this', 'is', 'sample', 'sentence']
#
# def count_word_frequencies(text):
#     words = clean_text(tokenizator(text))
#     freq_dict = dict((word, words.count(word)) for word in words)
#     return freq_dict
#
# print(count_word_frequencies('This is a sample sentence. This is a sample phrase.'))
# # {'this': 2, 'is': 2, 'sample': 2, 'sentence.': 1, 'phrase.': 1}
#
# def count_word_frequencies_alt(text):
#     words = clean_text(tokenizator(text))
#     word_frequencies = {}
#     for word in words:
#         if word in word_frequencies:
#             word_frequencies[word] += 1
#         else:
#             word_frequencies[word] = 1
#     return word_frequencies
#
#
# print(count_word_frequencies_alt('This is a sample sentence. This is a sample phrase.'))
# # {'this': 2, 'is': 2, 'sample': 2, 'sentence.': 1, 'phrase.': 1}