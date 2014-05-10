'''
Created on May 11, 2014

@author: karthik
'''
x = 123456789987654321
y = 987654321123456789

def multiply(x, y):
    if (x > 10 or y > 10):
        return x*y
    else:
        size1 = len(x)
        size2 = len(y)
        
        size = max(size1, size2)
        size = size/2
        
        a = x/size
        b = x%size
        c = y/size
        d = y%size
        
        z0 = multiply(a, c)
        z1 = multiply(b, d)
        z2 = multiply((a+b), (c+d)) - z1 - z0
        
        return (z0*(10**(2*size)) + z2*(10**size) + z1)
    
print multiply(x, y)    
    