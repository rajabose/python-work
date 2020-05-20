#quick sort logic using pivoted point
#Remember partition concept comes here. Problem is that once we see so much patterns we never judge all
#those important data in our lifes.
def partition(arr, startIndex, lastIndex):
    count_index = -1
    pivot_index = lastIndex
    initial_index = startIndex
    while initial_index <= lastIndex -1:
        if arr[pivot_index] > arr[initial_index]:
            count_index += 1
            value = arr[initial_index]
            arr[initial_index] = arr[count_index]
            arr[count_index] = value
            initial_index += 1
        
        value = arr[count_index+1]
        arr[count_index+1] = arr[pivot_index]
        arr[pivot_index] = value
    return count_index + 1
         
def quick_sort(arr, startIndex, lastIndex):
    if lastIndex > startIndex:
        pi =  partition(arr, startIndex, lastIndex)
        
        quick_sort(arr, startIndex, pi-1)
        quick_sort(arr, pi+1, lastIndex)

arr = [1,9,5,4,3,2,8,6]
#quick_sort(arr,0, 7)
sum_array = [0 for x in range(0,len(arr))]
sum = 0
for x in range(0,len(arr)):
    sum_array[x] = sum + arr[x]
    sum =  sum_array[x]
print(sum_array)