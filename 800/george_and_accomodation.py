n = int(input())

count = 0

for i in range(n):
  s = input().split()
  p = int(s[0])
  q = int(s[1])
  diff = abs(p - q)
  if (diff > 1):
    count += 1

print(count)