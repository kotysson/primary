def not_unique_func(text):
    tokenized_text = text.split()
    not_unique_words = set()
    for word in tokenized_text:
        if word in not_unique_words:
            yield word
        else:
            not_unique_words.add(word)

def main():
    text = "The smartest brain in the world in fact turned out to be the stupidest brain in the world"
    dublicate = set(not_unique_func(text))
    for element in dublicate:
        print(element)

if __name__ == "__main__":
    main()