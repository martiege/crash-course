
def myst(val1, val2):
    if (val1 and val2):
        return 1 
    elif (val1 and not val2): 
        return 2
    elif (not val1 and val2): 
        return 3 
    else: 
        return 4

print(myst(((True and False) or (False and True)), ((False or True) and (not(not True)))))
