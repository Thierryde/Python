# definit les fonctions du jeu "pendu"

import os
import pickle
from random import choice
from files import *

def recup_scores():
	# cette fonction recup le score si le fichier existe, sinon cree le fichier
	if os.path.exists(nom_fichier_scores):
		#si le fichier existe on le recupere
		fichier_scores = open(nom_fichier_scores, "rb")
		mon_depickler = pickle.Unpickler(fichier_scores)
		scores = mon_depickler.load()
		fichier_scores.close()
	else:
		#si le fichier n existe pas on le cree
		scores = {}
	return scores

def enregistrer_scores(scores):
	# cette fonction enregistre les scores dans le fichier nom_fichier_scores
	# elle recoit en paramaetre le dico des scores

	fichier_scores = open(nom_fichier_scores, "wb")
	mon_pickler = pickle.Pickler(fichier_scores)
	mon_pickler.dump(scores)
	fichier_scores.close()

def recup_nom_joueur():
	# recup le nom du joueur, 3 caracteres minimum et seulement lettre et chiffres
	# le return apres le print appelle la fonction en recursif

	nom_joueur = raw_input("Entrez votre pseudo (3 caracteres minimum) : ")
	if not nom_joueur.isalnum() or len(nom_joueur) < 3:
		print("Ce nom est invalide.")
		return recup_nom_joueur()
	else:
		return nom_joueur

def recup_lettre():
	# recup la lettre saisie par le joueur
	# si ce n'est pas une lettre, appelle la fonction en recursif

	lettre = raw_input("Tapez une lettre : ")
	lettre = lettre.lower()
	if len(lettre) > 1 or not lettre.isalpha():
		print("Ce n'est pas une lettre valide.")
		return recup_lettre()
	else:
		return lettre

def choisir_mot():
	#cette fonction choisit un mot random

	return choice(liste_mots)

def recup_mot_cache(mot_complet, lettres_trouvees):
	#  cette fonction renvoie le mot avec les lettres trouvees

	mot_cache = ""
	for lettre in mot_complet:
		if lettre in lettres_trouvees:
			mot_cache += lettre
		else:
			mot_cache += "*"
	return mot_cache
