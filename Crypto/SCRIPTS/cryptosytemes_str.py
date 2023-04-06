from __future__ import annotations
from typing import List


class Perm:
    """ Groupe des permutations, la loi étant la composition """

    def __init__(self, *args) -> None:
        """ Permutation définie par la liste des images de [0,1,2,...] """
        self.images = "".join([str(bit) for bit in args])

    def __repr__(self) -> str:
        """représente les images de la permutation"""
        return " ".join([image for image in self.images])

    def __len__(self) -> int:
        """longueur de la permutation obtenue avec len"""
        return len(self.images)

    #def __inv__(self) -> Perm :
   #     """ permutation réciproque de self """
   #     im = self.images
   #     n = len(im)
   #     return [couple[1] for couple in sorted( zip(im, range(n)) )]

    def permute(self, xs: str) -> str :
        """ si xs = [xs[0], xs[1], xs[2],...], p.permute(xs) = [xs[p(0)], xs[p(1)], xs[p(2)],...] """
        return "".join([xs[int(i)] for i in self.images])

    

class ChaineBits:

    def __init__(self, bits: str) -> None:
        self.bits = bits

    def __repr__(self) -> str:
        return self.bits
        
    def to_texte(self) -> Texte:
        bits = self.bits
        reste = len(bits) % 8
        nb_octets = len(bits) // 8
        comp = 8 - reste if reste > 0 else 0
        bits += "0"*comp
        return Texte("".join([chr(int(bits[i*8:(i+1)*8], 2)) for i in range(nb_octets)]))
    
class Texte:

    def __init__(self, texte: str) -> None:
        self.texte = texte

    def __repr__(self) -> str:
        return f"Texte({self.texte})"
        
        
    def to_bits(self) -> ChaineBits:
        res = ""
        for c in self.texte:
            cb = bin(ord(c))[2:]
            res += ("0"*(8-len(cb)) + cb)
        return ChaineBits(res)


class ECB:

    def __init__(self, cle: Perm) -> None:
        self.cle = cle
        self.len = len(cle)

    def __repr__(self) -> str:
        return f"ECB({cle})"
        
    def __decoupe_en_blocs(self, les_bits: ChaineBits) -> List[ChaineBits]:
        n = self.len
        reste = len(les_bits.bits) % n
        bs = les_bits.bits + "0"*(0 if reste == 0 else n - reste)
        return [ ChaineBits(bs[i*n:(i+1)*n]) for i in range(len(bs)//n) ]

    def __permute(self, les_bits: ChaineBits) -> List[ChaineBits]:
        """renvoie la liste des permutations des blocs construits à partir d'une liste de bits"""
        return [ChaineBits(self.cle.permute(bloc.bits)) for bloc in self.__decoupe_en_blocs(les_bits)]

    def chiffre(self, les_bits: ChaineBits) -> ChaineBits:
        """retourne le message chiffré sous forme de chaîne de bits""" 
        return ChaineBits("".join([bit for bloc in self.__permute(les_bits) for bit in bloc.bits]))




cle = Perm(0,1,2,3,5,6,4)
ecb = ECB(cle)
mes = Texte("bbbbbbbbbbbbbbbbbbbbbbbb")
chaine = mes.to_bits()
crypt = ecb.chiffre(chaine)
print(cle)
print(ecb)
print(mes)
print(chaine)
print(chaine.to_texte())
print(crypt)
print(crypt.to_texte())
