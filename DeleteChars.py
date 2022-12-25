# Program that recieves 2 arguments as Strings (words) and returns a first word without characters of the second 
# word and a second word without characters of the first word

word_1 = input("Write a first word -> ")
word_2 = input("Write a second word -> ")

def delete_chars(w_1, w_2):
    l_word_1 = [*w_1]
    l_word_2 = [*w_2]

    chars_to_delete = []
    
    # First, we have to detect the common characters, and save them in a list
    for i in l_word_1:
        for j in l_word_2:
            if i == j:
                chars_to_delete.append(i)

    
    # As we just have saved characters that are repeated in the same list, let's format the list for them to
    # not repeat
    for i in chars_to_delete:
        c = 0
        for j in chars_to_delete:
            if i == j:

                # With the following if else statement, we are telling the program to detect if a character has 
                # appeared more than once. In that case, we have to delete that character for the later character 
                # errasement of both words given
                if c == 1:
                    chars_to_delete.remove(i)
                else:
                    c += 1

    # Once we have the wanted characters, we procceed to errase the characters to have two words completely unique
    for i in l_word_1:
        for j in chars_to_delete:
            if i == j:
                l_word_1.remove(i)
    
    for i in l_word_2:
        for j in chars_to_delete:
            if i == j:
                l_word_2.remove(i)

    w1 = w2 = ""

    for i in l_word_1:
        w1 += i
    for i in l_word_2:
        w2 += i

    return w1, w2

print("\nNew first word: " + delete_chars(word_1, word_2)[0] + "; New second word: " + delete_chars(word_1, word_2)[1])