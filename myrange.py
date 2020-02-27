#Implementing my version of the ramge function

def myrange(first, second=None, step=1):
    
    if second is None:
        current = 0
        maxnum = first
    
    else:
        current = first
        maxnun = second
        
    if step > 0:
        while current < maxnum:
            yield current
            current += step
    
    else: 
        while current > maxnum:
            yield current
            current += step
    
    
print(list(myrange(5)))