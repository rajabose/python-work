def count_dir(str=""):
    str_len = len(str)
    count = 0
    final_dict = {}
    operation_stack = []
    while count < str_len:
        if str[count] != '.':
            if (str[count] in final_dict.keys()):
                final_dict[str[count]] += 1
            final_dict[str[count]] = 1
            operation_stack.append(str[count])
            count = count + 2
        else:
            if len(operation_stack) > 0:
                 operation_stack.pop()
                
            if len(operation_stack) > 0:
                if operation_stack[len(operation_stack)-1] in final_dict.keys():
                    final_dict[operation_stack[len(operation_stack)-1]] = final_dict[operation_stack[len(operation_stack)-1]] + 1
                else:
                    final_dict[operation_stack[len(operation_stack)-1]] = 1
                count = count + 3
    
    return final_dict        


result = count_dir("a/b/../c/d/e/../../")
print(result)