# Return Kth to Last

# Implement an algorithm to find the kth to last element of a singly linked list.

from src.c2.common.linked_list import LinkedList

class KthToLast(LinkedList):
  def __init__(self):
    LinkedList.__init__(self)

  def kth_to_last(self, n):
    node = self.head
    mem = None
    count = 0
    while node:
      count += 1
      if count >= n:
        if mem:
          mem = mem.next
        else:
          mem = self.head
      node = node.next
    return mem.data
