n, m = map(int, input().split())
c = 1

for i in range(n):
  b = True
  
  for j in range(m):
    if i % 2 == 0:
      print("#", end="")
    else:
      if (c % 2 == 1 and j == m - 1 and b):
        print("#", end="")
        c += 1
        b = False
      elif (c % 2 == 0 and j == 0 and b):
        print("#", end="")
        c += 1
        b = False
      else:
        print(".", end="")

  print()