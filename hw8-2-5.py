# Author: JD 12/09/2021

def weird_sum(li):
    li2 = []
    for x in li:
        if x % 2 != 0:
            li2.append(x)
        
    if li2 != []:
        li.remove(li2[0])
    total = 0
    for y in li:
        total += y
        
    return total

print(weird_sum([2, 4, 6, 8, 9]) == 20,
weird_sum([13, 12, 10]) == 22,
weird_sum([14, 16, 32]) == 62)

