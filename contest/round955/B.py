t = int(input())

for i in range(t):
  x, y, k = list(map(int, input().split()))

  while (k):
    x += 1
    while ( x % y == 0):
        x = x // y
    k -= 1
  
  print(x)
