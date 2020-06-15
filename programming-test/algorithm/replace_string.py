#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the mutualSubstitutions function below.
def mutualSubstitutions(s, subFirst, subSecond):
    hash_str = {}
    str_array = [''] * len(s) 
    for elem in range(0, len(s)):
        if s[elem] not in hash_str.keys():
            hash_str[s[elem]] = []
            hash_str[s[elem]].append(elem)
        else:
            hash_str[s[elem]].append(elem)
        str_array[elem] = s[elem]

    for i in range(0, len(subFirst)):
        if subFirst[i] in hash_str.keys():
            a = hash_str[subFirst[i]]
            for j in a:
                str_array[j] = subSecond[i]
                
        if subSecond[i] in hash_str.keys():
            a = hash_str[subSecond[i]]
            for j in a:
                str_array[j] = subFirst[i]
    
    return ''.join(str_array)

# a = ['a','b','c','d','e','fa']
# print(''.join(a))
#if __name__ == '__main__':

def square(match):
    number  =  int(match.group(0))
    return int(number**2)

print(mutualSubstitutions("keyboard",['m','a'],['y','o']))
