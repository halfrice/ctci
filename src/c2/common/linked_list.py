from src.c2.common.node import Node

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
    # search and destroy first found
    node = self.head
    prev = None
    while node:
      if node.data == data:
        if prev:
          prev.next = node.next
        else:
          self.head = node.next
        return True
      prev = node
      node = node.next
    return False

  def stringify(self):
    node = self.head
    s = ''
    while node:
      s += node.data
      node = node.next
    return s
