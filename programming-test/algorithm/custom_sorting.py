def custom_sort_key(word):
    split_array = word.split()
    new_array =  split_array[1:]
    return "".join(new_array).lower()

str_array = ["af4 act try boat","ag4 aaa duck duck", "log4 duke lenge tab dekhnege"]

str_array = sorted(str_array, key=custom_sort_key)
#print(str_array)
# x = [(ord(name[0]),name[0]) for name in sorted(namelist)]
# to reverse sort, sorted(names, reverse=True)

#how to use lambda to sort an string array or any list or hash
# to sorted(str_array, key=lambda x:x[::-1])

def reverse_word(word):
    return word[::-1]

a = [1,5,7,8,3,5,8,1,1,1,1]
b = a[5:]
a = sorted(a[0:5])
a = a + b
print(a)