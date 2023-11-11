n = int(input())
count = 1

curr = ""
for t in range(n):
  magnet = input()
  if t == 0:
    curr = magnet
  else:
    if magnet != curr:
      count += 1
    curr = magnet
  
print(count)