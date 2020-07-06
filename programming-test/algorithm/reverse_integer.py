import math

def reverse_int(n):
    i2 = 0
    i3 = 0
    i5 = 0
    next2 = 2
    next3 = 3
    next5 = 5
    uglynumbers = [0]*(n+1)
    uglynumbers[0] = 1
    next = 1
    for i in range(0,n):
        next = min(next5,min(next2,next3))
        uglynumbers[i+1] = next
        print(next)
        if next == next2:
            i2 = i2 + 1
            next2 = uglynumbers[i2] * 2
        elif next == next3:
            i3 = i3 + 1
            next3 = uglynumbers[i3] * 3
        elif next == next5:
            i5 = i5 + 1
            next5 = uglynumbers[i5] * 5
    
    return next

#print(reverse_int(10)) 


def count_perfectsquares(lower_bound, upper_bound):
    n = math.ceil(math.sqrt(upper_bound)) - math.floor(math.sqrt(lower_bound))
    if lower_bound == math.sqrt(lower_bound)*math.sqrt(lower_bound):
        n = n+1
    print(math.floor(n))

count_perfectsquares(2,100)
    