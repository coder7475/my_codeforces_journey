n = int(input())
x, y = [], []
for i in range(n):
  h, a = map(int, input().split())
  x.append(h)
  y.append(a)

c = 0
for m in x:
    c += y.count(m)

print(c)