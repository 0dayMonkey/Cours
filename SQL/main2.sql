-- Type BAC
-- a)

CREATE TABLE IF NOT EXISTS Patients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT,
  prenom TEXT,
  genre TEXT,
  annee_naissance INTEGER
);

CREATE TABLE IF NOT EXISTS Medecins (
  matricule INTEGER PRIMARY KEY,
  nom_prenom TEXT,
  specialite TEXT,
  telephone TEXT
);

CREATE TABLE IF NOT EXISTS Ordonnances (
  code INTEGER PRIMARY KEY AUTOINCREMENT,
  id_patient INTEGER,
  matricule_medecin INTEGER,
  date_ord TEXT,
  medicaments TEXT,
  FOREIGN KEY (id_patient) REFERENCES Patients(id),
  FOREIGN KEY (matricule_medecin) REFERENCES Medecins(matricule)
);


-- b) 
ALTER TABLE Patients ADD cp STR;

-- c)
INSERT INTO Patients VALUES (NULL, "Wizeunit", "Anne", "F", 
2000, "12345");

-- d)
UPDATE Patients SET genre = "F" WHERE id = 100;

-- e) 
DELETE FROM Medecins WHERE specialite = "épidémiologie";

-- f)
substr(prenom,1,1)IN("A","E","I","O","U","Y")
SELECT prenom, nom
FROM Patients
WHERE substr(cp,1,2) = "29" AND substr(prenom,1,1) IN
("A","E","I","O","U","Y")
ORDER BY annee_naissance DESC;

--g) 
SELECT p.prenom, p.nom
FROM Patients AS p
JOIN Ordonnances AS o 
ON p.id = o.id_patient
JOIN Medecins AS m
ON o.matricule_medecin = m.matricule
WHERE o.date_ord LIKE "%04-2020" AND m.specialite LIKE 
'%sychiatr%';

-- h) 

/* c'est le nombre de consult faites en déc 2020 par un médecin avec un id qui commence par 1 */

--i)

SELECT m.specialite, COUNT(o.code) AS nb_consultations_2020
FROM Ordonnances AS o
JOIN Medecins AS m
ON o.matricule_medecin = m.matricule
WHERE o.date_ord LIKE '%2020' 
GROUP BY m.specialite;
