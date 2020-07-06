dict  = { 1:"atf", "gagf":"babfd" }
print(dict)
print(dict.items())
print(dict.keys())
print(dict.get(1))
print(dir(dict.items()[0]))
print(dict.items()[0][1]) # strategy to read tuples. items() give tuples list from hash
#print(dir(dict))
print(dict.has_key('agfaf'))

set_example = {"agsg", "gfga", "agfga", 'agsg', "gfga"}
for x in set_example:
    print(x)

tuple_array = ()
#tuple_array.__add__("aag")
print(tuple_array)

a  =[[]]
print(a)
m, n = 5,6
arr = [[n-x for x in range(n)] for x in range(m)]
print(arr)
arr[0].sort()
print(arr[0])

class Test:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    # def __repr__(self):
    #     return '({},{})'.format(self.name, self.id)
    
Test1 = Test("raja",1)
Test2 = Test("bose",2)
testarray = [Test1,Test2]

def get_name(test_object):
    return test_object.name

print(testarray)
sorted_by_name = sorted(testarray, key=get_name)
print(sorted_by_name[0].name)