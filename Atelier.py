#-*- coding: utf-8 -*- 



#grille, ici sous forme de matrices pour representer le jeu dans le debut, milieu et fin de partie
grille_debut_partie = {
    "   ": ["1", "2", "3", "4", "5", "6", "7", "8"],
    "A": [" ", " ", " ", " ", " ", " ", " ", " "],
    "B": ["●", " ", "●", " ", "●", " ", "●", " "],
    "C": [" ", "●", " ", "●", " ", "●", " ", "●"],
    "D": [" ", " ", " ", " ", " ", " ", " ", " "],
    "E": [ " ", " ", " ", " ", " ", " ", " ", " "],
    "F": ["o", " ", "o", " ", "o", " ", "o", " "],
    "G": [ " ", "o", " ", "o", " ", "o", " ", "o"],
    "H": [ " ", " ", " ", " ", " ", " ", " ", " "]}


grille_milieu_partie = {
    "   ": ["1", "2", "3", "4", "5", "6", "7", "8"],
    "A": [" ", " ", " ", " ", " ", "●", " ", " "],
    "B": [" ", " ", "●", " ", "●", " ", " ", " "],
    "C": [" ", "●", " ", "o", " ", " ", " ", " "],
    "D": ["●", " ", "●", " ", "o", " ", "●", " "],
    "E": [" ", "o", " ", " ", "o", " ", " ", "●"],
    "F": [" ", " ", "o", "o", " ", " ", "o", " "],
    "G": [" ", "o", " ", " ", " ", " ", " ", " "],
    "H": [" ", " ", " ", " ", " ", " ", " ", " "]}


grille_fin_partie = {
    "   ": [ "1", "2", "3", "4", "5", "6", "7", "8"],
    "A": [" ", " ", "●", "o", " ", " ", "●", " "],
    "B": [" ", " ", "o", " ", " ", " ", " ", " "],
    "C": [" ", "o", "●", " ", " ", " ", " ", " "],
    "D": [ "●", " ", "o", " ", "●", " ", " ", "●"],
    "E": [" ", " ", " ", "o", " ", "o", " ", " "],
    "F": [ " ", " ", " ", " ", "o", " ", "●", " "],
    "G": [ " ", "o", " ", " ", " ", " ", " ", "●"],
    "H": [ " ", " ", " ", " ", " ", "o", " ", " "]}


#l'equipe "o" peut gagner en sautant le pion en "B3" avec le pion en "C2" pour arriver en "A4"



#Création graphique de la grille 8x8
def afficher_grille(grille) :
    for ligne in grille:
        print(ligne,end='|')
        for colonne in range(0,len(grille[ligne])):
            print(grille[ligne][colonne]  , end= "  |  ")
        print('\n','—' *54 ,sep='')




#Affiche les règles
def affichage_regles():
    print("Les régles : ")
    print("  ")
    print("Vous ne pouvez déplacer que vos pions")
    print("Le but du jeux est de se rendre dans les cages adverses (2 cases)\n")
    print("Un joueur n'a pas le droit de se rendre dans ses propres cages. \n")
    print("Vous ne pouvez deplacer votre pion que dans 4 directions, en haut, en bas, à droite et à gauche (jusqu'à 7 cases max)\n")
    print("Il est interdit de passer la ligne médiane sans effectuer un saut par dessus l'un de ses pions\n")
    print("On peut effectuer un saut si et seulement si un pion de notre équipe est sur la case adjacente et que la case derrière est vide\n")
    print("Le saut peut s'effectuer dans toutes les directions (y compris les diagonales)\n")
    print("Fin des régles. ")
    print("  ")



#Affiche la grille choisit en indiquant les deux joueurs de la grille
def affichage(j1, j2):
    choix=input(("Pour voir la grille de début, tapes 1\n\nPour voir la grille de milieu, tapes 2\n\nPour voir la grille de fin, tapes 3\n\nchoix : "))
    while choix != "1" and choix != "2" and choix != "3":
        choix=input(("Choisissez bien un chiffre ENTRE 1 ET 3 : "))

    if choix=="1":
        print("Voici la grille du début de partie :\n")
        grille = grille_debut_partie
        afficher_grille(grille)
        print("Joueur 1 : ",j1,"\nJoueur 2 : ",j2," \n")
        return grille

    elif choix=="2":
        print("Voici la grille du milieu de partie :\n ")
        grille = grille_milieu_partie
        afficher_grille(grille)
        print("Joueur 1 : ",j1,"\nJoueur 2 : ",j2," \n")
        return grille

    elif choix=="3":
        print("Voici la grille de fin de partie : \n ")
        grille = grille_fin_partie
        afficher_grille(grille)
        print("Joueur 1 : ",j1,"\nJoueur 2 : ",j2," \n")
        return grille



#permet de choisir le pion que vous voulez en début de partie
def choix_du_pion():
    joueur=input("Quel pion choisissez vous ? ( 1 : '●', 2 : 'o' ) : ")
    while joueur != "1" and joueur != "2":
        joueur=input("choisissez bien un chiffre entre 1 et 2 : ")
    if joueur == "1":
        print("Vous êtes le joueur avec le pion : '●'.\n")
        j1, j2 = '●', 'o' 
    elif joueur == "2":
        print("Vous êtes le joueur avec le pion 'o'.\n")
        j1,j2 = 'o', '●'
    return j1, j2



def saisir_coordonnee(grille):
    coordonnee = str(input("Entrez vos coordonnées : "))
    ligne = (coordonnee[0])
    colonne = (coordonnee[1])
    while not (est_au_bon_format(coordonnee) and est_dans_grille(ligne,colonne,grille)):
        print("Veuillez entrer de bonnes coordonnées avec une lettre comprise entre A et H suivis d'un chiffre compris entre 1 et 8 (exemple : A7)")
        coordonnee = str(input("Entrez vos coordonnées : "))
        ligne = (coordonnee[0])
        colonne = (coordonnee[1])
    print("Les coordonneées sont bonnes ! ")
    return ligne,colonne



def est_dans_grille(ligne,colonne,grille) :
     #On peut mettre des minuscules pour éviter de s'embêter
     ligne = ord(ligne)
     colonne = ord(colonne)
     if (65 <= ligne <= 72 or 97 <= ligne <= 104) and 49 <= colonne <= 56 :
         return True
     return False



def est_au_bon_format(coordonnee):
    if len(coordonnee) != 2:
        return False
    elif len(coordonnee)==2:
        ligne = (coordonnee[0])
        colonne = (coordonnee[1])
        ligne = ord(ligne)
        colonne = ord(colonne)
        if 65<=ligne<=90 and 48<=colonne<=57:
            return True
        return False
    
    
    
def choix_pion_a_bouger():
    pion=saisir_coordonnee(grille)
    return pion

def choix_case_aller():
    case_aller=saisir_coordonnee(grille)
    return case_aller


def type_deplacemment():
 # Demande à l'utilisateur de choisir le type de déplacement qu'il veut faire
    print('CHOISISSEZ LE TYPE DE DÉPLACEMENT QUE VOUS VOULEZ FAIRE')
    print('a domicile ou sauter')
    deplacement=input()
    
# Vérifie si l'option choisie est valide
    while deplacement!=('a domicile') or  deplacement!=('sauter'):
        if deplacement == "sauter":
            print("Vous avez choisi de sauter.")
            return deplacement

        elif deplacement == "a domicile":
            print("Vous avez choisi de faire un déplacement a domicile.")
            return deplacement

        else:
            print("Vous n'avez pas choisi une option valide.")
            deplacement=input('CHOISISSEZ LE TYPE DE DÉPLACEMENT QUE VOUS VOULEZ FAIRE')






def mouv_a_dom(grille,pion,case_aller,j1):
    type_mouv=mouv_hori_verti(pion,case_aller)
    c,p=convert_pos(pion)
    c1,p1=convert_pos(case_aller)

    if type_mouv=="hori":
        if verif_camp_joueur(grille,j1,case_aller) == False and verif_case_inter_longue_dist_horizon(grille,pion,case_aller) == True:
            grille[c][p]=' '
            grille[c1][p1]=j1
            return grille
        
    if type_mouv=="verti":
        if verif_camp_joueur(grille,j1,case_aller) == False and verif_case_inter_longue_dis_vertical(grille,pion,case_aller) == True:
            grille[c][p]=' '
            grille[c1][p1]=j1
            return grille
    else:
        return grille

def mouv_sauter(grille,pion,case_aller,j1):
    c1,p1=convert_pos(pion)
    c2,p2=convert_pos(case_aller)
    if verif_case_intermediaire(case_aller,pion,grille,j1)==True and verif_saut_possible(case_aller,pion)==True:
        grille[c1][p1]=' '
        grille[c2][p2]=j1
        return grille
    else:
        return grille
    
def exe_deplacement(grille,pion,case_aller,j1,deplacement):

    if deplacement=='sauter':
        mouv_sauter(grille,pion,case_aller,j1)

    if deplacement=='a domicile':
        
        mouv_a_dom(grille,pion,case_aller,j1)

    return grille

def ask_enchainement():
    print("1 pour enchaine autre pour ne pas faire")
    x=int(input())
    return x==1
    



def tour_j1(grille):
    pion=choix_pion_a_bouger()
    c,p=convert_pos(pion)
    while grille[c][p]!=j1:
        print("le pion ne fait pas parti de votre equipe")
        pion=choix_pion_a_bouger()
        c,p=convert_pos(pion)

    deplacement=type_deplacemment()
    case_aller=choix_case_aller()
    exe_deplacement(grille,pion,case_aller,j1,deplacement)
    if deplacement=='sauter':
        while verif_enchainement_possible(case_aller,pion) == True :
            enchainement=ask_enchainement()
            if enchainement==True:
                pion=case_aller
                case_aller=choix_case_aller()
                exe_deplacement(grille,pion,case_aller,j1,deplacement)
            else:
                break

    afficher_grille(grille)
    return grille

def tour_j2(grille):
    pion=choix_pion_a_bouger()
    c,p=convert_pos(pion)
    while grille[c][p]!=j2:
        print("le pion ne fait pas parti de votre equipe")
        pion=choix_pion_a_bouger()
        c,p=convert_pos(pion)

    deplacement=type_deplacemment()
    case_aller=choix_case_aller()
    exe_deplacement(grille,pion,case_aller,j2,deplacement)
    
    if deplacement=='sauter':
        while verif_enchainement_possible(case_aller,pion) == True :
            enchainement=ask_enchainement()
            if enchainement==True:
                pion=case_aller
                case_aller=choix_case_aller()
                exe_deplacement(grille,pion,case_aller,j2,deplacement)
            else:
                break
    afficher_grille(grille)
    return grille

def mouv_hori_verti(pion,case_aller):

    a,b=convert_pos(pion)
    x,y=convert_pos(case_aller)
    if a==x:
        type_mouv="hori"
    else:
        type_mouv="verti"
    return type_mouv




def fin_jeu(grille):
    for i in grille['A']:
        if i=='o':
            print("C'est o qui gange")
            return False
    for j in grille['H']:
        if j=='●':
            print("C'est ● qui gange")
            return False
    else:
        return True



                    #########################
                    ###LES FONCTIONS TESTS###
                    #########################
                    


def convert_pos(case):
    o,a =case
    a=int(a)-1
    return o,a

def verif_case_vide(grille,case_aller):
    o,a=convert_pos(case_aller)
    return grille[o][a]==' '

def verif_camp_joueur(grille,j1,case_aller):
    o,a=convert_pos(case_aller)
    if j1== 'o' and (o=='A' or 'B' or 'C' or 'D'):
        return False
        
    if j1== '●' and (o=='E' or 'F' or 'G' or 'H'):
        return False
    else:
        return True
    

def verif_saut_possible(case_aller,pion):
    # Récupère les coordonnées des deux cases
    row1, col1 = convert_pos(case_aller)
    row2, col2 = convert_pos(pion)
    ordoné1 = ord(row1) 
    ordoné2 = ord(row2)

    
    # Calcule les différences en x et y
    dx = abs(ordoné1 - ordoné2)
    dy = abs(col1 - col2)
    
    # Vérifie si les deux cases partagent une arête horizontale, verticale ou diagonale et si la distance entre elles est de 2 cases
    if (dx == 0 and dy == 2) or (dx == 2 and dy == 0) or (dx == 2 and dy == 2):
        return True
    
    return False



def verif_case_intermediaire(case_aller,pion,grille,j1):
    # Récupère les coordonnées des deux cases et la case intermédiaire
    row1, col1 = convert_pos(case_aller)
    row2, col2 = convert_pos(pion)
    row3=chr(abs(ord(row1)+ord(row2))//2)
    col3=abs(col1+col2)//2

    # Vérifie si la case intermédiaire contient un pion allier
    if grille[row3][col3]==j1:
        print("le saut est possible bonne case intermediaire \n")
        return True
    else:
        print("le saut est impossible mauvaise case intermediare \n")
        return False
    
def verif_case_inter_longue_dist_horizon(grille,pion,case_aller):
    row1, col1 = convert_pos(case_aller)
    row2, col2 = convert_pos(pion)
    col1=(col1)-1
    col2=(col2)-1
    if col1>col2:
        for i in range(col1,col2):
            if grille[row1][i]!=' ':
                return False
        else:
            return True
    else:
        for i in range(col2,col1):
            if grille[row1][i]!=' ':
                return False
        else:
            return True

def verif_case_inter_longue_dis_vertical(grille,pion,case_aller):
    row1, col1 = convert_pos(case_aller)
    row2, col2 = convert_pos(pion)
    col1=(col1)-1
    col2=(col2)-1
    a=index_pion(case_aller)
    b=index_pion(pion)

    if a>b:
        for i in range(b,a):
            if grille[ligne[i]][col1]!=' ':
                return False
        else:
            return True
    else:
        for i in range(a,b):
            if grille[ligne[i]][col1]!=' ':
                return False
        else:
            return True



ligne=['A','B','C','D','E','F','G']

def index_pion(pion):
    # renvoie l'index du pion choisit
    row1, col1 = pion
    for x in range (len(ligne)):
        if row1==ligne[x]:
            return x
        


def verif_enchainement(grille,j1,case_aller,pion):
    pos_enchainemement=[]
    # Récupère la case de départ de l'enchaînement
    case_depart_enchainement=case_aller
    x,y=convert_pos(case_depart_enchainement)
    a,b=convert_pos(pion)
    pos=ord(a)
    i=index_pion(case_depart_enchainement)

    # Vérifie si le saut vers le haut est possible
    if (i) > 1 and grille[(ligne[i-1])][y] == (j1) and grille[(ligne[i+1])][y]==' ':
        pos_enchainemement.append(('haut'))

    # Vérifie si le saut vers le bas est possible
    if (i) <5  and grille[(ligne[i+1])][y] == j1 and grille[(ligne[i+2])][y]==' ':
        pos_enchainemement.append(('bas'))

    # Vérifie si le saut vers la gauche est possible
    if y > 1 and grille[x][y] == (j1)  and grille[x][y-2] == ' ':
        pos_enchainemement.append(('gauche'))

    # Vérifie si le saut vers la droite est possible
    if y < 5 and  grille[x][y+1]!=(j1) and grille[x][y+2] == ' ':
        pos_enchainemement.append(('droite'))

    # Verif diagonale
    # Vérifie si le saut en diagonale haut-gauche est possible
    if i > 1 and y > 1 and grille[ligne[i-1]][y-1] == j1 and grille[ligne[i-2]][y-2] == ' ':
        pos_enchainemement.append('haut-gauche')

    # Vérifie si le saut en diagonale haut-droite est possible
    if i > 1 and y < 5 and grille[ligne[i-1]][y+1] == j1 and grille[ligne[i-2]][y+2] == ' ':
        pos_enchainemement.append('haut-droite')

    # Vérifie si le saut en diagonale bas-gauche est possible
    if i < 5 and y > 1 and grille[ligne[i+1]][y-1] == j1 and grille[ligne[i+2]][y-2] == ' ':
        pos_enchainemement.append('bas-gauche')

    # Vérifie si le saut en diagonale bas-droite est possible
    if i < 5 and y < 5 and grille[ligne[i+1]][y+1] == j1 and grille[ligne[i+2]][y+2] == ' ':
        pos_enchainemement.append('bas-droite')

    return pos_enchainemement


def verif_enchainement_possible(case_aller,pion):
    pos_enchainement=verif_enchainement(grille,j1,case_aller,pion)
    return len(pos_enchainement)>0


                    
                    
#Cette fonction teste les coordonnees pour voir si c'est le bon format (lettre suivit d'un chiffre)
def test_est_au_bon_format():
    assert est_au_bon_format("Y9") == True, 'une lettre est un chiffre'
    assert est_au_bon_format("D7") == True, 'une lettre est un chiffre'
    assert est_au_bon_format("  ") == False, 'vide'
    assert est_au_bon_format("AZ98I") == False, 'trop de caracteres'
    assert est_au_bon_format("8A") == False, 'Un chiffre est une lettre'
    assert est_au_bon_format("22") == False, 'Deux chiffres'
    assert est_au_bon_format("DG") == False, 'Deux lettres'
    
    
    
#fonction de test pour verifier si les coordonnees sont au bon format
def test_est_dans_grille():
    assert est_dans_grille("A","2", grille_debut_partie)==True, "Bonne coordonnée"
    assert est_dans_grille("A","9",grille_fin_partie)==False, "Valeur sup"
    assert est_dans_grille("G","6",grille_fin_partie)==True, "Bonne coordonnée"
    assert est_dans_grille("Q","9",grille_milieu_partie)==False, "Coordonnée trop grande"
    assert est_dans_grille("9","9",grille_debut_partie)==False, "Mauvaise coordonnée"

    
#Fonction de test pour lancer les differents tests
def tests():
    print(" ")
    print("Debut des tests ! ")
    test_est_au_bon_format()
    test_est_dans_grille()
    print("Les testes sont bons ! ")
    print(" ")



                    ####################
                    ###CODE PRINCIPAL###
                    ####################
                    
                    
                  
print("————————————————————JEU DEMETER————————————————————")              
      
#demande a l'utilisateur s'il veut afficher les regles puis lancer les tests      
regle = "blabla"
while  regle != "oui" and  regle != "non":
    regle = str.lower(input("Voulez vous afficher les regles (plus les tests) ? (Oui/Non) :"))
if regle == "oui":
    affichage_regles()
    tests()



j1, j2 = choix_du_pion()
grille = affichage(j1, j2)
def main():
    i=0
    while fin_jeu(grille)==True:
        print("tour numero",i, end=" ")
        print("c'est a ",j1,"de jouer")
        tour_j1(grille)
        print("c'est a ",j2,"de jouer")
        tour_j2(grille)
        i+=1

    return grille

main()