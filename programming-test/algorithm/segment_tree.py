import os
import sys
from queue import LifoQueue 
from collections import deque 

# To initialize queue in python
# stack = LifoQueue(maxsize = 3) 

# To initialize deque in python
# stack = deque()

# To implement stack in python using list
# stack = [], stack.append(), stack.pop()

# to create sets in python
# you just need to append in curly braces like set = {"agaf", "agag", "agg"} methods are 
# union, update, add, len, remove, discard, pop, copy, issubset, clear

# To create dictionary in python use curly braces to instantiate the hash map in python
# methods are following get, values, items, keys, pop, popitem, del, clear, copy

def create_tree(arr, start_index, last_index):
    print("bfd")
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         final_head_node = None
#         current_node = None
#         count = 0
#         fake_list = head
        
#         while fake_list != None:
#             count += 1
#             fake_list = fake_list.next
        
#         pivoted_index = count - n
                
#         while pivoted_index > 1:
#             if final_head_node == None:
#                 final_head_node = ListNode(val=head.val, next=None)
#                 current_node = final_head_node
#             else:
#                 new_node = ListNode(val=head.val, next=None)
#                 current_node.next = new_node
#                 current_node = new_node
#             head = head.next
                
#             pivoted_index -= 1
        
#         if head.next != None:
#             head.next = head.next.next
        
#         while head != None:
#             new_node = ListNode(val=head.val, next=None)
#             current_node.next = new_node
#             current_node = new_node
#             head = head.next
            
#         final_head_node
        
# headNode = ListNode(val=1,next=None)
# current_node = headNode
# new_node = ListNode(val=2,next=None)
# current_node.next = new_node
# current_node = new_node
# new_node = ListNode(val=3,next=None)
# current_node.next = new_node
# current_node = new_node
# new_node = ListNode(val=4, next=None)
# current_node.next=  new_node
# current_node = new_node
# new_node = ListNode(val=5, next=None)
# current_node.next = new_node
# current_node = new_node

# a = Solution()
# answer = a.removeNthFromEnd(headNode,2)

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        source_node = head
        final_head_node = None
        
        if head != None and head.next == None:
            return head
        
        while source_node != None and source_node.next != None:
            first_node = source_node
            second_node = source_node.next
            if final_head_node == None:
                final_head_node = ListNode(val=second_node.val, next=None)
                new_node = ListNode(val=first_node.val, next=None)
                final_head_node.next = new_node
                current_node = new_node
            else:
                current_node.next = ListNode(val=second_node.val, next=None)
                current_node = current_node.next
                new_node = ListNode(val=first_node.val, next=None)
                current_node.next = new_node
                current_node = new_node
            source_node = second_node.next
                
        if source_node != None:
            new_node = ListNode(val=source_node.val,next=None)
            current_node.next = new_node
            current_node = new_node
            source_node = source_node.next
            
        while final_head_node != None:
            print(final_head_node.val)
            final_head_node = final_head_node.next
        #return final_head_node
    
headNode = ListNode(val=1,next=None)
current_node = headNode
new_node = ListNode(val=2,next=None)
current_node.next = new_node
current_node = new_node
new_node = ListNode(val=3,next=None)
current_node.next = new_node
current_node = new_node
new_node = ListNode(val=4, next=None)
current_node.next=  new_node
current_node = new_node

a = Solution()
a.swapPairs(headNode)