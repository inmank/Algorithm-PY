'''
Created on May 11, 2014

@author: karthik
'''
x = 123456789987654321
y = 987654321123456789

def grade3multiply(x, y):
    return x*y

def karatmultiply(x, y):
    if (x > 10 or y > 10):
        return x*y
    else:
        size = max(len(x), len(y))/2

        a = x/size
        b = x%size
        c = y/size
        d = y%size
        
        z0 = karatmultiply(a, c)
        z1 = karatmultiply(b, d)
        z2 = karatmultiply((a+b), (c+d)) - z1 - z0
        
        return (z0*(10**(2*size)) + z2*(10**size) + z1)
    
print karatmultiply(x, y)
#print grade3multiply(x, y)    
    