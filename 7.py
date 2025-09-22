import math
# print(math.sqrt(9))
def isprime(num):
    m=int(math.sqrt(num))
    for i in range(2,m+1):
        # print(i)
        if num%i==0:
            # print('vo',i)
            return False
            
    return True
    



num=2
i=0
while i<10001:
    if isprime(num):
        i+=1
        # print('hello',num)
        
    num+=1
    
print(num-1)





