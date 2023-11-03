n = input()

luckys = [4, 7, 47, 77, 74, 44, 444,447,474, 477, 777, 774, 744]
flag = False
for i in luckys:
  if int(n) % i == 0:
    flag = True
    break

if flag:
  print("YES")
else:
  print("NO")