    
def merge_sort(arr, startIndex, lastIndex):
    mid = (startIndex + lastIndex)/2
    # fist_half = arr[startIndex:mid]
    # second_half = arr[mid:lastIndex+1]
    
    if lastIndex - startIndex >= 2:
        merge_sort(arr,startIndex, mid-1)
        merge_sort(arr, mid, lastIndex)
        current_index = 0
        local_array = arr[startIndex:lastIndex+1] #it is an array of slice which means its index start with zero
        first_half_index = startIndex
        second_half_index =  mid
        
        while first_half_index < mid and second_half_index <= lastIndex:
            if arr[first_half_index] <= arr[second_half_index]:
                local_array[current_index] = arr[first_half_index]
                first_half_index +=1
                current_index += 1
            else:
                local_array[current_index] = arr[second_half_index]
                second_half_index += 1
                current_index += 1
        if first_half_index < mid:
            while first_half_index < mid:
                local_array[current_index] = arr[first_half_index]
                first_half_index += 1
                current_index += 1
        if second_half_index <= lastIndex:
            while second_half_index <= lastIndex:
                local_array[current_index] = arr[second_half_index]
                current_index += 1
                second_half_index += 1
                
        current_index = 0
        while startIndex <= lastIndex:
            arr[startIndex] = local_array[current_index]
            current_index += 1
            startIndex += 1
                
    elif lastIndex - startIndex == 1 and arr[startIndex] > arr[lastIndex]:
        value = arr[lastIndex]
        arr[lastIndex] = arr[startIndex]
        arr[startIndex] = value
    
arr = [1,9,5,4,3,2,8,6]
merge_sort(arr,0, 7)
# mid = 7/2
#print(arr[4:7])
# print(arr[mid:7])
print(arr)