n = int(input())
arr = list(map(int, input().split()))

even_count, even_index, odd_count, odd_index = 0, 0, 0, 0
for i in range(n):
  if arr[i] % 2 == 0:
    even_count += 1
    even_index = i
  else:
    odd_count += 1
    odd_index = i
  
if even_count > odd_count:
  print(odd_index+1)
else:
  print(even_index+1)
    