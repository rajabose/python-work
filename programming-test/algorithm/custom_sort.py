def reorderElements(logFileSize, logLines):
    # WRITE YOUR CODE HERE
    
    num_index = -1
    current_index = logFileSize-1
    
    while current_index >=0:
        split_array = logLines[current_index].split(" ")
        split_array = split_array[1:]
        join_str = "".join(split_array)
        if join_str.isnumeric():
            num_index = current_index
        else:
            if num_index == -1:
                num_index = logFileSize
            #num_index =  num_index - 1
            temp_value = logLines[current_index]
            logLines[current_index] = logLines[num_index]
            logLines[num_index] = temp_value
            num_index = num_index - 1 
        current_index = current_index - 1 
        
    num_index = num_index - 1
    if num_index >=0:
        #sort array
        sorted(logLines[0:num_index+1],key=custom_key)
        
    return logLines
    #pass

def custom_key(str):
    a = str.split(" ")
    a = a[1:]
    final_str = "".join(a)
    final_str.lower()