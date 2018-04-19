# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        return

    def has_value(self, value):
        if self.val == value:
            return True
        else:
            return False

class SingleLinkedList:
    def __init__(self):

        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    def list_length(self):

        count = 0
        current_node = self.head

        while current_node is not None:

            count = count + 1

            current_node = current_node.next

        return count

    def output_list(self):

        current_node = self.head

        while current_node is not None:
            print(current_node.val)
            current_node = current_node.next

        return


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        h1 = l1.head
        h2 = l2.head

        while h1.next != None:
            h1 = h1.next
            number1 = h1.val

        number1 = ListNode(h1)
        print number1.data

        while h2.next != None:
            h2 = h2.next
            number2 = h2.val

        number2 = ListNode(h2)

        print number1.val
        print number2.val





node1 = ListNode(15)
node2 = ListNode(8)

l1 = SingleLinkedList()

for current_item in [node1, node2]:
    l1.add_list_item(current_item)

node1 = ListNode(2)
node2 = ListNode(4)


l2 = SingleLinkedList()

print("l2 length: %i" % l2.list_length())

for current_item in [node1, node2]:
    l2.add_list_item(current_item)

add = Solution()
add.addTwoNumbers(l1, l2)
