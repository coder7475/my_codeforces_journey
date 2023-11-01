'''
  Title: Beautiful Year
  Author: Robiul Hossain
  Time: 92ms
  input: y
  output: x
'''
# Take the input in string
y = input()
# Convert the taken num to int data type
x = int(y)
# Loop Until find minimum year number that has distinct digits
while True:
  x += 1
  arr = list(str(x))
  s = set(arr)
  if len(s) == len(arr):
    print(x)
    break
