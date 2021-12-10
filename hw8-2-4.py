# Author: JD 12/09/2021

def letter_filter(word,letter):
    counter = 0
    for x in word:
        if x == letter:
            counter += 1
    
    return counter

print(letter_filter("cat", "t") == 1,
letter_filter("apple", "p") == 2,
letter_filter("supercalifragilisticexpialidocious", "i") == 7)
