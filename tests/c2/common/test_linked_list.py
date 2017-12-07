from src.c2.common.linked_list import LinkedList

ll = LinkedList()

def test_linked_list():
  assert isinstance(ll, LinkedList) is True
  assert ll.is_empty() is True

def test_add():
  ll.add('a')
  assert ll.is_empty() is False
  ll.add('b')
  ll.add('b')
  ll.add('c')
  ll.add('c')
  ll.add('c')
  ll.add('b')
  ll.add('b')
  ll.add('a')
  assert ll.stringify() == 'abbcccbba'

def test_remove():
  assert ll.remove('c') is True
  assert ll.stringify() == 'abbccbba'
