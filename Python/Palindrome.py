import unidecode as ud


def palindrome(string):
  if len(string) == 0:
    return False
    
  for i in range(len(string)):
    if string[i]!= string[len(string)-i-1]:
      return False
  if string[0] == string[len(string)-1]:
    return True
  return False

def main():
  string = input("Mot : ")
  if palindrome(string.lower()) == True and palindrome(ud.unidecode((string.replace(" ",""))).lower()) == True:
    print("Palindrome complet")
    return True
  if palindrome(ud.unidecode((string.replace(" ",""))).lower()):
    print("Palindrome partiel")
    return True
  else:
    return False

if __name__ == "__main__":
  main()


"""
def is_palindrome(s):
  # Supprimez les espaces et les caractères spéciaux de la chaîne
  s = ''.join(e for e in s if e.isalnum())
  # Normalisez la chaîne pour supprimer les accents
  s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore')
  # Mettez la chaîne en minuscule
  s = s.lower()
  # Inversez la chaîne
  s_rev = s[::-1]
  # Compare la chaîne originale et la chaîne inversée
  if s == s_rev:
    return True
  else:
    return False  


"""