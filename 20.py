import math
a=math.factorial(100)

s=0
while a:
    s+=a%10
    a=a//10
    
print(s)
    