from src.c2.common.node import Node

node = Node(3)

def test_node():
  assert isinstance(node, Node)
  assert node.data == 3
