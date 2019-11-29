
def myst3(a): 
	s  = ''
	for r in a: 
		for c in r: 
			s += chr(ord('A') + c)
	return s

z = ((2, 0, 11, 8, 5), (14, 17, 13, 8, 0))
print(myst3(z))
