#!/usr/bin/env python3.4

# -*-coding:utf-8-*-

import os

from tkinter import *

def multiplier_par_3(nbAMultiplier=0):

    nbAMultiplier = nbAMultiplier * 3

    return nbAMultiplier


if __name__ == "__main__":

    #Création d'une fenêtre

    fenetre = Tk();
    fenetre.title('Ma fenetre')
    fenetre['bg']='bisque' #Couleur de fond    
   
    #####################################################################

    #Création d'une ligne de texte
    textField001 = Label(fenetre, text="Salut les ZEROS")

    #Création d'un bouton
    button001 = Button(fenetre, text="Bt1", command = fenetre.quit)
    button002 = Button(fenetre, text="Bt2", command = fenetre.quit)

    #Création d'un champ de saisie
    #Création d'une variable Tkinter, correspondant à la chaîne de caractères saisis
    var_texte = StringVar()
    inputText001 = Entry(fenetre, textvariable = var_texte, width=20)

    #Création d'une case à cocher
    var_caseACocher = IntVar()
    checkBox001 = Checkbutton(fenetre, text = "Cochez-moi", variable = var_caseACocher)

    #Création de case "radio"
    var_choix = StringVar()

    radioBox001 = Radiobutton(fenetre, text = "Rouge", variable = var_choix, value = "rouge")
    radioBox002 = Radiobutton(fenetre, text = "Vert", variable = var_choix, value = "vert")
    radioBox003 = Radiobutton(fenetre, text = "Bleu", variable = var_choix, value = "bleu")

    #Création d'une liste
    liste001 = Listbox(fenetre)
    liste001.insert(END, "Agen")
    liste001.insert(END, "Sète")
    liste001.insert(END, "Perpignan")
    

    #####################################################################

    #Insertion des objets dans la fenêtre
    
    textField001.pack(side = "top", fill = X)
    button001.pack(side = "top", fill = X)
    button002.pack(side = "top", fill = X)
    inputText001.pack(side = "top", fill = X)
    checkBox001.pack(side = "top", fill = X)
    radioBox001.pack(side = "top", fill = X)
    radioBox002.pack(side = "top", fill = X)
    radioBox003.pack(side = "top", fill = X)
    liste001.pack(side = "top", fill = X)

    #####################################################################

    #Récupérer les valeurs...

    #Choix radio
    var_choix.get()

    #####################################################################


    #Boucle Tkinter, active jusqu'à la fermeture de la fenêtre
    fenetre.mainloop()

        
    #####################################################################

    #Affichage des valeurs

    print(var_choix.get())
    print ("Coché", var_caseACocher)
    


