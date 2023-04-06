"""

a) permutation = perm + len bloc mais on peux utiliser seulement la permutation
b) pour dechiffrer ce message, on peux faire un tableau ou alors une liste en permutant chacun des id

Partie B

# 1
def permute(self, xs: List[int]) -> List[int]:
 return [xs[i] for i in self.images]

# 2a
inverse[image] = antécédent

# 2b
def __invert__(self) -> Perm:
 inverse = [0]*self.taille
 for antecedent, image in enumerate(self.images):
 inverse[image] = antecedent
 return Perm(taille = self.taille, images = inverse
# 3

#4 
def to_entiers(self) -> Chaine:
 res: List[int] = []
 for c in self.texte:
 cb = [int(entier) for entier in bin(ord(c))[2:]]
 res += ([0] * (8-len(cb)) + cb)
return Chaine(res)

#5 
def to_texte(self) -> Texte:
 entiers: List[int] = self.entiers
 assert set(entiers) == {0,1}, "On ne peut transformer en 
texte que des chaînes de bits (0 ou 1)"
 reste: int = len(entiers) % 8 
 nb_octets: int = len(entiers) // 8
 comp: int = 8 - reste if reste > 0 else 0
 # On complète éventuellement par des 0 s’il manque
 # des entiers pour faire des “paquets de 8”
 entiers += [0] * comp
 # On fabrique une liste de chaînes d’entiers de longueur 8
 # du type [«10101100», «00011010»,...]
 octets: List[str] = [
 "".join([str(b) for b in entiers[ i*8 : (i+1) * 8 ]]) 
for i in range(nb_octets)]
 # On concatène alors tous les octets pour former une 
unique chaîne de caractères
 # et on en fait une instance de la classe Texte
 return Texte("".join([chr(int(octet, 2)) for octet in oc-
tets]))

#6
def __decoupe_en_blocs(self, les_entiers: Chaine) -> List[Chaine]:
 n: int = self.taille
 reste: int = len(les_entiers.entiers) % n
 bs: List[int] = les_entiers.entiers + [0] * (0 if reste 
== 0 else n - reste)

def __permute(self, les_entiers: Chaine) -> List[Chaine]:
 return [Chaine(self.cle.permute(bloc.entiers)) for bloc 
in self.__decoupe_en_blocs(les_entiers)]

  def chiffre(self, les_entiers: Chaine) -> Chaine:

ents = []
 for bloc in self.__permute(les_entiers):
 for entier in bloc.entiers:
 ents.append(entier)
 return Chaine(ents)
"""

#######################################################


# Exercice 8
#1
def rot47(text):
    return ''.join(chr(33 + ((ord(char) + 14) % 94)) if 33 <= ord(char) <= 126 else char for char in text)

print(rot47("Bonjour tout le monde !"))



#2
# ROT47 c'est un peu comme un code cesar aménager : on decale de maniere circulaire les caractere 47 fois ( comme vu dans la fonction précédente ). Donc en toute logique, pour le décodé, on décale encore 47 fois. 

#3a
#il y a 127166 possibilité donc 127166 essaie à faire pour brute force

#3b
# On fait une analyse fréquencielle

#3c
def stat(mes: str) -> list:
  dico = {}
  for lettre in mes:
   if lettre in dico:
     dico[lettre] += 1
   else:
     dico[lettre] = 1
  return sorted(dico, key=lambda x: dico[x], reverse=True)

#3d 
def remplace(origine: str, etalon: str) -> str:
    freq_origine = stat(origine)
    freq_etalon = stat(etalon)
    dico_remplacement = {freq_origine[i]: freq_etalon[i] for i in range(len(freq_origine))}
    return ''.join([dico_remplacement.get(char, char) for char in origine])

#3e
def decrypt(message: str, etalon: str) -> str:
    # Analyse de fréquence du message chiffré
    freq = stat(message)
    most_freq = freq[0]
    
    # Calcul du décalage à appliquer
    shift = (ord(most_freq) - ord('e')) % 26
    
    # Déchiffrement du message
    decrypted = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decrypted += char
    
    return decrypted

#3f 
# ROT47 sera utiliser a des fins d'obsfuscation pour encoder des données qui ne seront pas sensible car même en utilisant un chiffrement par ROTx, la methode n'est pas sécurisé et cassable facilement

