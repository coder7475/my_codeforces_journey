s1 = input()
s2 = input()
t = input()

s = s1 + s2

tx = ''.join(sorted(t))
sx = ''.join(sorted(s))

print("YES") if tx == sx else print("NO")
