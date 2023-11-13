nums = input().split()
n = int(nums[0])
k = int(nums[1])

if k <= (n+1)//2:
  print((k*2) - 1)
else:
  print(((k - (n + 1) // 2) * 2))