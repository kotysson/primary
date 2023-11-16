# def sq_numbers(n):
#     for i in range(1, n+1):
#         yield i ** 2
#
# a = sq_numbers(3)
# print("Квадраты чисел 1, 2, 3")
# print(next(a))
# print(next(a))
# print(next(a))

def get_words(text, letter):
    words = text.split()
    for word in words:
        if word[0] == letter:
            yield word

def main():
    text = "The quick brown fox jumps over lazy dog."
    letter = "b"
    words = get_words(text, letter)
    for word in words:
        print(word)

if __name__ == "__main__":
    main()