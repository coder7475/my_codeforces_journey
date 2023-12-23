string = input()[1:-1].split(", ")
l = []
for c in string:
	if c != "":
		l.append(c)

print(len(set(l)))
