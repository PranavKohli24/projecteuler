a=2**1000
s=0
while a:
    s+=a%10
    a=a//10
    
print(s)
