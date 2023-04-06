from typing import List
from urllib.request import urlretrieve
url_mousq: str = "https://www.gutenberg.org/cache/epub/13951/pg13951.txt"

urlretrieve(url_mousq, 'mousq.txt')
fic: str = open('mousq.txt', 'r').read()

def cesar(clair: str, cle: int) -> str:
    chif = ""
    dec = ord('A')
    for car in clair:
        new_code = dec + ((ord(car) + cle - dec ) % 26)
        chif += chr(new_code) if 0x41 <= ord(car) <= 0x41 + 26 else car
    return chif

mm = "VENI, VIDI, VICI"
rot13 = lambda x: cesar(x, 13)
#print(rot13(rot13(mm)))
    


def rot47(clair: str) -> str:
    chif = ""
    dec = 0x21
    amp = 0x7f - dec
    for car in clair:
        new_code = dec + ((ord(car) + 47 - dec) % amp)
        chif += chr(new_code) if 33 <= ord(car) <= 126 else car 
    return chif

#print(rot47("ROT47 is the easiest and yet powerful cipher! ROT47 basically makes text unreadable and does not require addtional space."))

def rotx(clair: str, cle: int) -> str:
    chif = ""
    dec = 0x20
    amp = 0x1f0e0 - dec
    for car in clair:
        new_code = dec + ((ord(car) - dec + cle) % amp)
        chif += chr(new_code) if 0x20 <= ord(car) <= 0x1f0df else car
    return chif

#m = "Trahir qui disparut, dans La disparition, ravirait au lisant subtil tout plaisir. Motus donc, sur l’inconnu noyau manquant - « un rond pas tout à fait clos finissant par un trait horizontal » -, blanc sillon damnatif où s’abîma un Anton Voyl, mais d’où surgit aussi la fiction. Disons, sans plus, qu’il a rapport à la vocalisation. L’aiguillon paraîtra à d’aucuns trop grammatical. Vain soupçon : contraint par son savant pari à moult combinaisons, allusions, substitutions ou circonvolutions, jamais G.P. n’arracha au banal discours joyaux plus brillants ni si purs. Jamais plus fol alibi n’accoucha d’avatars si mirobolants. Oui, il fallait un grand art, un art hors du commun, pour fourbir tout un roman sans ça ! "

m = """Il est toujours assez délicat de vouloir utiliser une attaque statistique à l'aide d'un texte trop petit.
Mais cet exercice ne s'adresse pas à n'importe qui ! Non, si vous cherchez cet exercice, c'est que vous faites partie de l'élite. Oui, nous osons le dire : vous êtes l'espoir de l'humanité ! Vous avez choisi de poursuivre l'étude de l'informatique en Terminale. Quel noble choix ! Maintenant je dois écrire un peu ce qui me viens par la tête pour remplir un peu. Vous pensiez sûrement trouver un texte plus intéressant à lire. 
Je le déplore autant que vous. Je n'aime pas parler pour ne rien dire. On pourrait se dire : ça y est ! Il a enfin assez écrit comme ça. Il va trouver le temps long.
Mais non. Il fait pourtant beau dehors en cette période de confinement. Mais justement. Pourquoi vouloir sortir. D'ailleurs c'est impossible. Bon, pour en revenir à notre problème, il ne faut pas non plus s'attendre à recevoir de longs messages donc il faut bien trouver un moyen pour affiner l'attaque. N'oublions pas qu'il s'agit d'un chiffrement à décalage.
"""


with open("./rotXcrypte.txt","w+") as rotX:
    rotX.write(rotx(m, 0x1f0))

with open("./rotXcrypte.txt","r") as rotX:
    crypte = rotX.read()

def stat(mes: str) -> list:
    dico = {}
    for lettre in mes:
        if lettre in dico:
            dico[lettre] += 1
        else:
            dico[lettre] = 1
    return sorted(dico, key=lambda x: dico[x], reverse=True)

#stat_chif = stat(rotx(m, 0x1f0))

#stat_mousq = stat(fic)

#print(stat_chif)
#print(stat_mousq)

def remplace(origine: str, etalon: str) -> str:
    # Les fréquences du message et du texte de référence
    s_origine = stat(origine)
    s_etalon  = stat(etalon)
    # la taille minimum
    mini = min(len(s_origine), len(s_etalon))
    # on crée le dictionnaire de correspondance chiffré -> référence
    dic = {}
    for i in range(mini):
        dic[ s_origine[i] ] = s_etalon[ i ]
    # Pour traduire, on parcourt chaque caractère et on le remplace par sa traduction 
    trad = ""
    for lettre in origine:
        trad += dic[lettre]
    return trad

#print(remplace(crypte, fic))

def guess(origine: str, etalon: str) -> str:
    s_origine = stat(origine)
    s_etalon  = stat(etalon)
    dec = ord(s_origine[0]) - ord(s_etalon[0])
    print(dec)
    return rotx(origine, -dec)

a = guess(crypte, fic)

print(a)


    
