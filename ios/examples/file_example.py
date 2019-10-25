
f = open("test.txt", "r")
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = str(i) + ": " + lines[i]
f.close()

g = open("test_with_lines.txt", "w")
for line in lines:
    g.write(line)
