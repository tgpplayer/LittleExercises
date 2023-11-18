txt = "Hello hello, welcome!"

def count_words_of_text(txt):
    text = txt.split(" ")

    to_suprime = ".:,;'()[]{¿?}¡!-_"

    # First we suprime all the punctuation marks that could be next to the words
    for i in range(len(text)):
        for j in to_suprime:
            if j in text[i]:
                text[i] = text[i].replace(j, "")
        text[i] = text[i].lower()
                
    
    # Once we have the text formatted, we procceed to count the words

        
                
    print(text)

count_words_of_text(txt)