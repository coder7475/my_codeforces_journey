a, b = map(int, input().split())
years = 0

while a <= b:
  years += 1
  a *= 3
  b *= 2

print(years)