
def yatzy(t1, t2, t3, t4, t5):
    l = [t1, t2, t3, t4, t5]
    for i in range(len(l)): 
        for j in range(len(l) - i - 1):
            if l[j] > 6 or l[j + 1] > 6: 
                return "Ikke bruk input stoerre enn 6!"
            if l[j] < 1 or l[j + 1] < 1: 
                return "Ikke bruk input mindre enn 1!"

            if l[j] > l[j + 1]: 
                l[j], l[j + 1] = l[j + 1], l[j]
    return l 

def maxi_yatzy(lst):
    n = len(lst)
    most_val = None
    most_num = 0

    for base_dice in range(1, 6 + 1):
        num = 0
        for dice in lst: 
            if dice == base_dice: 
                num += 1 
        if num >= most_num: 
            most_val = base_dice 
            most_num = num 
    return "Du kastet " + str(n) + " terninger og fikk flest " + str(most_val)  + " (" + str(most_num) + " like)."

print(maxi_yatzy([1, 2, 5, 4, 4, 5]))