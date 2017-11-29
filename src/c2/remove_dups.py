# Remove Dups

# Write code to remove duplicates from an unsorted linked list. How would you solve this problem
# if a temporary buffer is not allowed?

class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def is_empty(self):
    return self.head == None

  def add(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def remove(self, data):
    # search and destroy all
    node = self.head
    prev = None
    while node:
      if node.data == data and prev:
        prev.next = node.next
      elif node.data == data and not prev:
        self.head = node.next
      prev = node
      node = node.next

  def remove_dups(self, data):
    node = self.head
    prev = None
    keep_node = None
    # find node to keep
    while not keep_node:
      if node.data == data:
        keep_node = node
      node = node.next
    # find and forget any duplicate nodes until a non-dup is found
    found_dup = False
    while node:
      if node.data == data:
        found_dup = True
      elif node.data != data and found_dup:
        prev.next = node
        found_dup = False
      else:
        prev = node
      node = node.next

  def remove_dups_no_buffer(self, data):
    self.remove(data)
    self.add(data)

  def stringify(self):
    node = self.head
    s = ''
    while node:
      s += node.data
      node = node.next
    return s
