import random
"""
Algorithme recursif

"""


# Methode du prof
def pgcdn(p, d):
  """
  
  """
  if p == 0:
    return d
  elif d <= p:
    return pgcdn(p - d, d)
  else:
    return pgcdn(p, d - p)


# Methode alternative
def pgcd(p, d):
  if d == 0:
    return p
  else:
    resu = p % d
    return pgcd(d, resu)


# Calculer une puissance
def puissance(a, n):
  if n == 0:
    return 1
  elif n == 1:
    return a
  else:
    return a * puissance(a, n - 1)


# Suite Fibonacci


def Fibb(n):
  if n == 0:
    return 0
  if n <= 2:
    return 1
  else:
    return Fibb(n - 1) + Fibb(n - 2)


#Dériver


def deri():
  choix = input("""
  Sous quelle forme est votre fonction :
  [a] u+v       [d] x
  [b] u*v       [e] ku
  [c] u/v \n
  """)
  if choix == "a":
    u = input("Valeur de u = ")
    v = input("Valeur de v =")
    return int(u) + int(v)


"""Concretement, un appel récursif à expo(2,3) donne maniere tres simplifiée:"""

# On considere la fonction fact(n), definie de maniere récursive et qui retourne le factoriel d'un entier naturel n. Donner le schéma de la pile qui clacule fact(4)

# IV) Compléxité d'un algorithme
"""Etudier la complexité d('un algorithme revient à donner ou estimer le nombre d'op"ration nécessaire pour son exécution

Lors de lexécution d'un algorithme,
- Si le nombre d'opération à effectuer est un nombre constant indépendant de la taille des données, on a une complexité qui vaut O(1)
-Si le nombre d'opération est équivalent à la taille des données n, on à une complexité qui vaut O(n)

-O(n) + O(1) = O(n)
-si R est un nombre constant R x O(n) = O(n)

Pour calculer la complexité, Tn d'une fonction récursive d'un problème de taille n, on peut exprimer Tn en fonction de Tn-1 et appliquer le tableau ci dessous :

Soit Tn la complexité de la fonction récursive factoriel. On a : 
Tn = Tn-1 +1
Tn = Tn-1 + O(1)
Tn = O(n)

"""


def conca(a, b):
  print(a + b)


#conca("bon","jour")

l = []


def ajout(L, a):
  L.append(a)
  return L


def hello(n):
  for i in range(n):
    print("hello")
  print("by")


def affiche_liste(l):
  for i in l:
    print(i)


m = [[1, 2, 3], [4, 5, 6]]


def Mat(M):
  for i in range(len(M)):
    c = len(M[i])
    for j in range(c):
      print('M[]', i, '][]', j, ']=', M[i][j])


# Mat(m)


# Exercices :
# 1) Ecrire une fonction listeAleatoire qui prend un entier n en argument et renvoie une liste de taille n contennt des nombres entre 1 et 10 tirés au hasard
def listeAleatoire(n):
  liste = [random.randint(0, 6) for x in range(n)]
  return liste


# Dégats collateraux émanant de Maelle ↓
#                print ("tranquillou billoute")
#


#2
def ListeAleatoire20():
  li = listeAleatoire(20)
  MaxListe(li)
  lii = singeltons(li)
  for i in lii:
    nbOccurence(i, lii)
  print(li)


#3 Ecrire une fonction maxListe
def MaxListe(l):
  max = None
  for i in l:
    if (max is None or i > max):
      max = i
  print(max)

  #4
  reponse = "c'est fait lol"


#5
liste = [5, 5, 5, 2, 5, 8, 7, 4, 6, 8, 5]


def singeltons(liste):
  lliste = []
  for i in liste:
    if i not in lliste:
      lliste.append(i)
  return lliste


#6
def q6():
  li = listeAleatoire(20)
  for i in li:
    nbOccurence(i, li)
  print(li)


#7 Fonction nombre d'occurence python
def nbOccurence(n, l):
  nb = 0
  for i in l:
    if n == i:
      nb = nb + 1
  print(nb)


"""

Le calcul de la puissance d'un nombre définie par a^0 = 1 et a et a^n = axa^n-1 n'est pas optimal. Il peut être amelioré de la manière suivante :
 - a^0 = 1
 si n est pair a^n = (axa)^n/2

La taille du probleme est divisée par deux a chaque appel récursif. On a donc une relation de récurrence de la forme T(n+1) <= t(n/2) + O(1) = 1 qui même à T(n) = O(log,(n))

"""


def puiss(x, n):
  if n == 0:
    return 1
  else:
    return x * puiss(x, n - 1)


def fus(cgch, cdrt):
  dd, gg, listetrrr = 0, 0, []
  while gg < len(cgch) and dd < len(cdrt):
    if cgch[gg] < cdrt[dd]:
      listetrrr.append(cgch[gg])
      gg += 1
    else:
      listetrrr.append(cdrt[dd])
      dd += 1
  listetrrr += cgch[gg:]
  listetrrr += cdrt[dd:]
  return listetrrr


def triFusion(tab):
  if len(tab) <= 1: return tab
  else:
    milieu = len(tab) // 2
    cgch = triFusion(tab[:milieu])
    cdrt = triFusion(tab[milieu:])
    return fus(cgch, cdrt)


#liste_random= [random.randint(0,100) for i in range(100)]
#print(liste_random)
#triFusion(liste_random)


# Exercice n°4
def pgcdr(p, d):
  if d == 0:
    return p
  else:
    resu = p % d
    return pgcdr(d, resu)


def irreductible(c, d):
  a = pgcdr(c, d)
  return c / a, d / a


#Exercice n°5
liste = []


def car(n):
  if n < 1: return [n]
  return [n] + str(n - 1)


# Exercice n°6
#a
def er(a, n):
  if n == 0: return 1
  if n == 1: return a
  if n % 2 == 0: return er(a * a, n / 2)
  return a * er(a * a, (n - 1) / 2)


#b
def eri(x, y):
  result = 1
  while y != 0:
    if y & 1 == 1:  # si y impair
      result *= x
      y -= 1
    else:  #  y est pair
      x *= x
      y >>= 1
  return result


# Exercice n°7
#b
def egyp(a, b):
  if a == 0: return 0
  if a % 2 == 0: return egyp(a // 2, b * 2)
  else: return b + egyp(a - 1, b)


#Exercice n°10

Tribdick = {}


def Trib(n):
  if n == 0 or n == 1:
    return 0
  if n <= 2:
    return 1
  else:
    Tribdick[n] = Trib(n - 1) + Trib(n - 2) + Trib(n - 3)
    return Trib(n - 1) + Trib(n - 2) + Trib(n - 3)


def Tribi(n):
  a, b, c = 0, 0, 1
  for maelle in range(3, n + 1):
    d, a, b = a + b + c, b, c
    c = d
  if n < 2: return 0
  return d


# Entrainement : Pour un contrôle que je vais surrement encore rater ^^


#Suite de Fibonnaci en recursif
def fib(n):
  if n == 0: return 0
  if n <= 2: return 1
  else: return fib(n - 1) + fib(n - 2)


# Nombre d'occurence en itératif
def nbo(s, c):
  n = 0
  for i in s:
    if c == i: n = n + 1
  print(n)


# Exos du livre


def pgcde(a, b):
  if b == 0:
    return 1
  if a > b:
    return pgcde(a - b, b)


# Un mot est un palindrome si on peut le lire dans les deux sans de gauche à droite et de droite à gauche. Exemple KAYAK est un palindrome. Ecrire une fonction récursive permettant de vérifier si un mot est palindrome.
def palin(m):
  if str(m) == str(m)[::-1]: return True
  return False


# Exo5 : Fonction compte a rebourd liste
def exo5(n):
  return list(range(n, -1, -1))


print("Tu vas réussir !!!")

#exercice n°13
"""
a) 
1 1 1 1 1 1
1 1 1 1 2
1 1 1 3
1 1 4
1 5
b) 
c) :
"""
pieces = [20, 10, 5, 2, 1]


def rd(l, n):
  if n < 0: return 0
  if not l: return 0
  if n == 0: return 1
  return rd(l, n - l[0]) + rd(l[1:], n)


"""Modularité
Introduction
  I) Modules et packages
    a) Principes de modularité
Développer un logiciel ou simplement un programme conduit à répondre à un demande qui peut généralement être scindée à différents petits problémes. Ainsi répondre à la demande revient à resoudre chaque petit probléme independement afin qu'ils puissent intéragir si besoin. Pour ce faire on applique le principe de la programmation modulaire qui consiste entre autres a :
* Découper le code en fonctions et les classer par théme dans desfichiers appelesmodules
* classer ces modules dans des packages
* grouper des methodes ( fonctions) dans une classe en utilisant la programation objet.
    b) importation
    import nom_module as nom pour importer le module nom_module en le renommant par nom. Par exemple :
    import math as m
    m.sqrt(4) → 2

    On a aussi from nom_module import function pour importer function de nom_module. Par exemple :
    from math import sin
    sin(-1)

Exercice n°1
1) 
c
2)
a

II) Documentation
Que l'on écrire ou qu'on utilise une fonction ouun module, la documentation est centrale pour que le travail soit réutilisable.
Parmi les différents mécanismes, l'un des plus simples est la docstring qui peut être attachée à une fonction, à une méthode, à une classe, à unmodule, ou à un package. Dans tous les cas, c'est une chaine de caractere qui doit figurer au début de l'entité qu'elle documente. Cette documentation est ensuite consultable à l'aide de la commande help. 
a) assertions
Une assertion se fait à l'aide du mot clé "assert". Si l'expression qui suit le mot assert vaut True. Le programme poursuit sin exécution. Sinon elle s'arrête et indique AssertionError. 
Exemple : 
Commenter les lignes de code suivantes extraites dans des programmes.

assert  2 == 3 
>>> ça nous fait une AssertionError donc ça interomp l'execution

from math import sqrt 
>>> ok

asert sqrt(25) == 5
>>> c'est juste, la racine de 25 c'est bien 5 donc ça continue l'execution

assert 5*2+4 == 30
>>> ça nous fait une AssertionError donc ça interomp l'execution

assert fibo(3) == 2 
>>> Si la fonction est bien écrite, ça continue le programme

b) Le module doctest permet d'inserer des tests dans la docstring d'une fonction. Les doctests sont repérés à l'aide de la chaine >>>. 
Ecrire des doctests permet à la fois de realiser des tests et de documenter efficacement les fonctions.

c)

Exemple :
import pytest
from fibo import fibo


def test_0():
    assert fibo(0) == 0


def test_3():
    assert fibo(3) == 2


def test_7():
    assert fibo(7) == 13


def test_neg():
    with pytest.raises(ValueError):
        fibo(-1)

Exercice n°7
"""


def valeur1(chaine):
  s = 0
  for c in chaine:
    if c >= "A" and c <= "Z":
      s = s + ord(c) - ord('A') + 1
    return s


def valeurcorriger(chaine):
  s = 0
  for c in chaine.upper():
    if c >= "A" and c <= "Z": s = s + ord(c) - ord('A') + 1
  return s


def valeur2(chaine):
  s = 0
  for c in chaine.upper():
    if c >= "A" and c < "Z":
      s = s + ord(c) - ord('A') + 1
  return s


import string


def valeur3(chaine):
  s = 0
  for c in chaine.upper():
    if c in string.ascii_uppercase:
      s = s + string.ascii_uppercase.index(c)
  return s


import math


def terme(k: int) -> float:
  return 1 / (k**2)


def approxpi(n: int) -> float:
  s = 0
  # utilise les termes jusqu’à 1/n**2 inclus
  for k in range(1):
    s = s + terme(k + 1)
  return math.sqrt(s * 6)


def plusun(n):
  """
  >>> plusun(5)
  6
  
  """
  print(n + 1)


"""
La fonction expo permet de calculer le reste de la division par n de a
>>> expo(3,2,1)
9
>>> expo(6,7,8)
34992

pgcd(a,b) → renvoie le plus grand diviseur commun de a et b
>>> pgcd(66,60)
6
"""

import string
import itertools


def decale(lettre, dec):
  """
  decale(lettre,dec) → La fonction decale permet de decaler    l'index de le lettre, en attribuant alors une nouvelle et retournant 
  
  
  """
  alph = string.ascii_uppercase
  new_index = (alph.index(lettre) + dec) % 26
  return alph[new_index]


def cesar(message, dec):
  res = []
  for l in message:
    res.append(decale(l, dec))
  return ''.join(res)


def vigenere(message, passwd):
  res = []
  for (lettre, decl) in zip(message, itertools.cycle(passwd)):
    dec = string.ascii_uppercase.index(decl)
    res.append(decale(lettre, dec))
  return ''.join(res)


"""Exo bac
1) c'est fait

2) string.ascii_uppercase est un string qui contient tout les lettres ASCII en majuscules

3) On fait help(itertools.cycle) & help(zip)
"""
#for lettre, decl in zip(message, itertools.cycle(passwd))
"""
Cette ligne ligne de code est le début d'une boucle : Elle va repeter l'instruction désignée juste en dessous autant de fois qu'il y a de lettre dans lettre


Sequence 3 : Programmation objet.
Jusque là nous avons vu la programmation procédurale. C'est à dire nous avons utiliser ou realiser un ensemble d'instructions en manipulant des variables, données, fonctions et procédure. Il est temps de passer à un passer à un type de programmation plus avancé : programmation objet. Comme son nom l'indique, nous allons manipuler des objets à l'aide de la structure class. 

Dans une classe on trouve entre autres : 
* Une étiquette : son nom
* une ou plisuers attributs ou états
* les valeurs de ces états
* des methodes : procédure qui permettent de modifier les états.
Exemple :
"""


class Eleve:
  " Ici on peux mettre une deifinition d'une classe"

  def __init__(self, nom, prenom):
    """Methode d'initialisation avec les parametres"""
    self.nom = nom
    self.prenom = prenom


"""
Remarques :
* Le premier parametre self : toutes les méthodes le disposent come premier parametre. Il permet de faire référence à l'objet luimême
* La définition de la classe Eleve commence par une méthode spéciale __init__ dont le nom commence et termine par deux underscores ( tiret du 8 → _ ).
* Les constructeurs premettent de passer des valeurs par défaut à un objet au moment de la création. 
"""


class Rectangle:
  " Sert seulement à définir la classe Rectangle"

  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur


Rectangle("7", "5")
#Retourne un rectangle de 7 de longueur et 5 de largeur


class Date:
  "Sert à définir une date"

  def __init__(self, j, m, a):
    self.jour = j
    self.mois = m
    self.année = a


Date("13", "07", "2005")
#Retourne le 13/07/2005
"""
a) création d'une instance
Après avoir crée une classe, on peut facilement crée des objets ayant la structure de cette dernière. Par exemple en considérant l'exemple précédent, l'instruction :
"""

Eleve(
  "Hadji", "Macoumba"
)  # crée un objet Eleve et initialise les valeurs de ses attributs nom et prenom à l'aide du constructeur __init__. On instancie l'objet Eleve. L'objet crée a la même structure que l'objet Eleve ; c'est une instance.
student = Eleve(
  "NSI", "Terminale"
)  # déclare la variable student et lui affecte une instance de l'objet Eleve ( de nom NSI et de prenom " Terminale  ")
"""
Notons que : 
* la variable student ne contient pas l'objet mais c'est un pointeur qui pointe sur le bloc mémoire qui contient l'objet
* schematiquement on a :
              .__________________.
              |prenom:"Terminale"|
              |------------------|
student --->  |    nom : "NSI"   |
              |__________________|

b) manipulation des attributs d'instance
On peut modifier les atributs d'instance à l'aied de la notation objet.attribut.
Considérons l'exemple précédent :
>> student.nom
"NSI"
>> student.nom = "Prépa"
>> student.nom
"Prépa"

Remarques :
* Les attributs d'instances sont propres aux instances. On ne peut y accéder qu'à partir de l'objet instancié.
* Python permet de crée des attributs non définis au moment de la création de l'objet. 

>> student.spe = "PC"
>> student.spe
"PC"
Cette dernière implémentation est à bannir car elle peut être une source d'erreurs.

c) Implémentation de méthodes
On peut manipuler les attributs d'instance à l'aide de méthodes définies dans la classe. 

Exemple :
Vous pourrez utiliser la classe Rectangle créee dans la partie précédente
1) Ecrire une méthode __str__ qui affiche les informations du rectangle 
2) Ecrire une méthode qui calcul et retourne son aire
3) Ecrire une méthode qui calcule et renvoie son périmetre
4) Ecrire une méthode qui permet de savoir si le rectangle est un carré.
"""


class Rectangle:
  " Sert seulement à définir la classe Rectangle"

  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur

  def __str__(self):  #1
    print("La longueur est", self.longueur, "\nLa largeur est", self.largeur)

  def aire(self):  #2
    """Calcule et retourne l'aire du rectangle initié"""
    return self.largeur * self.longueur

  def peri(self):  #3
    """Calcule le perimetre du triangle"""
    return (self.largeur + self.longueur) * 2

  def isquare(self):  #4
    if self.longueur == self.largeur:
      return "Oui le rectangle est un carré"
    return "Non, c'est bien un rectangle magueule"


rec = Rectangle(5, 4)
"""
Considérons l'exemple de la classe Eleve où dans le constructeur.

1) Ajouter les attributs : notes_nsi et specialites, sous forme de listes qui sont initialement vides.
2) Ecrire une méthode qui ajoute une ou plusieurs notes en NSI. On permettra à l'utilisateur d'ajouter une note jusqu'a ce qu'il réponde Non ou N. Les notes sont comprises entre zéro et vingt.
3) Ecrire une méthode qui ajoute un ou plusieurs choix de spécialité.
4) Ecrire une méthode qui renvoie la note moyenne de l'élève en NSI
5) Ecire une méthode __str__ qui affiche les informations de base de l'éléve : nom, prénom. 

"""
import time
from typing import List


def nouvelle_page():
  print("\u001B[H\u001B[J")


class Cellule():

  def __init__(self) -> None:

    self.actuel = False
    self.futur = False
    self.voisins = None

  def est_vivant(self) -> bool:

    return self.actuel

  def set_voisins(self, voisins):
    self.voisins = voisins

  def get_voisins(self):
    """
        Renvoie la liste des voisins de la cellule
        """
    return self.voisins

  def naitre(self):
    """
        Met l’état futur de la cellule à True
        """
    self.futur = True

  def mourir(self):
    """
        Met l’état futur de la cellule à False
        """
    self.futur = False

  def basculer(self):
    """
        Fait passer l’état futur de la cellule 
        dans l’état actuel
        """
    self.actuel = self.futur

  def __str__(self):
    """
        Représentation de l'objet sous forme 
        d'une chaîne de caractères
        """
    if self.actuel:
      chaine = "X"
    else:
      chaine = "-"
    return chaine

  def calcule_etat_futur(self):
    """
        Implémente les règles d’évolution du jeu 
        de la vie en préparant l’état futur à sa
        nouvelle valeur
        """
    nbre_voisins_vivants = 0

    for cell_voisine in self.get_voisins():
      if cell_voisine.est_vivant():
        nbre_voisins_vivants += 1

    if (nbre_voisins_vivants != 2) and\
    (nbre_voisins_vivants != 3) and\
    self.est_vivant():
      self.mourir()
    elif (nbre_voisins_vivants == 3) and\
    not self.est_vivant():
      self.naitre()
    else:
      self.futur = self.actuel


from typing import List
from random import random


class Grille:
  """
    Grille du Jeu de la Vie
    """

  def __init__(self, hauteur, largeur):
    """
        Initialisations des attributs
        """
    self.hauteur = hauteur
    self.largeur = largeur
    self.matrix = self.set_matrice()

  def set_matrice(self):
    """
        Construction de la grille de cellules
        """
    matrice = [[Cellule() for j in range(self.largeur)]
               for i in range(self.hauteur)]
    return matrice

  def dans_grille(self):
    """
        Vérifie que le point de coordonnées (i,j) 
        est dans la grille
        """
    return 0 <= j < self.largeur and 0 <= i < self.hauteur

  def set_cell_xy(self):
    """
        Affecte une nouvelle cellule à la case (i,j)
        de la grille
        """
    if self.dans_grille(i, j):
      self.matrix[i][j] = cellule
    else:
      raise IndexError(f"({i}, {j}) pas dans la grille")

  def get_cell_xy(self):
    """
        Récupère la cellule située dans la case (i,j) 
        de la grille
        """
    if self.dans_grille(i, j):
      return self.matrix[i][j]
    else:
      raise IndexError(f"({i}, {j}) pas dans la grille")

  def get_largeur(self):
    return self.largeur

  def get_hauteur(self):
    return self.hauteur

  def est_voisin(i: int, j: int, x: int, y: int) -> bool:
    return (abs(x - i) == 1) or (abs(y - j) == 1)

  def get_voisins(self):
    """
        Renvoie la liste des voisins d’une cellule
        """
    voisins = []
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        if self.dans_grille(i, j) and\
        Grille.est_voisin(x, y, i, j):
          voisins.append(self.get_cell_xy(i, j))
    return voisins

  def set_voisins(self):
    """
        Affecte à chaque cellule de la grille la liste 
        de ses voisins
        """
    for i in range(self.hauteur):
      for j in range(self.largeur):
        cellule = self.get_cell_xy(i, j)
        cellule.set_voisins(self.get_voisins(i, j))

  def __str__(self):

    chaine = ""
    for i in range(self.hauteur):
      for j in range(self.largeur):
        chaine += str(self.get_cell_xy(i, j)) + " "
      chaine += "\n"
    return chaine

  def remplir_alea(self, taux: int):
    for i in range(self.hauteur):
      for j in range(self.largeur):
        if random() <= (taux / 100):
          cellule = self.get_cell_xy(i, j)
          cellule.naitre()
          cellule.basculer()

  def jeu(self):
    for i in range(self.hauteur):
      for j in range(self.largeur):
        cellule = self.get_cell_xy(i, j)
        cellule.calcule_etat_futur()

  def actualise(self):
    """
        Bascule toutes les cellules de la 
        Grille dans leur état futur
        """
    for i in range(self.hauteur):
      for j in range(self.largeur):
        cellule = self.get_cell_xy(i, j)
        cellule.basculer()


def main():
  plateau = Grille(30, 30)
  plateau.remplir_alea(50)
  plateau.set_voisins()
  while True:
    nouvelle_page()
    print(plateau)
    print("\n")
    time.sleep(0.8)
    plateau.jeu()
    plateau.actualise()


main()

def _____test_____():
  print(studentt.note_nsi)
  studentt.ajout_note(ajout)
  print(studentt.note_nsi)
  studentt.ajout_note(7)
  print(studentt.note_nsi)
  studentt.moyenne()
  print(studentt.spé)
  studentt.ajout_spé(ajoutspé)
  print(studentt.spé)
  studentt.ajout_spé(1)
  print(studentt.spé)
  studentt.ajout_spé("SES")
  print(studentt.spé)
  studentt.__str__()
  print(etudiant.nom)
  print(etudiant.liste_eleve)
  etudiant.ajout_eleve()
def adam(n):
  """
  adam(n)→ renvoie n *5
  
  >>> adam(5)
  25
  """
  return n * 5
  from rich import print


def test():
  classe = ["une", "deux", "trois"]

  for i in range(len(classe)):
    print(i + 1, ")", classe[i])
  dl = input("choix : ")
  classe.pop(int(dl) - 1)
  isinstance("s", int)


print("[bold cyan]hey[/bold cyan]")

classe = ["Tb", "Ta", "Te"]

import math


def sus(e=math.sin(69)):
  print(e)


class Cellules:

  def __init__(self,
               actuel: bool = False,
               futur: bool = False,
               voisins: list = None):
    self.actuel = actuel
    self.futur = futur
    self.voisins = voisins

  def __str__(self):
    if self.actuel == True:
      print("X")
    else:
      print("-")

  def est_vivant(self):
    return self.actuel

  def set_voisins(self):
    self.voisins = self.voisins

  def get_voisins(self):
    return self.voisins

  def naitre(self):
    self.futur = True

  def mourir(self):
    self.futur = False

  def basculer(self):
    self.futur = self.actuel

  def calcule_etat_futur(self):
    compteur = 0
    for i in self.voisins.est_vivant():
      if i == True:
        compteur += 1
      else:
        compteur += 0
    if self.actuel == True:
      if compteur >=2 and compteur <= 3:
        self.futur == True
      elif compteur == 0 or compteur >3:
        self.futur == False
"""
Une liste chainée est une structure de données parmi tant d'autres. On commencera à définir sa structure avant de les implémenter à l'aide des classes.

Définition :

Une structure de données est une manière de définir, stocker, accéder, modifier des données. Exemples : Tableaux, tuples, dictionnaires.
 

I) Structure d'une liste chainée
   a) Une liste chainée est une structure qui permet de regrouper des données. Elle peut être vue comme une liste ordonnée d'éléments/objets/noeuds dont :
   * Chaque noeud contient une valeur et un pointeur qui pointe vers un autre element
   * Une luiste vide est une liste vide qui pointe sur Null ou None

Remarques :
* Une liste chainée est uniquement caractérisée par son nom L ou son premier élement ( hear, tête, car )
* Le reste de la liste est dit queue, tail, corps, cdr
* La structure ci-dessus est dite liste simplement chainée. EN effet, chaque noeud pointe sur un seul element ( son suivant ).
* Il existe des liste doublement chainées ou chaque élement pointe sur sons uivant et son précédent ; des listes clique où le dernier element pointe sur le premier



II) Implémentation d'une liste chainée
a) Implémentation les algorithmes ( structures, fonctions ou procédure)
Implémentater les algorithmes ( structures, fonctions ou procédure)





fonction existe(L,val)
si L= Null 
  renvoyer Faux
x = L
tant que x.valeur different val:
    x = x.suivant
    si x = Null:
      renvoyer faux
    sinon:
      renvoyer vrai


montrer
x = L
si x est null
  afficher " La liste est vide"
tant que x.suivant est different Null
   afficher x
   x = x.suivant

supprimer le premier element :
si L est vide 
afficher " la liste est vide"
sinon supprimer L.suivant

suprimer le dernier element :
x = L
si x est null
  afficher " La liste est vide"
tant que x.suivant.suivant est different Null
   x = x.suivant
si x.suivant.suivant = null
supprimer x.suivant

longueur :
long = 1
tant que x.suivant est different Null
   ajouter 1 à long
   x = x.suivant
si x.suivant = null:
afficher long

longueur recursive:
si x est null
retourne 0
si x.suivant = null
return 1
sinon retourne longueur recusrive 1 + x.suivant

insere_apres(L,element,nouveau):
tant que x est different element
x = x.suivant
si x = element
element.suivant = x.suivant
x.suivant = nouveau
"""

class Noeud:
    def __init__(self, v , suivant=None):
        self.v = v
        self.suivant = suivant

n = Noeud(6)

class Liste:
    def __init__(self, lst=None):
        self.l = lstP

    def is_empty(self):
      if self.l is None:
        return True
      return False
    def error(self):
      raise IndexError("La liste est vide")
    
    def add_first(self,element):
      if self.is_empty() == True:
        self.l.n.suivant = element
      element.n.suivant = self.l.n.suivant
      self.l.n.suivant = element

n = Noeud(6)
l = Liste()
l.add_first(5)

"""
class Noeuds:
    def __init__(self, val):
        self.val = val
        self.suivant = None

class Liste:
    def __init__(self,l = None):
        self.l = l
      
    def is_empty(self):
      if self.l is None:
        return True
      return False
      
    def error(self):
      print("La liste est vide\n")
      
    def display(self):
      if self.is_empty() == True:
        self.error()
      else:
        noeud = self.l
        while noeud:
            print(noeud.val)
            noeud = noeud.suivant

    def add_last(self, val):
        noeudnouv = Noeuds(val)
        if self.is_empty() == True:
            self.l = noeudnouv
            return

        noeudderni = self.l
        while noeudderni.suivant:
            noeudderni = noeudderni.suivant
        noeudderni.suivant = noeudnouv

    def add_first(self, val):
          if self.is_empty() == True:
            self.l = noeudnouv
            return
          else:
            noeudnouv = Noeuds(val)
            noeudnouv.suivant = self.l
            self.l = noeudnouv

    def contains(self, value):
        if self.is_empty() == True:
            return False
        else:
          noeud = self.l
          while noeud:
              if noeud.val == value:
                  return True
              noeud = noeud.suivant 
        return False

    def insert_after_node(self, element, val):

        if not element:
            self.add_first(val)
            return

        noeudnouv = Noeuds(val)

        noeudnouv.suivant = element.suivant
        element.suivant = noeudnouv

    def delete_node(self, key):

        noeud = self.l

        if noeud and noeud.val == key:
            self.l = noeud.suivant
            noeud = None
            return

        prev = None
        while noeud and noeud.val != key:
            prev = noeud
            noeud = noeud.suivant

        if noeud is None:
            return

        prev.suivant = noeud.suivant
        noeud = None

    def delete_node_at_pos(self, pos):

        noeud = self.l

        if pos == 0:
            self.l = noeud.suivant
            noeud = None
            return

        prev = None
        count = 1
        while noeud and count != pos:
            prev = noeud
            noeud = noeud.suivant
            count += 1

        if noeud is None:
            return

        prev.suivant = noeud.suivant
        noeud = None

    def len_iterative(self):

        count = 0
        noeud = self.l

        while noeud:
            count += 1
            noeud = noeud.suivant
        return count

    def len_recursive(self, node):
        noeud = self.l
        if noeud is None:
            return 0
        return 1 + self.len_recursive(noeud.suivant)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.l
        while curr_1 and curr_1.val != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.suivant

        prev_2 = None
        curr_2 = self.l
        while curr_2 and curr_2.val != key_2:
            prev_2 = curr


n = Noeuds(6)
l = Liste()
l.display(),l.add_last(5),l.add_first(6),l.add_last(7),l.display(),l.contains(5)
"""


"""
# Verifier que chaque image soit dans le bon sens 
import random
dir = ["haut","gauche","droite","bas"]
l = [dir[random.randrange(len(dir))] for i in range(9)]
print(l)



def quel(i):
  if i == dir[0]:
    return 0
  if i == dir[1]:
    return 1
  if i == dir[2]:
    return 2
  if i == dir[3]:
    return 3


def verif(i,n):
  num = quel(i)
  if i == n:
    print(i)
    return i
  if i == dir[3]:
    return verif(dir[0],n)
  if i != n:
    print(i,"\nProchain :\n")
    return verif(dir[num+1],n)

def change(n):
  for i in range(len(l)):
    if l[i] != n:
      l[i] = verif(l[i],n)


change("haut")
print(l)
"""


"""
IV) Tableaux associatifs

Définitions
Un tableau associatif est un type abstrait qui associe des valeurs a des clés et est muni des operations suivantes :
* ajout d'une nouvelle valeur associée a une nouvelle clé 
* modification de la valeur associée a une clé existante
* Suppression d'une clé et de la valeur associée
* récuperation de la valeur associée à une clé donnée 
* Récupération de la clé d'une valeur donnée

Exemple :
Un tableau associatif pourrait par exemple associer les valeurs "couples prénom/nom" aux clés " numéro de sécurité sociale", la contrainte étant que chaque clé doit être unique dans le tableau associatif
"""
