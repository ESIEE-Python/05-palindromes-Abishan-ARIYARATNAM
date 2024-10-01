'''
    Vérifie si une chaine passée en paramètre est un palindrome.

'''
#### Fonction secondaire


def ispalindrome(p):
    '''
    Vérifie si une chaine passée en paramètre est un palindrome.

            Parameters:
                    p (str): Chaine de carac

            Returns:
                    Void
    '''
    # votre code ici
    txt = p

    txt = txt.lower()

    x = "àâçèéêëîïôùûüÿ"
    y = "aaceeeeiiouuuy"
    z = r""" .,;:!?…'"«»()[]{}-–_/\\@#&*%"""

    mytable = str.maketrans(x,y,z)

    print(txt.translate(mytable))

    if txt.translate(mytable) == txt.translate(mytable)[::-1]:
        return True
    return False

#### Fonction principale


def main():
    '''
    Vérifie si une chaine passée en paramètre est un palindrome.

    '''
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
