import OOPNER
from collections import Counter

class NERStats:

    def __init__(self, doc):
        self.doc = doc
        self.NerExtractor = OOPNER.NERExtractor()

    def analyze_entities(self):
        extracted_entities = self.NerExtractor.extract_named_entities(self.doc)
        freq_dict = Counter(extracted_entities)
        return freq_dict

    def display_most_common_entities(self, n):
        most_freq = self.analyze_entities().most_common(n)
        print("Most frequent entitites are:")
        for ent in most_freq:
            string = ', '.join(ent[0])
            print(string)

test = NERStats('Huawei Inc. is a technology company. Amazon not so much. Though Apple Inc. is losing now. But I believe in Apple Inc. force').display_most_common_entities(2)


# option 2 without from collections import Counter
#     def analyze_entities(self):
#         extracted_entities = self.NerExtractor.extract_named_entities(self.doc)
#         freq_dict = dict()
#         for element in extracted_entities:
#             if element in freq_dict:
#                 freq_dict[element] += 1
#             else:
#                 freq_dict[element] = 1
#         return freq_dict
#
#     def display_most_common_entities(self, n):
#         freq_dict = self.analyze_entities()
#         most_freq = sorted(freq_dict.items(), reverse = True, key=lambda item: item[1])
#         index = 0
#         print('The most frequent entities here are:')
#         while index < n:
#             print(f'{most_freq[index][0]}')
#             index += 1
