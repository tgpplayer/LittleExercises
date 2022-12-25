# This program returns the fisrt character no repeated of a String given. If there is no character no repeated, returns '_'

word = input("Write a word -> ")

def first_char_no_repeated(word):
    for i in word:
        c = 0
        for j in word:
            if j == i:
                c += 1
        if c == 1:
            return i
    return "_"

if first_char_no_repeated(word) != "_":
    print("The fisrt character no repeated is '" + first_char_no_repeated(word) + "'")
else:
    print(first_char_no_repeated(word))