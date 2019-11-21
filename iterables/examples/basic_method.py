
l = []
print(l)
l.append(12)
print(l)
l.insert(0, "hei")
print(l)
l.append("hei")
print(l)
l.remove("hei")
print(l)
l.pop(0)
print(l)
l = [1, 2, 1, 1, 1, 1, 2]
print(l)
print(l.count(1))
l.reverse()
print(l)
l.sort()
print(l)

# convert other other iterables to list
l = list(range(2, 10, 3))