text1 = "A big red parrot ate an unusually green apple and then the bird's feathers suddenly turned to green"
text2 = "The unusual apple later turned up again. This time it was eaten by a kitten, who was surprised to find itself \
green as well as the parrot"

def tokenization(text):
    tokens = text.lower().split()
    return tokens

tokens1 = tokenization(text1)

tokens2 = tokenization(text2)

def Jakkard(token1, token2):
    token_set1 = set(token1)
    token_set2 = set(token2)
    intersection_result = token_set1.intersection(token_set2)
    union = len(token_set1) + len(token_set2) - len(intersection_result)
    similarity = len(intersection_result) / union
    return round(similarity, 2)

tokenized1 = tokenization(text1)
tokenized2 = tokenization(text2)
Jakkard_result = Jakkard(tokenized1, tokenized2)
print(Jakkard_result)

