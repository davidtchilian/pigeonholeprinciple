
# Introduction

"pigeon" est un script en python qui est capable de simuler une expérience du principe des tiroirs.
Il prend en compte différentes options comme la possibilité de chercher à résoudre le problème du principe des tiroirs une seule fois.
Ou encore de lancer une boucle qui ira jusque la valeur indiquée.

# Prérequis pour le fonctionnement du script

- python
- pysat (paquet python qui comprend le SAT solver Glucose)
- bash

# Installation automatique

Vous pouvez executer ```make install``` ou alors suivre l'installation détaillée.

## Installation détaillée

#### Pour pysat

```pip3 install python-sat[pblib,aiger]```

#### Droits d'éxécution des fichiers sh

```chmod a+x cnf.sh```
```chmod a+x dimacs.sh```

# Utilisation du script pigeon.py

Afficher l'aide : ```python3 pigeon.py -h```

#### Liste des arguments valables :

- -h 	--help      (affiche l'aide aide)
- -u    --unique    (unique)
- -m 	--modele    (affiche le modèle qui satisfait l'expérience si il en a un)
- -b 	--boucle    (exécute une boucle qui parcours tous les modeles pigeons/nids jusqu'à atteindre les arguments donnés)
- -c    --cnf       (affiche seulement le fichier CNF du probleme avec les parametres donnés)
Le premier argument correspond au nombre de pigeons, le deuxieme au nombre de nids.

# Exemples d'utilisations

- Exécuter un exemple avec 3 nids et 3 pigeons : ```make exemple```

- Lancer une seule fois l'expérience : ```python3 pigeon.py -u 3 4 ``` 
Dans cet exemple on a 3 pigeons et 4 nids.

- Lancer une seule fois l'expérience et obtenir le modèle associé : ```python3 pigeon.py -u -m 3 4 ``` 

- Enregistrer le fichier CNF d'une expérience ainsi que sa satisfaisabilité : ```python3 pigeon.py -c 3 4 > experience.cnf``` 

- Générer un fichier au format DIMACS avec des "0" à la fin de chaque ligne et une en-tête de forme "p cnf a b" : ```./dimacs.sh 3 4```

- Générer et enregistrer dans un fichier au format CNF sans les "0" à la fin de chaque ligne : ```./cnf.sh 3 4 > moncnf.cnf```