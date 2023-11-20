n = int(input())

for x in range(n):
  m = int(input())

  if (m - 1) % 3 == 0 or (m + 1) % 3 == 0:
    print("First")
  else:
    print("Second")