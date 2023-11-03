t = int(input())

for i in range(t):
  ints = input().split()
  x, y, k = int(ints[0]), int(ints[1]), int(ints[2])
  if (y <= x):
    print(x)
  else:
    if y - x <= k:
      print(y)
    else:
      print(y+(y-(x+k)))