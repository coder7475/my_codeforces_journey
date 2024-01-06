t = int(input())

for i in range(t):
  a, b = map(int, input().split())

  if ((a+b) % 2 == 1):
    print("Alice")
  else:
    print("Bob")
