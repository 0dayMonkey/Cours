####################      Stack : Pile         ###########################


class Stack:

  def __init__(self):
    self.l = None

  def push(self, val):
    nouveau_noeud = Noeud(val)
    nouveau_noeud.suivant = self.l
    self.l = nouveau_noeud

  def pop(self):
    if self.l is None:
      raise IndexError(" La pile est vide")
    temp = self.l
    self.l = self.l.suivant
    return temp.val

  def der_val(self):
    if self.l is None:
      return None
    return self.l.val

  def is_empty(self):
    return not bool(self.l)

  def display(self):
    temp = self.l
    while (temp):
      print(temp.val)
      temp = temp.suivant

  def __str__(self):
    ret_str = " "
    temp = self.l
    while temp:
      ret_str += str(temp.val) + " --> "
      temp = temp.suivant
    ret_str += "None"
    return ret_str

  def reverse(self):
    precedent, noeud_actuel = None, self.l
    while noeud_actuel is not None:
      suiv = noeud_actuel.suivant
      noeud_actuel.suivant = precedent
      precedent = noeud_actuel
      noeud_actuel = suiv
    self.l = precedent

  def search(self, value):
    find = False
    sta = Stack()
    while not find and self.head is not None:
      v = self.head.v
      if v == value:
        find = True
      else:
        sta.push(self.pop())
    while sta.head is not None:
      self.push(sta.pop())
    return find

  def update(self, value, nv):
    qu = Stack()
    while not self.is_empty():
      v = self.pop()
      if v == value:
        qu.push(nv)
      else:
        qu.push(v)
    while not qu.is_empty():
      self.push(qu.pop())

  """      
      l = impr.l
            while l is not None:
                print(l.val)
                l = l.suivant
            l = pair.l
            while l is not None:
                print(l.val)
                l = l.suivant
         """


def copie(s):
  stack_tempo = Stack()
  copie_s = Stack()
  while not s.is_empty():
    stack_tempo.push(s.pop())
  while not stack_tempo.is_empty():
    val = stack_tempo.pop()
    s.push(val)
    copie_s.push(val)
  print(copie_s.__str__())
  return copie_s


def separ(s, stack_pair=Stack(), stack_impr=Stack()):
  stack_tempo = Stack()
  while not s.is_empty():
    stack_tempo.push(s.pop())
  while not stack_tempo.is_empty():
    val = stack_tempo.pop()
    s.push(val)
    if val % 2 == 0: stack_pair.push(val)
    else:
      stack_impr.push(val)
  print(stack_impr.__str__())
  print(stack_pair.__str__())
  return (stack_pair, stack_impr)


def parenthesage(string, stack=Stack()):
  for i in string:
    if i == '(':
      stack.push(i)
    elif i == ')':
      if stack.is_empty():
        return False
      else:
        stack.pop()
    if i == '[':
      stack.push(i)
    elif i == ']':
      if stack.is_empty():
        return False
      else:
        stack.pop()
  if stack.is_empty():
    return True
  else:
    return False


try:
  assert parenthesage('][([))()(')
except Exception:
  pass
assert parenthesage('((()))')
assert parenthesage('((()') == False
assert parenthesage('()))')
