QUESTION=[
    {
        "Avez-vous l'intention de quitter le pays après avoir terminé vos études universitaires ?\n1- Oui\n2- Non\n3- Incertain\n\n"
    }   
]



while True:
    fly = input("Avez-vous l'intention de quitter le pays après avoir terminé vos études universitaires ?\n1- Oui\n2- Non\n3- Incertain\n\n")
    try:
        fly = int(fly)
        if 1 <= fly <= 3:
            break
        else:
            print("Veuillez choisir une option valide (1, 2 ou 3).")
    except ValueError:
        print("Veuillez entrer un nombre entier.")
