import math

nums = input().split()

n = int(nums[0])
m = int(nums[1])
a = int(nums[2])

tiles = math.ceil(n/a) * math.ceil(m/a)

print(tiles)