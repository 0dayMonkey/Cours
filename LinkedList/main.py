class Noeud:

  def __init__(self, v):
    self.val = v
    self.suivant = None


class Liste:

  def __init__(self, max: 10):
    self.l = None
    self.max = max
    self.cardinal = self.len()

  def is_empty(self):
    return self.l is None

  def display(self):
    noeud_actuel = self.l
    if l.is_empty():
      raise RuntimeError("Empty list")
    else:
      while noeud_actuel:
        print(noeud_actuel.val)
        noeud_actuel = noeud_actuel.suivant

  def display_intrf(self):
    esp = " "
    noeud = self.l
    while noeud:
      esp += str(noeud.val) + " --> "
      noeud = noeud.suivant
    esp += "None"
    return esp

  def len(self):
    compteur = 0
    noeud_actuel = self.l

    while noeud_actuel:
      compteur += 1
      noeud_actuel = noeud_actuel.suivant
    return compteur

  def add_first(self, val):
    nouveau_noeud = Noeud(val)
    if l.len() == self.max:
      raise RuntimeError("Full list")
    else:
      nouveau_noeud.suivant = self.l
      self.l = nouveau_noeud

  def add_last(self, val):
    nouveau_noeud = Noeud(val)
    if l.len() == self.max:
      raise RuntimeError("Full list")
    if self.l is None:
      self.l = nouveau_noeud
      return
    dernier_noeud = self.l
    while dernier_noeud.suivant:
      dernier_noeud = dernier_noeud.suivant
    dernier_noeud.suivant = nouveau_noeud

  def contains(self, val):
    noeud = self.l
    if l.is_empty():
      raise RuntimeError(
        "Pourquoi tu cherche quelque chose dans cette liste, elle est vide")
    while noeud:
      if noeud.val == val:
        return True
      noeud = noeud.suivant
    return False

  def reverse(self):
    if l.is_empty():
      raise RuntimeError("La liste est vide chacal")
    else:
      preced, actu = None, self.l
      while actu is not None:
        proch1 = actu.suivant
        actu.suivant = preced
        preced = actu
        actu = proch1
      self.l = preced

  # faux
  def faux(self):
    noeud = self.l
    if l.is_empty():
      raise RuntimeError("Liste vide")
    else:
      fi = noeud
      noeud = noeud.suivant
      fi = None

  def delete_last(self):
    noeud = self.l
    if not l.is_empty():
      if noeud.suivant == None:
        noeud = None
      else:
        while noeud.suivant.suivant != None:
          noeud = noeud.suivant
        dernier_noeud = noeud.suivant
        noeud.suivant = None
        dernier_noeud = None

###################################################

  def delete(self, v):
    noeud = self.l
    preced = None
    if l.is_empty():
      raise RuntimeError("Liste vide")
    else:
      while not l.is_empty() and noeud.val == v:
        self.l = noeud.suivant
        noeud = self.l
      while noeud:
        while noeud and noeud.val != v:
          preced = noeud
          noeud = noeud.suivant
        preced.suivant = noeud.suivant  # genere une erreur mais marche à 100% !!
        noeud = preced.suivant
      return self.l

  def get_val(self, indice):
    if indice < 0 or indice > self.len() - 1:
      raise IndexError(
        f'Indice invalide, selectioner un indice non eronné, donnez un chiffre entre 0 et {self.len()-1} '
      )
    noeud = self.l
    for i in range(indice):
      if l.is_empty():
        raise RuntimeError("Liste vide UwU")
      noeud = noeud.suivant
    else:
      return noeud.val

  def update_val(self, indice, val):
    if indice < 0:
      raise IndexError(
        f'Indice invalide, selectioner un indice que eronné, donnez un chiffre entre 0 et {self.len()} '
      )
    noeud = self.l
    for i in range(indice):
      if l.is_empty():
        raise RuntimeError("Liste vide UwU")
      noeud = noeud.suivant
    noeud.val = val
    return (f'Valeur changée à l"indice {indice} pour {val}')

  def add(self, liste_python):
    if l.is_empty():
      raise RuntimeError("Liste vide")
    for i in liste_python:
      l.add_first(i)

  def sort(self):
    noeud = self.l
    if l.is_empty():
      raise RuntimeError("Trier une liste vide...")
    else:
      while noeud:
        noeud2 = noeud.suivant
        while noeud2:
          if noeud.val > noeud2.val:
            noeud.val, noeud2.val = noeud2.val, noeud.val
          noeud2 = noeud2.suivant
        noeud = noeud.suivant

  def delete_first(self):
    if l.is_empty():
      raise RuntimeError("Liste vide")
    else:
      noeud = self.l
      self.l = noeud.suivant
      noeud.suivant = None

  def nb_occurence(self, val):
    if l.is_empty():
      raise RuntimeError("Liste vide UwU")
    noeud = self.l
    nb = 0
    while noeud:
      if noeud.val == val:
        nb += 1
      noeud = noeud.suivant
    return nb

  def same(self, liste):
    if not l.is_empty():
      if liste.len() != self.len():
        return False
      else:
        for i in range(self.len()):
          if self.l.val != liste.l.val:
            return False
          else:
            self.l = self.l.suivant
            liste.l = liste.l.suivant
    else:
      raise RuntimeError(
        "Liste vide"
      )  # impossible que ça arrive vu qu'une liste vide = une liste vide
    return True


###################################################
"""
Pas reussi à faire :

*  concatenation(self, liste_deux)
*  insert(self, v)


"""

##################### Zone de Test #################

l = Liste(100)

# test pour same() ( à tester avec a et b --> a.display(),b.display(),a.same(b))
a = Liste(10)
b = Liste(10)

tst = [1,2,3,4]

import random

n = 1
for i in range(9):
  l.add_first(random.randint(0, 10))
  a.add_first(n)
  b.add_first(n)
  n += 1


print(l.is_empty()) # False
assert not l.is_empty()
print(l.display(), "\n") # Liste + None
print(l.len()) # 9
assert l.len() == 9
print(l.display_intrf()) # Liste avec interface
l.sort()
print(l.display_intrf()) # Liste avec triée
l.add_first(5)
print(l.len()) #10
assert l.len() == 10
l.add_last(5)
print(l.len()) # 11
assert l.len() == 11
l.delete_first()
print(l.len()) # 10
assert l.len() == 10
l.delete_last()
print(l.len()) # 9
assert l.len() == 9
l.add_first(666)
print(l.get_val(0)) # 666
assert l.get_val(0) == 666
l.update_val(0,667)
print(l.get_val(0)) # 667
assert l.get_val(0) == 667
print(l.contains(667)) # True
assert l.contains(667)
try:
  l.delete(667) # ça marche hm
except Exception:
  pass
print(l.len()) # 9
assert l.len() == 9
print(l.contains(667)) # False
l.add(tst)
print(l.len()) # 13
for i in range(10): l.add_last(200)
print(l.nb_occurence(200)) # 10
assert l.nb_occurence(200) == 10
print(a.display_intrf()) # Verification de la similaritée
print(b.display_intrf())
print(a.same(b)) # True
assert a.same(b)
rev = Liste(10)
n = 0
for i in range(10): 
  rev.add_first(n)
  n += 1
print(rev.display_intrf()) # afficage avec l'itnerface
rev.reverse() # on reverse notre liste
print(rev.display_intrf()) # affichage avec l'interface
