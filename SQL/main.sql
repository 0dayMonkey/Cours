/*




"""
SE TESTER
QUIZ 

1 - Vocabulaire des bases de données

1) b,c
2) b
3) c

2 - Clés et contraintes d’intégrité
1) b
2) c,d

3 - Conception de bases de données
1) c
2) a
3) a,d 
4) c



4) 
a) Oui on peux, on vois par exemple deux fois le meme numero de commande avec deux sandwich different ( même commande, plusieurs sandwich) - voir la question (e)
b) 

Ssandwich = (S1,S2)
((Nom_Sandwich,String),(Prix,Float))))

Sclient = (A1,A2,A3,A4)
((Nom,String),(Prénom,String),(Adresse,String),(NumeroClient,Integer))

c) La table Sandwich ne compte que des clé primaire ( uniques a celui ci, qui défini l'item qui sera utiliser plus tard )

d) La table Client compte une clé primaire, Id_Client qui va permettre de differencier chque client.
La table commande quand a elle contient des clé etrangere, ' Numero_Client' qui viens de la table Client et ' Nom_Sandwich ' qui viens de la table Sandwich

e)  Non elle ne semble pas si bien modélisée car lorsqu'on commande plusieurs sandwich
 
 _____________________________________________________
|                 |               |                   |
|  Nom_Sandwich   |      Prix     |    Id_sandwich    |
|_________________|_______________|___________________|
|                 |               |                   |
|   Italien       |      2,30     |    1              |
|_________________|_______________|___________________|
|                 |               |                   |
|   Americain     |      5,30     |    2              |
|_________________|_______________|___________________|
|                 |               |                   |
|   Cheeseburger  |      2,70     |    3              |
|_________________|_______________|___________________|
|                 |               |                   |
|   Zambon        |      600      |    4              |
|_________________|_______________|___________________|


 
 ______________________________________________________________________________________
|           |           |           |           |           |            |             |
|NumCommande| NumClient |  Sandwich | Quantité  |  Adresse  |    Date    |    Prix     |
|___________|___________|___________|___________|___________|____________|_____________|
|           |           |           |           |   28 rue  |            |             |
|     1     |     42    |     1     |     1     |  de Paul  | 25/03/2023 |    2,30€    |
|___________|___________|___________|___________|___________|____________|_____________|
|           |           |           |           |   1 Bd    |            |             |
|     2     |     56    |    1,3    |    2,3    |   Damso   | 26/03/2023 |    5€       |
|___________|___________|___________|___________|___________|____________|_____________|


où Sandwich serait un n-uple avec l'identifiant du sandwich tout comme la quantité.
Le prix se baserai sur l'identifiant du tableau sandwich ( somme des prix des identifiants dans les n-uples )


5) 
((UtilisateurID,string),(NomUtilisateur,string),(AdresseEmail,string),(MotDePasse,string),(DateInscription,date),(Droits,chaine(administrateur,modérateur,utilisateur)))





Exercice n°6

Users ((id_user, int), (Pseudonyme, str), (Adresse_email, str), (Date_enregistrement, date), (Droits, str))
Posts ((id_post, int), (Titre, str), (Contenu, str),(Date_message, date), (Heure, heure), (id_user, int))
Albums ((id_album, int), (Titre, str), (id_user, int))
Albums_post((id_album, int), (id_post, int))

7) 

a. 
((Nom, str), (Prénom, str), (Date_de_naissance, date), (Classe, int), (Option1, str), (Option2, str), (Option3, str))

b. Non aucune clé primaire
c. contrainte de relation et d'attribut vide
d. S(Élèves) = ((id_eleve, int), (Nom, str), (Prénom, str), (ddn, date), (Classe, str))
S(Options) = ((id_eleve, ), (Option, ))


"""

*/
CREATE TABLE elv (
    id_eleves INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    math INTEGER NOT NULL,
    anglais INTEGER NOT NULL,
    info INTEGER NOT NULL,
    classe TEXT NOT NULL
);

INSERT INTO elv (nom, math, anglais, info, classe)
VALUES ('Joe', 14, 17, 18,"TA"), ('Zoe', 19, 15, 17,"TB");



CREATE TABLE IF NOT EXISTS Eleves (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
   prenom TEXT,
   nom TEXT,
   nais TEXT,
   adr TEXT,
   ville TEXT,
   cp TEXT,
   email TEXT
 );  

/*
Produit(NumProd, NomProd, Conditionnement, Volume, Age)
Employé(NumEmp, NomEmp, PrénomEmp, DateEmbauche)
Fournisseur(NumFourn, NomFourn, Ville, Pays)
Catalogue(NumFourn, NumProd, Prix, Stock)
Commande(NumProd, NumEmp, NumFourn, Date, Qté)

Exercice n°1 :

1) 

Table Produit:

    Clé primaire: NumProd

Table Employé:

    Clé primaire: NumEmp

Table Fournisseur:

    Clé primaire: NumFourn

Table Catalogue:

    Clé primaire: (NumFourn, NumProd)
    Clé étrangère: NumFourn réfère à NumFourn dans la table Fournisseur
    Clé étrangère: NumProd réfère à NumProd dans la table Produit

Table Commande:

    Clé étrangère: NumProd réfère à NumProd dans la table Produit
    Clé étrangère: NumEmp réfère à NumEmp dans la table Employé
    Clé étrangère: NumFourn réfère à NumFourn dans la table Fournisseur

2) Requetes pour creer les tables du schema 

*/
CREATE TABLE Produit (
  NumProd INT PRIMARY KEY,
  NomProd VARCHAR(255),
  Conditionnement VARCHAR(255),
  Volume INT,
  Age INT
);

CREATE TABLE Employé (
  NumEmp INT PRIMARY KEY,
  NomEmp VARCHAR(255),
  PrénomEmp VARCHAR(255),
  DateEmbauche DATE
);

CREATE TABLE Fournisseur (
  NumFourn INT PRIMARY KEY,
  NomFourn VARCHAR(255),
  Ville VARCHAR(255),
  Pays VARCHAR(255)
);

CREATE TABLE Catalogue (
  NumFourn INT,
  NumProd INT,
  Prix INT,
  Stock INT,
  PRIMARY KEY (NumFourn, NumProd),
  FOREIGN KEY (NumFourn) REFERENCES Fournisseur(NumFourn),
  FOREIGN KEY (NumProd) REFERENCES Produit(NumProd)
);

CREATE TABLE Commande (
  NumProd INT,
  NumEmp INT,
  NumFourn INT,
  Date DATE,
  Qté INT,
  FOREIGN KEY (NumProd) REFERENCES Produit(NumProd),
  FOREIGN KEY (NumEmp) REFERENCES Employé(NumEmp),
  FOREIGN KEY (NumFourn) REFERENCES Fournisseur(NumFourn)
);



-------------------- INSERT -------------------- 

INSERT INTO Fournisseur (NumFourn, NomFourn, Ville, Pays)
VALUES (1, 'Fournisseur 1', 'Paris', 'France'),
       (2, 'Fournisseur 2', 'Londres', 'Royaume-Uni'),
       (3, 'Fournisseur 3', 'Berlin', 'Allemagne'),
       (4, 'Fournisseur 4', 'Madrid', 'Espagne'),
       (5, 'Fournisseur 5', 'Rome', 'Italie'),
       (6, 'Fournisseur 6', 'Nice', 'France');


INSERT INTO Produit (NumProd, NomProd, Conditionnement, Volume, Age)
VALUES
  (1, 'Coca', 'Bouteille', 50, 10),
  (2, 'Fanta', 'Canette', 30, 10),
  (3, 'Sprite', 'Canette', 30, 10),
  (4, 'Ice-Tea', 'Bouteille', 50, 10),
  (5, 'Orangina', 'Bouteille', 50, 10),
  (6, 'Heineken', 'Bouteille', 50, 18),
  (7, 'Coca-Lite', 'Canette', 30, 10);

INSERT INTO Employé (NumEmp, NomEmp, PrénomEmp, DateEmbauche)
VALUES (1, 'Dupont', 'Jean', '2010-01-01'),
       (2, 'Durand', 'Marie', '2012-03-02'),
       (3, 'Martin', 'Luc', '2015-05-05'),
       (4, 'Leroy', 'Julie', '2018-07-07'),
       (5, 'Roux', 'Jacques', '2020-09-09');

INSERT INTO Catalogue (NumFourn, NumProd, Prix, Stock)
VALUES (1, 1, 2.5, 100),
       (1, 2, 2, 200),
       (2, 3, 2.3, 150),
       (3, 4, 2.7, 90),
       (3, 5, 3, 50),
       (2, 6, 3.5, 70),
       (4, 1, 2, 100),
       (4, 2, 3, 200),
       (5, 3, 2.7, 150),
       (6, 4, 1.70, 90),
       (6, 5, 3.2, 50),
       (1, 6, 3, 70);
  

INSERT INTO Commande (NumProd, NumEmp, NumFourn, Date, Qté)
VALUES (1, 1, 1, '2022-01-01', 10),
       (2, 2, 2, '2022-02-02', 20),
       (3, 3, 3, '2022-03-03', 30),
       (4, 4, 1, '2022-04-04', 40),
       (5, 5, 2, '2022-05-05', 50),
       (6, 1, 3, '2022-06-06', 60);





-------------------------------------------------
-- 3) 


/* SELECT * FROM Produit */

-- 4) Trier les produits vendus aux moins de 15 ans par volume de 30 cl de maniere décroissante ( Z à A )

SELECT NomProd
FROM Produit
WHERE Age < 15 AND Volume > 30 
ORDER BY NomProd DESC;

-- 5) Affichage des conditionnement différents de produit uniquement vendu aux personnes majeure ( 18 ou plus ) et elimine les repetitions 

SELECT DISTINCT Conditionnement
FROM Produit
WHERE Age >= 18;


-- 6) 

SELECT NomFourn, Ville
FROM Fournisseur
WHERE Pays = 'France'
ORDER BY Ville;


-- 7)  

SELECT NumProd AS "Numéro de produit", Prix AS "Prix unitaire"
FROM Catalogue
WHERE NumFourn = 1 AND Prix BETWEEN 1 AND 3

-- 8)  
SELECT NumProd, NumFourn, Date, Qté
FROM Commande
WHERE NumEmp IS NULL

-- 9)

SELECT DISTINCT NumEmp
FROM Commande c
JOIN Catalogue cat ON c.NumProd = cat.NumProd
WHERE Qté > 30 AND cat.Prix BETWEEN 1 AND 10
