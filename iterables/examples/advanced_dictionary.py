
letters  = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
defaults = [0 for i in range(len(letters))]

d = dict.fromkeys(
    letters, 
    defaults
)

# or
d = {}
for letter in letters: 
    d.setdefault(letter, 0)

animals = {"cats": 2, "dogs": 10, "hippo": 0}
food    = {"salad": 2, "tomato": 1, "cheese": 2}
combine = animals.copy()
combine.update(food)
print(combine)

res = combine.pop("cats")
print(combine)
print(res)
