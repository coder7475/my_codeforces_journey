n = int(input())
s = input()

mid = n // 2
a = 0
d = 0
for c in s:
  if c == 'A':
    a += 1
  else:
    d += 1

if a > mid:
  print('Anton')
elif d > mid:
  print("Danik")
else:
  print("Friendship")