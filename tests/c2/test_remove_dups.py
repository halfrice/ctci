from src.c2.remove_dups import RemoveDups

ll = RemoveDups()

def test_remove_dups():
  ll.add('a')
  ll.add('b')
  ll.add('b')
  ll.add('c')
  ll.add('c')
  ll.add('c')
  ll.add('b')
  ll.add('b')
  ll.add('a')
  ll.remove_dups('c')
  assert ll.stringify() == 'abbcbba'
  ll.remove_dups('b')
  assert ll.stringify() == 'abca'
  ll.remove_dups('a')
  assert ll.stringify() == 'abc'

# def test_remove_dups_no_buffer():
#   ll.add('c')
#   ll.add('c')
#   ll.add('x')
#   ll.remove_dups_no_buffer('c')
#   assert ll.stringify() == 'xdba'
