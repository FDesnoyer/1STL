import random as rnd

def joueurA(n):
    perdu=True
    k=rnd.randint(1,n)
    score=0
    while perdu:
        score=score+1
        prop=int(input('Votre proposition?'))
        perdu=not((prop==k))
        if prop<k:
            print('Plus grand')
        else:
            if prop>k:
                print('Plus petit')
    print(f"Vous avez trouvé le nombre {k} en {score} essais")
    if 2**score>n:
        print("Pas top!!!")
    else:
        print("Pas mal :-/")
    return score

def joueurB(n):
    print(f"Choisissez un nombre de 1 à {n}, je vais le deviner!")
    print("Lorsque que je vous fais une proposition, répondez-moi Plus, Moins ou Gagné on y va?")
    score=0
    a=1
    b=n
    k=(a+b)//2
    print(k)
    test=input('Alors?')
    encore=not((test=='Gagné')or(test=='gagné'))
    while encore:
        score=score+1
        if (test=='Plus' or test=='plus'):
            a=k
            k=(a+b)//2
        else:
            if ((test=='moins')or(test=='Moins')):
                b=k
                k=(a+b)//2
            else:
                print('Merci de répondre')
        print(f"Je propose {k}")
        test=input('Alors?')
        encore=not((test=='Gagné')or(test=='gagné'))
    print(f"J'ai gagné en {score} coups!!!")
    if 2**score>n:
        print('Peut mieux faire')
    else:
        print("Et j'ai la grande classe...")
    return score