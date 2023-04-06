"""
Séquence 6 : Structures arborescentes
* Introduction :

- Pour étudier des données gigantesques les structures de données vues s'avére être inefficaces. Les Structures arborescentes permettent de stocker efficacement de telles données, d'y acceder rapidement, de représenter les parties d'un jeu entre autres.

a) Définition
Un arbre enbin_tree_tuple ( ou arborescence ) est constitué de noeuds organisés de maniere hierarchique : c'est un graphe non orienté, connexe, sans cycle dans lequel on a choisi un noeud particulier appelé la bin_tree_tuple. Chaque noeud peut être étiqueté par une valeur


Les noeuds sans fils → noeud externe




b) Caractéristiques d'un arbre
*Dans un arbre, chaque noeud a exactement un seul noeud pére, à l'exception de l'unique noeud bin_tree_tuple qui n'en a pas.
Chaque noeud peut avoir zéro, un ou pluieurs fils, dot il est le père.
* La taille d'un arbre est son nombre de noeuds 
* Les noeuds qui n'ont pas de fils sont appelés feuilles ou noeuds externes. Les autres sont dits noeuds internes
* l'Arité d'un noeud est son nombre de fils. Deux noeuds ayant le même pére sont dit frères
* La profondeur d'un noeud est la longueur du chemin le plus court vers la bin_tree_tuple ( la bin_tree_tuple a donc pour profondeur 0)
* La hauteur d'un arbre est la profondeur du noeud le plus profond ( 0 s'il est réduit à la bin_tree_tuple et, par convention, -1 si l'arbre est vide )


1) A
2) c d e g i et noeud interne b h  
3) b et f
4) taille = 9 hauteur = 3h


II) Arbres binaires 
a) Définition
* Un arbre binaire est un arbre dont chaque noeud a au plus deux fils
* Un arbre binaire est équilibré si, pour chaque noeud interne, les sous arbres gauche et droit ont une hauteur qui diffère de 1 au plus

* Un arbre binaire est complet à gauche si tous ses niveaux sont remplis, sauf eventuellement le dernier ( et que les feuilles du dernier niveau sont tassées à gauche )

* Un arbre binaire est dit parfait si toutes les feuilles ont la même profondeur

b) Parcours d'un arbre binaire

* Le parcours d'un arbre définie dans quelle ordre on parcourt ses noeuds
* Parcours en largeur : L'arbre est parcouru par niveau de gauche à droite
* Parcours préfixe/pré-ordre : Chaque noeud est parcouru avant ses fils
* Parcours infixe/en ordre : chaque noeud est visité après son fils gauche et avant son fils droit

* Parcours postfixe/postordre/suffixe : Chaque noeud est visité après son fils gauche et son fils droit 
"""


class BinaryTree:

  def __init__(self, v):
    self.val = v
    self.ls = None
    self.rs = None
# Ajout

  def add_left(self, NouvNoeud):
    if self.ls == None:
      self.ls = BinaryTree(NouvNoeud)
    else:
      t = BinaryTree(NouvNoeud)
      t.ls = self.ls
      self.ls = t

  def add_right(self, NouvNoeud):
    if self.rs == None:
      self.rs = BinaryTree(NouvNoeud)
    else:
      t = BinaryTree(NouvNoeud)
      t.rs = self.rs
      self.rs = t

  # Modification

  def set_left(self, value):
    self.left = value

  def set_right(self, value):
    self.right = value

  def set_val(self, valObjet):
    self.val = valObjet


# Affichage

  def preorder(self):
    print(self.val)
    if self.ls:
      self.ls.preorder()
    if self.rs:
      self.rs.preorder()

  def postorder(self):
    if self.ls:
      self.ls.postorder()
    if self.rs:
      self.rs.postorder()
    print(self.val)

  def inorder(self):
    if self.ls:
      self.ls.inorder()
    print(self.val)
    if self.rs:
      self.rs.inorder()

  def largeur(self):
    if self.ls and self.rs:
      return self.val+self.ls.largeur()+self.rs.largeur()
    elif self.ls:
      return self.val+self.ls.largeur()
    elif self.rs:
      return self.val+self.rs.largeur()
    else:
      return self.val

  def right(self):
    return self.rs

  def left(self):
    return self.ls

  def get_val(self):
    return self.val

bite = BinaryTree(5)

# Fonction


def is_empty(bin_tree):
  return bin_tree.val == None


def is_extern_node(self, bin_tree):
  if bin_tree.ls == None and bin_tree.rs == None:
    return True
  return False


def size(bin_tree):
  if bin_tree is None:
    return 0
  else:
    return size(bin_tree.ls) + 1 + size(bin_tree.rs)


def extern_node(bin_tree):
  if bin_tree == None:
    return 0
  if bin_tree.left() == None and bin_tree.right() == None:
    return 1
  else:
    return extern_node(bin_tree.left()) + extern_node(bin_tree.right())


def intern_node(bin_tree):
  if bin_tree == None:
    return 0
  if bin_tree.ls == None and bin_tree.rs == None:
    return 0
  else:
    return 1 + intern_node(bin_tree.ls) + intern_node(bin_tree.rs)


bite.add_left(4)
bite.add_right(8)

# binary tree implementation using tuples
def arbre_binaire(r):
    return [r, [], []] # bin_tree_tuple, gauche, droite

def inserer_gauche(bin_tree_tuple, nouvelle_branche):
    t = bin_tree_tuple.pop(1)
    if len(t) > 1: # si la branche gauche n'est pas vide
        bin_tree_tuple.insert(1, [nouvelle_branche, t, []])
    else:
        bin_tree_tuple.insert(1, [nouvelle_branche, [], []])
    return bin_tree_tuple

def inserer_droite(bin_tree_tuple, nouvelle_branche):
    t = bin_tree_tuple.pop(2)
    if len(t) > 1: # si la branche droite n'est pas vide
        bin_tree_tuple.insert(2, [nouvelle_branche, [], t])
    else:
        bin_tree_tuple.insert(2, [nouvelle_branche, [], []])
    return bin_tree_tuple

def obtenir_valeur_bin_tree_tuple(bin_tree_tuple):
    return bin_tree_tuple[0]

def definir_valeur_bin_tree_tuple(bin_tree_tuple, nouvelle_valeur):
    bin_tree_tuple[0] = nouvelle_valeur

def obtenir_enfant_gauche(bin_tree_tuple):
    return bin_tree_tuple[1]

def obtenir_enfant_droite(bin_tree_tuple):
    return bin_tree_tuple[2]

def is_extern_node(bin_tree_tuple):
  if bin_tree_tuple[1] == None and bin_tree_tuple[2] == None:
    return True
  return False
  
def size(bin_tree_tuple):
  return len(bin_tree_tuple)

def infixe(bin_tree_tuple):
  return bin_tree_tuple[1] + bin_tree_tuple[2]

def postfixe(bin_tree_tuple):
  return bin_tree_tuple[0] + bin_tree_tuple[1] + bin_tree_tuple[2]
  
def extern_node(bin_tree_tuple):
  if bin_tree_tuple[1] == None and bin_tree_tuple[2] == None:
    return 1
  else:
    return extern_node(bin_tree_tuple[1]) + extern_node(bin_tree_tuple[2])

def intern_node(bin_tree_tuple):
  if bin_tree_tuple[1] == None and bin_tree_tuple[2] == None:
    return 0
  else:
    return intern_node(bin_tree_tuple[1]) + intern_node(bin_tree_tuple[2])


def parcours_largeur(bin_tree_tuple):
  if is_extern_node(bin_tree_tuple):
    return extern_node(bin_tree_tuple)
  else:
    return parcours_largeur(bin_tree_tuple[1]) + parcours_largeur(bin_tree_tuple[2])
  

def bin_tree_tuple(bin_tree_tuple):
  return bin_tree_tuple[0]

def bin_tree_tuple_gauche(bin_tree_tuple):
  return bin_tree_tuple[1]

def bin_tree_tuple_droite(bin_tree_tuple):
  return bin_tree_tuple[2]

def bin_tree_tuple_tuple(bin_tree_tuple):
  return (bin_tree_tuple[0], bin_tree_tuple[1], bin_tree_tuple[2])

def is_empty(bin_tree_tuple):
  return bin_tree_tuple[1] == None and bin_tree_tuple[2] == None



# Huffman's Coding
def huffman_coding(bin_tree_tuple):
  if is_empty(bin_tree_tuple):
    return None
  else:
    bin_tree_tuple_tuple = bin_tree_tuple_tuple(bin_tree_tuple)
    bin_tree_tuple_gauche = bin_tree_tuple_gauche(bin_tree_tuple)
    bin_tree_tuple_droite = bin_tree_tuple_droite(bin_tree_tuple)
    if bin_tree_tuple_gauche == None:
      return bin_tree_tuple_droite
    else:
      return huffman_coding(bin_tree_tuple_gauche) + bin_tree_tuple_droite

def huffman_decoding(bin_tree_tuple):
  if is_empty(bin_tree_tuple):
    return None
  else:
    bin_tree_tuple_tuple = bin_tree_tuple_tuple(bin_tree_tuple)
    bin_tree_tuple_gauche = bin_tree_tuple_gauche(bin_tree_tuple)
    bin_tree_tuple_droite = bin_tree_tuple_droite(bin_tree_tuple)
    if bin_tree_tuple_gauche == None:
      return bin_tree_tuple_droite
    else:
      return huffman_decoding(bin_tree_tuple_gauche) + bin_tree_tuple_droite

def huffman_decoding_infixe(bin_tree_tuple):
  if is_empty(bin_tree_tuple):
    return None
  else:
    bin_tree_tuple_tuple = bin_tree_tuple_tuple(bin_tree_tuple)
    bin_tree_tuple_gauche = bin_tree_tuple_gauche(bin_tree_tuple)
    bin_tree_tuple_droite = bin_tree_tuple_droite(bin_tree_tuple)
    if bin_tree_tuple_gauche == None:
      return bin_tree_tuple_droite
    else:
      return huffman_decoding_infixe(bin_tree_tuple_gauche) + bin_tree_tuple_droite

def huffman_decoding_postfixe(bin_tree_tuple):
  if is_empty(bin_tree_tuple):
    return None
  else:
    bin_tree_tuple_tuple = bin_tree_tuple_tuple(bin_tree_tuple)
    bin_tree_tuple_gauche = bin_tree_tuple_gauche(bin_tree_tuple)
    bin_tree_tuple_droite = bin_tree_tuple_droite(bin_tree_tuple)
    if bin_tree_tuple_gauche == None:
      return bin_tree_tuple_droite
    else:
      return huffman_decoding_postfixe(bin_tree_tuple_gauche) + bin_tree_tuple_droite



##################### Exercices Bacs ##############################

class Noeud :

    def __init__(self, cle):
        self.cle = cle
        self.gauche = None
        self.droit = None

    def insere(self, cle):
        if cle < self.cle :
            if self.gauche == None :
                self.gauche = Noeud(cle)
            else :
                self.gauche.insere(cle)
        elif cle > self.cle :
            if self.droit == None :
                self.droit = Noeud(cle)
            else :
                self.droit.insere(cle)
    def hauteur(self):
      if self.gauche == None and self.droit == None:
          return 1
      if self.gauche == None:
          return 1 + self.droit.hauteur()
      elif self.droit == None:
          return 1 + self.gauche.hauteur()
      else:
          hg = self.gauche.hauteur()
          hd = self.droit.hauteur()
          if hg > hd:
              return hg + 1
          else:
              return hd + 1

class Arbre :

    def __init__(self, cle):
        self.racine = Noeud(cle)

    def insere(self, cle):
        self.racine.insere(cle)
      
    def hauteur(self):
        return self.racine.hauteur()

    # methode taille qui renvoie la taille de l'arbre  
    def taille(self):
      if self.gauche is None and self.droit is None:
        return 1
      if self.gauche is None:
        return 1 + self.droit.taille()
      if self.droit is None:
        return 1 + self.gauche.taille()  
      return 1 + max(self.gauche.taille(), self.droit.taille())
    #  On souhaite écrire une méthode bien_construit de la classe Arbre qui renvoie la valeur True si l’arbre est « bien construit » et False sinon.
    def bien_construit(self):
      if self.gauche is None and self.droit is None:
        return True
      if self.gauche is None:
        return self.droit.bien_construit() and self.gauche.bien_construit()
      if self.droit is None:
        return self.gauche.bien_construit() and self.droit.bien_construit()
      return self.gauche.bien_construit() and self.droit.bien_construit()
      
    # methode dessin qui renvoie une chaîne de caractères représentant l'arbre sous forme de chaîne de caractères.
    def dessin(self):
      if self.gauche is None and self.droit is None:
        return " "
      if self.gauche is None:
        return self.droit.dessin() + " "
      if self.droit is None:
        return self.gauche.dessin() + " "
      return self.gauche.dessin() + " " + self.droit.dessin()
      