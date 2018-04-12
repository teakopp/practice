#!/bin/python

# How to make linked list in Python http://stackabuse.com/python-linked-lists/

class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with node data"
        if self.data == value:
            return True
        else:
            return False


class SingleLinkedList:
    def __init__(self):
        "constructor to initate this object"

        self.head = None
        self.tail = None
        return


# node1 = ListNode(15)
# node2 = ListNode(8.2)
# node3 = ListNode("Berlin")





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
