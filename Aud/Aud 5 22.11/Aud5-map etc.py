# map function
test = list(map(lambda x: x*10, range(10)))
print(test)

# # task 1
word_length_list = list(map(lambda x: len(x), ['sofa', 'desk', 'table', 'chair']))
print(word_length_list)

# #task 2
sentence_length_list = list(map(lambda x: len(x.split()), ['Twenty first century', 'Place and time', "crazy monk did it"]))
print(sentence_length_list)

# #task 3
import spacy
nlp = spacy.load("en_core_web_sm")
text = "He flew up to the skies and felt extremely happy to have left his planet"
tokenized_text = nlp(text)
#
lemmatization = list(map(lambda x: x.lemma_ , tokenized_text))
print(lemmatization)

# filter function accepts True/False conditions
people = [('John', 22), ('Eva', 20), ('Mark', 23)]
adults = list(filter(lambda x: x[1] >=21, people))
print(adults)

# task 1
wordlist = ['high', 'medium', 'superlong', 'supersuperlong']
correct_length = list(filter(lambda x: len(x) > 6, wordlist))
print(correct_length)

# task 2
# у меня не импортировалась библиотека, поэтому пришлось пошаманить
import nltk
from nltk.tokenize import word_tokenize
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
tokenized = nltk.pos_tag(word_tokenize('he was brave enough to face the danger, but reaching out for the sword, sir Max suddenly \
remembered he was in fact sleeping at home two minutes ago'))
print(tokenized)
noun = list(filter(lambda x: x[1] == 'NN', tokenized))
print(noun)
print('aaa')

# task 3
# начала решать немного другим методом, но моя попытка закончилась ничем
# вывод: решить эту задачку в одну строку мне не по зубам

sentences = ['He was brave enough to face the danger.', 'Though while reaching out for the sword, sir Max suddenly \
realised that in fact he had gone to bed two hours ago.', 'As he remember, the dream went away.']
tagged = list(filter(lambda x: 'VBD' in nltk.pos_tag(word_tokenize(x)), sentences))
print(tagged)

# task 3 aud variant
sentences = ['this is a sample sentence', 'a cute dog', 'wow wow wow']
tagged = [{sent: nltk.pos_tag(word_tokenize(sent))} for sent in sentences]

for element in tagged:
    temp = list(filter(lambda x: x[1] == 'VBZ', list(element.values())[0]))
    #print(temp)
    if len(temp) != 0:
        print(list(element.keys())[0])