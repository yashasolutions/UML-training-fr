mport datetime

class bibliotheque:
    def __init__(self) -> None:
        pass

    def add_adherent():
        print("Ajouter un adherent")

    def del_adherent():
        print("Enlever un adherent")

    def add_doc():
        print("Ajouter un document")


class adherent:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def emprunter_livre():
        print("Emprunter un livre")

    def rendre_livre():
        print("Rendre un livre")

class emprunte:
    def __init__(self) -> None:
        self.date_emprunt = datetime.datetime.now()
        self.date_retour = self.date_emprunt + datetime.timedelta(days=15)
        
    def prolonger_retour(self, nbr_jour):
        self.date_retour = self.date_emprunt + datetime.timedelta(days=nbr_jour)

class livre:
    def __init__(self) -> None:
        self.disponnible = True
    
    def empruntable(self):
        if self.disponnible == True:
            return True
        else:
            return False


class document:
    def __init__(self, dessinateur):

class bd:
    def __init__(self, dessinateur):

        

