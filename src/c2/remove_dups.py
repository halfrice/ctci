# Remove Dups

# Write code to remove duplicates from an unsorted linked list. How would you solve this problem
# if a temporary buffer is not allowed?

from src.c2.common.linked_list import LinkedList

class RemoveDups(LinkedList):
  # def __init__(self):
    # LinkedList.__init__(self)

  def remove_dups(self, data):
    node = self.head
    prev = None
    cut = None
    while node:
      if node.data == data:
        if cut:
          prev.next = node.next
        else:
          prev = node
          cut = node
      else:
        prev = node
      node = node.next

  def remove_dups_no_buffer(self, data):
    return
