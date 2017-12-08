from src.c2.kth_to_last import KthToLast

ll = KthToLast()
ll.add('a')
ll.add('b')
ll.add('c')
ll.add('d')
ll.add('e')
ll.add('f')
ll.add('g')

def test_kth_to_last_linked_list():
  assert ll.stringify() == 'gfedcba'

def test_kth_to_last():
  assert ll.kth_to_last(1) == 'a'
  assert ll.kth_to_last(2) == 'b'
  assert ll.kth_to_last(3) == 'c'
  assert ll.kth_to_last(7) == 'g'
