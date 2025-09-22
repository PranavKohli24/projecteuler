def lcm(a,b):
    s=min(a,b)
    for i in range(2,s+1):
        if a%i==0 and b%i==0:
            hcf=i
            
    lc=(a*b)/hcf
    
    return lc



s=1
s*=19
s*=5040
s*=17
s*=13
s*=11


# print(s)
# print(lcm(5040,12))
print(s)


