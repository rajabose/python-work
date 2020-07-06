# create prefix or fenwick tree with associated values of key.
# array = [1, 3, 0, -1, 5, 10, -2, 4, 11]
#steps to follow to create fenwick tree to check the values
def convert(arr, n, bit):
    for i in range(0, n):
        update(bit, i+1, n+1, arr[i])

def update(bit, i, n, val):
    while i < n:
        bit[i] += val
        i+= (i & -i) 
    
def query(arr, i, n, bit):
    total_sum = 0
    while i > 0:
        total_sum += bit[i]
        i-= ( i & -i )
    return total_sum

def find_range_sum(arr, n):
    bit = [0]* (n+1)
    convert(arr, n, bit)
    print(bit)
    
    value = query(arr, 5, n, bit)
    print(value)
    
    arr[5] = 10
    update(bit, 6, n+1, 10)
    print(bit)
    
    value = query(arr, 6, n, bit)
    print(value)
    
    
arr = [1, 3, 0, -1, 5, 10, -2, 4, 11]
find_range_sum(arr, len(arr))
