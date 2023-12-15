a = list(map(int, input().split()))
l = set(a)
diff = 4 - len(l)

if diff > 0:
  print(diff)
else:
  print(0)