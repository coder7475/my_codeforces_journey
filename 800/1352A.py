t = int(input())

for i in range(t):
  n = int(input())
  ans = []
  power = 1

  while n > 0:
    dividend = n % 10
    if (dividend > 0):
      ans.insert(0, dividend * power)
    n //= 10
    power *= 10

  print(len(ans))
  print(*ans)