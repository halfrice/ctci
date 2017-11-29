from src.c2.common.linked_list import LinkedList

ll = LinkedList()

def test_linked_list():
  assert isinstance(ll, LinkedList) is True
  assert ll.is_empty() is True

def test_add():
  ll.add('a')
  assert ll.is_empty() is False
  ll.add('b')
  ll.add('c')

def test_remove():
  ll.remove('c')
  ll.remove('b')
  ll.remove('a')
  assert ll.is_empty() is True

def test_stringify():
  ll.add('o')
  ll.add('a')
  ll.add('m')
  ll.add('l')
  assert ll.stringify() == 'lmao'
