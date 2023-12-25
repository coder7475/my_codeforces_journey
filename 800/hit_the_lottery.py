n = int(input())
c, a = 0, [100, 20, 10, 5, 1]

for x in a:
  c += n // x
  n %= x

print(c)

