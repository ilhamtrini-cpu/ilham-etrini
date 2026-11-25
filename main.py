FICHIER = "contacts.txt"


def sauvegarder_contacts(contacts):
    """Réécrit entièrement contacts.txt."""
    with open(FICHIER, "w", encoding="utf-8") as f:
        for contact in contacts:
            f.write(f"{contact['nom']};{contact['telephone']};{contact['email']}\n")


def charger_contacts():
    """Lit contacts.txt et retourne une liste de dictionnaires."""
    contacts = []
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:
                    parties = ligne.split(";")
                    if len(parties) == 3:
                        contacts.append({
                            "nom": parties[0],
                            "telephone": parties[1],
                            "email": parties[2],
                        })
    except FileNotFoundError:
        pass
    return contacts


def ajouter_contact(contacts):
    """Demande les infos, ajoute le contact et sauvegarde."""
    nom = input("Nom : ").strip()
    telephone = input("Téléphone : ").strip()
    email = input("Email : ").strip()

    if not nom or not telephone or not email:
        print("Tous les champs sont obligatoires.")
        return

    contacts.append({"nom": nom, "telephone": telephone, "email": email})
    sauvegarder_contacts(contacts)
    print("Contact ajouté avec succès.")


def afficher_contacts(contacts):
    """Affiche tous les contacts numérotés."""
    if not contacts:
        print("Aucun contact enregistré.")
        return

    print("\n--- Liste des contacts ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['nom']} | {contact['telephone']} | {contact['email']}")


def supprimer_contact(contacts):
    """Supprime un contact choisi par son numéro et sauvegarde."""
    if not contacts:
        print("Aucun contact à supprimer.")
        return

    afficher_contacts(contacts)

    try:
        numero = int(input("Numéro du contact à supprimer : "))
    except ValueError:
        print("Veuillez entrer des chiffres uniquement.")
        return

    if 1 <= numero <= len(contacts):
        supprime = contacts.pop(numero - 1)
        sauvegarder_contacts(contacts)
        print(f"Contact '{supprime['nom']}' supprimé.")
    else:
        print("Numéro invalide.")


def menu():
    """Boucle principale du programme."""
    contacts = charger_contacts()

    while True:
        print("\n=== Gestionnaire de Contacts ===")
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Supprimer un contact")
        print("4. Quitter")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_contact(contacts)
        elif choix == "2":
            afficher_contacts(contacts)
        elif choix == "3":
            supprimer_contact(contacts)
        elif choix == "4":

            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")


menu()
