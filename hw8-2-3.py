# Author: JD 12/09/2021

def three_letter_words(li):
    counter = 0
    for x in li:
        if len(x) == 3:
            counter += 1
    
    return counter

print(three_letter_words(["cat", "bat", "apple"]) == 2,
three_letter_words(["apple", "hippo", "mouse"]) == 0,
three_letter_words(["hop", "pop", "bop"]) == 3)

