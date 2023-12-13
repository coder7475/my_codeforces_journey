t = int(input())

for i in range(t):
  n = int(input())
  s = input()
  num0 = s.count("0")
  num1 = s.count("1")

  if num0 > num1 or num0 > 0:
    print("YES")
  else:
    print("NO")

