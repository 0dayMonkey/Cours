from __future__ import annotations
# Pour pouvoir annoter les types des instances de classes 
from typing import List
# Pour renseigner le type des éléments des listes
from PIL import Image
# Pour travailler sur les images
from numpy.random import permutation
# Pour créer des permutations aléatoirement

class Perm:
    """
    On définit une permutation en donnant ses images ou sa taille.
    Dans ce dernier cas, une permutation est aléatoirement choisie
    """

    def __init__(self, taille = None, images = None) -> None:
        """
        Une permutation a pour attributs sa taille et la liste de ses images.
        Un des deux doit être donné au moment de l'instanciation.
        Une Permutation est si besoin créée aléatoirement en utilisant la fonction permutation
        du module numpy.random
        
        >>> Perm(6).images
        [1, 3, 0, 2, 5, 4]
        >>> Perm(images = [1,0,2]).taille
        3 
        """
        # si la taille n'est pas donnée, c'est la longueur de la liste des images
        self.taille = taille if taille else len(images)
        # si les images ne sont pas données, on les tire aléatoirement
        self.images = images if images else list(permutation(range(taille)))

    def __repr__(self) -> str:
        """
        On représente les images de la permutation :

        >>> Perm(6)
        1 3 0 2 5 4
        """
        return " ".join([str(image) for image in self.images])

    def __invert__(self) -> Perm :
        """
        Permet d'obtenir la permutation réciproque de self avec ~

        >>> p = Perm(4)
        >>> p
        1 3 0 2
        >>> ~p
        2 0 3 1
        """
        return None
        
    def permute(self, xs: List[int]) -> List[int]:
        """
        Permute les éléments d'une liste donnée en argument 
        Si xs = [xs[0], xs[1], xs[2],...] et si p est une permutation alors  
        p.permute(xs) = [xs[p(0)], xs[p(1)], xs[p(2)],...] 
        
        >>> p = Perm(5)
        >>> xs = ['a', 'b', 'c', 'd', 'e']
        >>> p.permute(xs)
        ['e', 'd', 'c', 'b', 'a']
        """
        return None


class Chaine:
    """
    Une chaîne d'entiers est construite à partir d'une liste d'entiers
    Permet d'être manipulée par un cryptosystème par blocs
    """

    def __init__(self, entiers: List[int]) -> None:
        """
        Une chaîne d'entiers est construite à partir d'une liste d'entiers 
        Des 0 et des 1 pour les textes
        Des entiers entre 0 et 255 pour les images
        """
        self.entiers = entiers

    def __repr__(self) -> str:
        """
        On représente la chaîne d'entiers par les entiers séparés par des espaces

        >>> Chaine([1, 0, 1, 1])
        1 0 1 1
        """
        return " ".join([str(entier) for entier in self.entiers])

    def to_texte(self) -> Texte:
        """
        Les cryptosystèmes manipulent des chaines de bits mais les humains veulent du texte
        Cette méthode permet de transformer une trame de caractères codés sur un octet 
        en la chaîne de caractères correspondante.

        >>> Chaine([1, 1, 1, 0, 1, 0, 0, 1]).to_texte()
        é

        À comparer avec :

        >>> chr(0b11101001)
        'é'
        """
        return None

    def to_image(self, larg, haut, chemin="./crypte.png") -> Photo:
        """
        Transforme une Chaîne d'entiers  en une image PIL dont on donne les dimensions 
        en arguments
        """
        # on crée une image vide au départ de la bonne dimension
        im = Image.new(mode = 'L', size = (larg, haut))
        pix = self.entiers
        for x in range(larg):
            for y in range(haut):
                im.putpixel((x,y), pix[y*larg + x])
        im.save(chemin)
        return Photo(chemin)


class Texte:
    """
    On crée une classe Texte principalement pour avoir une méthode 
    permettant d'obtenir la représentation d'une chaîne de caractères sous forme d'une
    chaîne d'entiers
    """

    def __init__(self, texte: str) -> None:
        """
        Une instance de texte est définie à partir de la donnée
        d'une chaîne de caractères
        """
        self.texte = texte

    def __repr__(self) -> str:
        """
        Une instance de Texte est représentée par la chaîne de caractères
        qui la constitue
        """
        return self.texte

    def to_entiers(self) -> Chaine:
        """
        On transforme une instance de Texte en la chaîne d'entiers correspondante.

        >>> Texte('ab').to_entiers()
        0 1 1 0 0 0 0 1 0 1 1 0 0 0 1 0
        """
        return None

class Photo:
    """
    Une instance de Photo est définie à partie du chemin relatif vers un fichier image  
    """
    
    def __init__(self, chemin:str) -> None:
        self.chemin = chemin
        # le mode L correspond à un niveau de gris stocké sur un octet (un entier entre 0 et 255)
        self.image = Image.open(chemin).convert(mode='L')
        self.larg, self.haut = self.image.size 
        # On récupère chaque pixel en parcourant l'image de gauche à droite et de haut en bas
        # Les pixels sont stockés dans un objet Chaine 
        self.to_chaine = Chaine([self.image.getpixel((x, y)) for y in range(self.haut) for x in range(self.larg)])

    def montre(self):
        """
        Affiche l'image avec l'application par défaut
        """
        self.image.show()


class ECB:
    """
    Classe dont les instances sont des cryptosystèmes dépendant de la donnée de leur clé
    sous la forme d'une permutation
    """

    def __init__(self, cle: Perm) -> None:
        """
        Un cryptosystème ECB est défini par la donnée d'une permutation
        On crée un 2nd attibut donnant la taille de la permutation
        """
        self.cle = cle
        self.taille = cle.taille

    def __repr__(self) -> str:
        """
        Représentation d'un cryptosystème en donnant sa clé

        >>>  ECB(Perm(images=[1,0,3,2]))
        ECB de clé : 0 1 3 2
        """
        return f"ECB de clé : {self.cle}"

    def __invert__(self) -> ECB:
        """
        Renvoie la fonction de déchiffrement en utilisant la permutation réciproque.
        Accessible avec l'opérateur unaire ~

        >>> e = ECB(Perm(4))
        >>> e
        ECB de clé : 2 0 3 1
        >>> ~e
        ECB de clé : 1 3 0 2
        """
        return ECB(~(self.cle))

    def __decoupe_en_blocs(self, les_entiers: Chaine) -> List[Chaine]:
        """
        Prend une chaîne d'entiers et la transforme en liste de chaînes d'entiers de
        longueur celle de la permutation en complétant éventuellement par des 0.
        Méthode à usage interne facilitant l'écriture de la fonction chiffre

        >>> e = ECB(Perm(images=[1,0,3,2]))                                                                                                                                          
        >>> e.__decoupe_en_blocs(Chaine([1,2,3,4,5,6,7,8,9,10,11,12,13]))                                                                                                              
        [1 2 3 4, 5 6 7 8, 9 10 11 12, 13 0 0 0]
        """
        return None

    def __permute(self, les_entiers: Chaine) -> List[Chaine]:
        """
        Renvoie la liste des permutations des blocs de longueur celle de la permutation
        construits à partir d'une chaîne d'entiers.

        >>> e = ECB(Perm(images=[1,0,3,2]))                                                                                                                                          
        >>> e.__permute(Chaine([1,2,3,4,5,6,7,8,9,10,11,12,13]))
        [2 1 4 3, 6 5 8 7, 10 9 12 11, 0 13 0 0]
        """
        return None

    def chiffre(self, les_entiers: Chaine) -> Chaine:
        """
        Retourne le message chiffré sous forme de chaîne d'entiers.
        Utilise les sous-méthodes précédentes.

        >>> cle = ????
        >>> ecb = ECB(cle)
        >>> mes = Texte("ananas")
        >>> chaine = ????
        >>> crypte = ecb.chiffre(chaine)
        >>> mes
        ananas
        >>> crypte
        HîRzÂj
        """
        return None

"""
def chiffre_texte(cle: Perm, message: str) -> str:
    ecb = ECB(cle)
    mes = Texte(message)
    chaine = mes.to_entiers()
    crypte = ecb.chiffre(chaine)
    return crypte.to_texte()

def chiffre_image(cle: Perm, image: str) -> str:
    ecb = ECB(cle)
    pic = Photo(image)
    larg, haut = pic.larg, pic.haut
    pic_chaine = pic.to_chaine
    pic_crypte = ecb.chiffre(pic_chaine)
    pic_decrypte = (~ecb).chiffre(pic_crypte)
    #pic.montre()
    pic_crypte.to_image(larg, haut).montre()
    pic_decrypte.to_image(larg, haut).montre()
"""
