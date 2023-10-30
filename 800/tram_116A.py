n = int(input())

p = 0
m = 0

for i in range(n):
  a, b = map(int, input().split())
  p = p - a + b
  m = max(p, m)

print(m)