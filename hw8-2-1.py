# Author: JD 12/09/2021

def count_odds(li):
    counter = 0
    for x in li:
        if int(x) % 2 != 0:
            counter += 1
    
    return counter

li = input("The list of number: ")

li = li.split(",")

count = count_odds(li)
print(count)

print(count_odds([1, 2, 3, 4, 5, 6]) == 3,
count_odds([1, 3, 5, 7, 9]) == 5,
count_odds([2, 4, 6, 8, 10]) == 0)