s = input()
m = 'hello'

j = 0

for c in s:
  if j < 5 and c == m[j]: 
    j+=1
  
if j == 5:
  print("YES")
else:
  print("NO")
