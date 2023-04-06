class Noeud:
    def __init__(self, val):
        self.val = val
        self.suivant = None

#####################  Linked List : Liste chainée   #################class####


class Liste:
    def __init__(self):
        self.l = None

    def display(self):
        noeud_actuel = self.l
        while noeud_actuel:
            print(noeud_actuel.val)
            noeud_actuel = noeud_actuel.suivant 

    def add_last(self, val):
        nouveau_noeud = Noeud(val)

        if self.l is None:
            self.l = nouveau_noeud
            return

        dernier_noeud = self.l
        while dernier_noeud.suivant:
            dernier_noeud = dernier_noeud.suivant
        dernier_noeud.suivant = nouveau_noeud

    def add_first(self, val):
        nouveau_noeud = Noeud(val)

        nouveau_noeud.suivant = self.l
        self.l = nouveau_noeud
   
    def contains(self, val):
        noeud = self.l
        while noeud:
            if noeud.val == val:
                return True
            noeud = noeud.suivant
        return False

    def insert_after_node(self, precedent_node, val):

        if not precedent_node:
            print("Pas dans la liste")
            return

        nouveau_noeud = Noeud(val)

        nouveau_noeud.suivant = precedent_node.suivant
        precedent_node.suivant = nouveau_noeud

    def delete_node(self, element):

        noeud_actuel = self.l

        if noeud_actuel and noeud_actuel.val == element:
            self.l = noeud_actuel.suivant
            noeud_actuel = None
            return

        precedent = None
        while noeud_actuel and noeud_actuel.val != element:
            precedent = noeud_actuel
            noeud_actuel = noeud_actuel.suivant

        if noeud_actuel is None:
            return

        precedent.suivant = noeud_actuel.suivant
        noeud_actuel = None

    def delete_node_at_pos(self, pos):

        noeud_actuel = self.l

        if pos == 0:
            self.l = noeud_actuel.suivant
            noeud_actuel = None
            return

        precedent = None
        compteur = 1
        while noeud_actuel and compteur != pos:
            precedent = noeud_actuel
            noeud_actuel = noeud_actuel.suivant
            compteur += 1

        if noeud_actuel is None:
            return

        precedent.suivant = noeud_actuel.suivant
        noeud_actuel = None

    def len_iterative(self):

        compteur = 0
        noeud_actuel = self.l

        while noeud_actuel:
            compteur += 1
            noeud_actuel = noeud_actuel.suivant
        return compteur

    def len_recursive(self, noeud):
        if noeud is None:
            return 0
        return 1 + self.len_recursive(noeud.suivant)

    def reverse(self):
        preced, actu = None, self.l
        while actu is not None:
            proch1 = actu.suivant
            actu.suivant = preced
            preced = actu 
            actu = proch1
        self.l = preced
      
    def is_empty(self):
      return self.l is None

    


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
        while(temp):
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
        precedent,noeud_actuel = None, self.l
        while noeud_actuel is not None:
            suiv = noeud_actuel.suivant
            noeud_actuel.suivant = precedent
            precedent = noeud_actuel
            noeud_actuel = suiv
        self.l = precedent



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
   while not s.is_empty():stack_tempo.push(s.pop())
   while not stack_tempo.is_empty():
     val = stack_tempo.pop()
     s.push(val)
     copie_s.push(val)
   print(copie_s.__str__())
   return copie_s

def separ(s,stack_pair=Stack(),stack_impr= Stack()):
     stack_tempo = Stack()
     while not s.is_empty(): stack_tempo.push(s.pop())
     while not stack_tempo.is_empty():
       val = stack_tempo.pop()
       s.push(val)
       if val % 2 == 0:stack_pair.push(val)
       else:
          stack_impr.push(val)
     print(stack_impr.__str__())
     print(stack_pair.__str__())
     return (stack_pair, stack_impr)


def parenthesage(string, stack = Stack()):
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
assert  parenthesage('((()')  == False
assert  parenthesage('()))') 

"""crée des chaines de caractere random à  parenthese

l = []
n = 1
for i in range(10):
  chance = random.randint(0,10)
  if chance < 5:
    f'({l}{n}.append())'
  
"""
  

####################      Queue : File         ###########################

class Queue:
    def __init__(self):
        self.entete = None
        self.fin_queue = None

    def isEmpty(self):
        return self.entete is None

    def Enqueue(self, val):
        temp = Noeud(val)

        if self.fin_queue == None:
            self.entete = self.fin_queue = temp
            return
        self.fin_queue.suivant = temp
        self.fin_queue = temp

    def Dequeue(self):
        if self.isEmpty():
            raise IndexError(
                "La queue est vide, impossible de dequeue")
        temp = self.entete
        self.entete = temp.suivant

        if(self.entete == None):
            self.fin_queue = None

    def display(self):
      if self.isEmpty():
        raise IndexError("La queue est vide, impossible de d'afficher")
      temp = self.entete
      while(temp):
          print(temp.val)
          temp = temp.suivant

    def reverse(self):
        precedent = None
        noeud_actuel = self.l
        while noeud_actuel is not None:
            suiv = noeud_actuel.suivant
            noeud_actuel.suivant = precedent
            precedent = noeud_actuel
            noeud_actuel = suiv
        self.l = precedent


q = Queue() # Queue --> Files
s = Stack() # Stack --> Piles
l = Liste() # Liste chainée
n = Noeud(1)

n = 1
for i in range(10):
  s.push(n)
  l.add_first(n)
  n += 1


import random

def attendre_doublon(n):
  liste = []
  while len(liste) < n:
    val = random.randint(0,n)
    if val in liste:
      liste.append(val)
      return len(liste)
    liste.append(val)
  return 0


def temps(n,nb):
  e = 0
  for i in range(nb): 
    e =  e+int(attendre_doublon(n))
  return e/nb



class Tableau:
    def __init__(self):
        self.dico = {}

    def __setitem__(self, key, value): # modification 
        self.dico[key] = value

    def __getitem__(self, key): # avoir un item par sa clé
        return self.dico[key]

    def __delitem__(self, key): # suppression 
        del self.dico[key]

    def __len__(self): #taille
        return len(self.dico)

    def __str__(self): # affichage
        return str(self.dico)

 


    
a = Tableau()
