
import argparse
import core as p

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pigeons", type=int, help="nombre de pigeons")
    parser.add_argument("nids", type=int, help="nombre de nids")
    parser.add_argument("-m", "--modele", help="affiche le modele obtenu si le CNF est satisfaisable", action="store_true")
    parser.add_argument("-b", "--boucle", help="execute une boucle jusqu'a atteindre la valeur donnée en argument pour n et m", action="store_true")
    parser.add_argument("-u", "--unique", help="execute une seule fois l'experience avec les n et m donnés", action="store_true")
    parser.add_argument("-c", "--cnf", help="affiche la Forme normale conjonctive du probleme donné", action="store_true")
    args = parser.parse_args()
    
    if args.boucle:
        increment = 0
        pigeons = args.pigeons
        nids = args.nids
        print("pigeons : " + str(pigeons) + " nids : " + str(nids))
        while pigeons != 0 and nids != 0:
            pigeons = pigeons - 1
            nids = nids - 1
            increment = increment + 1

        for i in range(increment):
            print("pigeons : " + str(pigeons + i+1) + " nids : " + str(nids + i+1) + " : ", end="")
            p.satPigeon(pigeons + i+1, nids + i+1, args.modele, args.cnf)
        return

    if args.unique:
        # print(args)
        p.satPigeon(args.pigeons, args.nids, args.modele, args.cnf)
        return
    if args.cnf:
        p.satPigeon(args.pigeons, args.nids, args.modele, args.cnf)
        return
    

if __name__ == '__main__':
    main()

    