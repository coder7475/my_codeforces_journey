t = int(input())

def get_digits(num):
  nums = []
  for n in str(num):
    nums.append(int(n))

  return nums

# print(get_digits(333))

for i in range(t):
  x, k = map(int, input().split())

  while True:
    digits = get_digits(x)
    summ = sum(digits)
    if summ % k == 0:
      print(x)
      break
    else:
      x += 1