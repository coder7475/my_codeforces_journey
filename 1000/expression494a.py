a = int(input())
b = int(input())
c = int(input())

output = max( 0, a+b+c )
output = max(output, a+b*c )
output = max(output, a*(b+c))
output = max(output, a*b*c)
output = max(output, (a+b)*c)

print(output)