n = int(input())

x = 0
y = 0
z = 0

for i in range(n):
  arr = input().split()
  x += int(arr[0])
  y += int(arr[1])
  z += int(arr[2])

if x == 0 and y == 0 and z == 0:
  print("YES")
else:
  print("NO")