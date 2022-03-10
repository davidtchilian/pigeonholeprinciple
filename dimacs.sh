#!/bin/bash
# $1 = nbPigeons
# $2 = nbNids

if (( $# != 2 )); then
	echo "arguments invalides, donnez deux nombres (un pour les pigeons et un pour les nids)"
	echo "par exemple : ./code.sh 3 4"
	exit 1
fi
#Algorithme quadratique O(n²)

let m=$1*$2

# nombre de clauses 
# Pour chaque pigeon = $1
# pour chaque nid = nombre de combinaisons 2 a 2 des pigeons : $1*($1-1)/2
# divisé par 2 pour eviter a b et b a
n=$(($1+$2*($1*($1-1)/2)))

# header
echo p cnf $m $n

# Chaque pigeon a au moins un nid
for i in $(seq 1 $2 $m); do
	let j=$i+$2-1
	echo $(seq $i $j) 0
done

# Affichage de toutes les combinaisons possibles
# Chaque nid a au maximum un pigeon
# exemple : pairs 1 2 3 4 donnera :
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
function pairs
{
for i in $@; do
shift
	for j in $@; do
		echo $i $j 0
	done
done
}

# Pour chaque nid calculer les dissociations deux a deux pour chaque pigeon
for i in $(seq $2); do
pairs $(for j in $(seq 1 $2 $m); do
		let k=$i+$j-1
		echo $k
	done)
done | awk '{print "-"$1" -"$2" 0"}'