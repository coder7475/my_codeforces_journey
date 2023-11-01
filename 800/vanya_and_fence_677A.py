n, h = input().split()
arr = input().split()
extra = 0
for i in arr:
  if int(i) > int(h):
    extra += 1

print(int(n) + extra)