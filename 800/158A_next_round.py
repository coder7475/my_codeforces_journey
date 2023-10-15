""" 
  ! TODO: number of participents who advanced
  --------------------------------------------
  n: int
  number of participants
  k: int
  the k-th place on standings
  a: array
  the standings after contest from 1 to n
"""
n, k = map(int, input().split())
a = input().split()

passed_score = int(a[k-1])
# print(type(passed_score))
count = 0
for i in reversed(range(len(a))):
  score = int(a[i])
  if score > 0 and score >= passed_score:
    count += 1

print(count)
