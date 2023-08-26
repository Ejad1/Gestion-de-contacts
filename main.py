import os
from fpdf import FPDF


# Mon programme de gestion de contacts en utilisant la POO

# Définition de la classe contact
class Contact:
    def __init__(self, nom, prenom, description, numero):
        self.nom = nom
        self.prenom = prenom
        self.description = description
        self.numero = numero

    def affichage(self):
        print(f'{self.nom} {self.prenom} : {self.numero} \nDescription du contact : {self.description}')


class GestionnaireContacts:
    def __init__(self):
        self.contacts = []

    def ajouter_contact(self, contact):
        self.contacts.append(contact)

    def sauvegarder_contacts_pdf(self, nom_fichier):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for contact in self.contacts:
            pdf.cell(200, 10, txt="Nom: " + contact.nom, ln=True)
            pdf.cell(200, 10, txt="Prénom: " + contact.prenom, ln=True)
            pdf.cell(200, 10, txt="Description: " + contact.description, ln=True)
            pdf.cell(200, 10, txt="Téléphone: " + str(contact.numero), ln=True)
            pdf.cell(200, 10, txt="-" * 20, ln=True)

        pdf.output(nom_fichier)

    def post_contacts(self):
        for monContact in self.contacts:
            monContact.affichage()


# Exécution du code
if __name__ == '__main__':
    rep = True

    while rep:
        mon_gestionnaire = GestionnaireContacts()

        nom_contact = input('Veuillez entrer le nom du contact : ')
        prenom_contact = input('Entrer le prénom du contact : ')
        description_contact = input('Entrer une description du contact : ')
        numero_contact = int(input('Numéro du contact : '))

        nouveau_contact = Contact(nom_contact, prenom_contact, description_contact, numero_contact)

        mon_gestionnaire.ajouter_contact(nouveau_contact)

        fichier_pdf = "contacts.pdf"
        mon_gestionnaire.sauvegarder_contacts_pdf(fichier_pdf)
        print(f"Contacts sauvegardés dans {fichier_pdf}")

        choix = input('Voulez-vous continuer ? Entrer O si oui : ')
        if choix != 'O':
            rep = False

os.system("pause")
