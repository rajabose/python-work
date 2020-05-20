import os
import sys

array = []
input = sys.stdin.readline
size_of_array, other_input = input().split()
for x in range(0, int(size_of_array)/2):
    for z in range(0, x):
        print(" "),
    for y in range(0, int(size_of_array) - 2*x):
        print(y),
    for t in range(0, x):
        print(" ")
    print("\n")

   
# ############ ---- Input Functions ---- ############
# def inp():
#     return(int(input()))
# def inlt():
#     return(list(map(int,input().split())))
# def insr():
#     s = input()
#     return(list(s[:len(s) - 1]))
# def invr():
#     return(map(int,input().split()))

#Points to be remembered
#1. Input.
#2. Collection like Map, Dict, Set, List, Sorting algorithm, Array, Tuple, Mutuable and Non Mutuable.
#3. Multidimensional Collection.
#4. String manuplation.
#5. Object Oriented Concept.
#6. File Handling.
#7. Cache Handling.
#8. Airthmetic and Logical Operations expression.


#Challenges in the coding
#1. Index or out of Index error in the array. happens quite frequently in the code because of algorithm
#2. Storing object instance in the array or list.