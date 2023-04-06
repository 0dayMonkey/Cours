import bisect


class ArbreHuffman:

  def __init__(self, lettre, nbocc, g=None, d=None):
    self.lettre = lettre
    self.nbocc = nbocc
    self.gauche = g
    self.droite = d

  def est_feuille(self) -> bool:
    return self.gauche is None and self.droite is None

  def __lt__(self, other):
    # Un arbre A est strictement inférieur à un arbre B
    # si le nombre d’occurrences indiqué dans A est
    # strictement **supérieur** à celui de B
    return self.nbocc > other.nbocc


def parcoudroite(arbre, chemin_en_coudroite, dico):
  if arbre is None:
    return
  if arbre.est_feuille():
    dico[arbre.lettre] = chemin_en_coudroite
  else:
    parcoudroite(arbre.gauche, chemin_en_coudroite + [0], dico)
    parcoudroite(arbre.droite, chemin_en_coudroite + [1], dico)


def fusionne(gauche, droite) -> ArbreHuffman:
  nbocc_total = gauche.nbocc + droite.nbocc
  return ArbreHuffman(None, nbocc_total, gauche, droite)


def compte_occurrences(texte: str) -> dict:
  """
        Renvoie un dictionnaire avec chaque caractère du texte
        comme clé et le nombre d’apparition de ce caractère
        dans le texte en valeur
        >>> compte_occurrences("AABCECA")
        {"A": 3, "B": 1, "C": 2, "E": 1}
        """
  occ = dict()
  for car in texte:
    if car not in occ:
      occ[car] = 0
    occ[car] = occ[car] + 1
  return occ


def construit_liste_arbres(texte: str) -> list:
  """ Renvoie une liste d’arbres de Huffman, chacun réduit 
        à une feuille """
  dic_occurrences = compte_occurrences(texte)
  liste_arbres = []
  for lettre, occ in dic_occurrences.items():
    liste_arbres.append(ArbreHuffman(lettre, occ))
  return liste_arbres


def codage_huffman(texte: str) -> dict:
  """ Codage de Huffman optimal à partir d’un texte
        >>> codage_huffman("AAAABBBBBCCD")
        {'A': [0, 0], 'C': [0, 1, 0], 'D': [0, 1, 1], 'B': [1]}
        """
  liste_arbres = construit_liste_arbres(texte)
  # Tri par nombres d’occurrences décroissants
  liste_arbres.sort()
  # Tant que tous les arbres n’ont pas été fusionnés
  while len(liste_arbres) > 1:
    arbre1 = liste_arbres.pop(0)
    arbre2 = liste_arbres.pop(0)
    arbre_fusionne = fusionne(arbre1, arbre2)
    bisect.insort(liste_arbres, arbre_fusionne)
  # Il ne reste plus qu’un arbre, c’est celui qui contient tous les codes
  arbre_final = liste_arbres[0]
  dico_codes = dict()
  parcoudroite(arbre_final, [], dico_codes)
  return dico_codes


class ArbreBinaire:
  def __init__(self, etiquette, gauche=None, droite=None):
        self.etiquette = etiquette
        self.gauche = gauche
        self.droite = droite
  
  def add_left(self, NouvNoeud):
    if self.gauche == None:
        self.gauche = ArbreBinaire(NouvNoeud)
    else:
        t = ArbreBinaire(NouvNoeud)
        t.gauche = self.gauche
        self.gauche = t
  
  
  def add_right(self, NouvNoeud):
    if self.droite == None:
        self.droite = ArbreBinaire(NouvNoeud)
    else:
        t = ArbreBinaire(NouvNoeud)
        t.droite = self.droite
        self.droite = t
  
  def largeur(self):
    if self.gauche and self.droite:
      return self.etiquette+self.gauche.largeur()+self.droite.largeur()
    elif self.gauche:
      return self.etiquette+self.gauche.largeur()
    elif self.droite:
      return self.etiquette+self.droite.largeur()
    else:
      return self.etiquette 

    def __str__(self):
        def str_recursive(node, prefix):
            if node is None:
                return ""
            s = prefix + str(node.etiquette) + "\n"
            if node.gauche is not None or node.droite is not None:
                s += prefix + "/" + " "*(len(str(node.etiquette))-1) + " \\" + "\n"
                s += str_recursive(node.gauche, prefix + " "*(len(str(node.etiquette))))
                s += str_recursive(node.droite, prefix + " "*(len(str(node.etiquette))))
            return s
        return "Racine\n" + str_recursive(self, "")
      
  def set_left(self, value):
    self.gauche = value

  def set_right(self, value):
    self.droite = value

def hauteur(bintree):
    if bintree is None:
        return -1
    return 1 + max(hauteur(bintree.gauche), hauteur(bintree.droite))

def is_feuille(bintree):
    return bintree.gauche is None and bintree.droite is None

def affiche_etiquette_feuille(bintree):
    if bintree is None:
        return
    if is_feuille(bintree):
        print(bintree.etiquette)
    affiche_etiquette_feuille(bintree.gauche)
    affiche_etiquette_feuille(bintree.droite)

def Nb_occurence(bintree, val):
    if bintree is None:
        return 0
    return (1 if bintree.etiquette == val else 0) + Nb_occurence(bintree.gauche, val) + Nb_occurence(bintree.droite, val)

a = ArbreBinaire("a")

a.__str__()



Jeu = {
  
'Astérix': ['Gaulois', 'Formidables', 
           [['Le Village', 57, (34, 22)], 
           ['Autre Village', 123, (36, 23)]]], 
 
'Obélix': ['Gaulois', 'Formidables', 
          [['Le Village', 161, (38, 28)]]],
 
'César': ['Romain', 'Pax', 
         [['Rome', 1668, (151, 12)]]]
      
}

def alliance_joueur(jeu, j):
 return jeu[j][1]

def population_joueur(jeu, j):
  return sum([village[1] for village in jeu[j][2]])

def population_peuple(jeu, p):
  s = 0
  for joueur in jeu.values():
    if joueur[0] == p:
      s += sum([village[1] for village in joueur[2]])
  return s