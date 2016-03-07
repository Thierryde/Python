from files import *
from functions import *

scores = recup_scores()

joueur = recup_nom_joueur()

if joueur not in scores.keys():
	scores[joueur] = 0

continuer_partie = 'y'

while continuer_partie != 'n':
	print("Joueur {0}: {1} points".format(joueur, scores[joueur]))
	mot_a_trouver = choisir_mot()
	lettres_trouvees = []
	mot_trouve = recup_mot_cache(mot_a_trouver, lettres_trouvees)
	nb_chances = nb_vies
	while mot_a_trouver != mot_trouve and nb_chances > 0:
		print("Mot a trouver {0} (encore {1} chances".format(mot_trouve, nb_chances))
		lettre = recup_lettre()
		if lettre in lettres_trouvees:
			print("Lettre deja choisie !")
		elif lettre in mot_a_trouver:
			lettres_trouvees.append(lettre)
			print("Bien joue !")
		else:
			nb_chances -= 1
			print("Rate, cette lettre n'est pas presente")
		mot_trouve = recup_mot_cache(mot_a_trouver, lettres_trouvees)

	if mot_a_trouver == mot_trouve:
		print("Felicitations ! Vous avez trouve le mot {0}.".format(mot_a_trouver))
	else:
		print("Pendu !! Vous avez perdu.")

	scores[joueur] += nb_chances + 1

	continuer_partie = input("Souhaitez vous continuer la partie? (y/n) ?")
	continuer_partie = continuer_partie.lower()

enregistrer_scores(scores)

print("Vous finissez la partie avec {0} points.".format(scores[joueur]))