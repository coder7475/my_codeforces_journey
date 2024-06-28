t = int(input())

for x in range(t):
  cor_1 = list(map(int, input().split()))
  cor_2 = list(map(int, input().split()))
  bol_1 = cor_1[0] > cor_1[1]
  bol_2 = cor_2[0] > cor_2[1]
  
  if (bol_1 == bol_2):
    print("YES")
  else:
    print("NO")

