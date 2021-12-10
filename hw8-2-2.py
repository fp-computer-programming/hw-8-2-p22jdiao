# Author: JD 12/09/2021

def sum_odds(li):
    li2 = []
    for x in li:
        if x % 2 != 0:
            li2.append(x)
    total = 0
    for y in li2:
        total += y
    
    return total

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9,
sum_odds([1, 3, 5, 7, 9]) == 25,
sum_odds([2, 4, 6, 8, 10]) == 0)

