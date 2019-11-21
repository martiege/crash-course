

def set_first_element(lst, new_value):
    lst[0] = new_value

def copy_set_first_element(lst, new_value):
    new_lst = lst.copy()
    set_first_element(new_lst, new_value)
    return new_lst

def copy_set_first_element2(lst, new_value):
    new_lst = lst.copy()
    new_lst[0] = new_value
    return new_lst

l = [10, 12, 5, 1, 23, 1]
print(l)
set_first_element(l, "hei")
print(l)


