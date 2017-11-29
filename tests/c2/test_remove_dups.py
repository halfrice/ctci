from src.c2.remove_dups import *

ll = LinkedList()

def test_linked_list():
  assert isinstance(ll, LinkedList)
  assert ll.is_empty()

def test_add():
  ll.add('a')
  ll.add('b')
  ll.add('c')
  ll.add('c')
  ll.add('x')
  ll.add('x')
  ll.add('d')
  assert ll.stringify() == 'dxxccba'

def test_remove():
  ll.remove('x')
  assert ll.stringify() == 'dccba'

def test_remove_dups():
  ll.add('c')
  ll.add('c')
  ll.stringify()
  ll.remove_dups('c')
  assert ll.stringify() == 'cdba'

def test_remove_dups_no_buffer():
  ll.add('c')
  ll.add('c')
  ll.add('x')
  ll.remove_dups_no_buffer('c')
  assert ll.stringify() == 'dbaxc'
