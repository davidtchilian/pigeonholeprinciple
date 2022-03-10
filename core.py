from pysat.solvers import Glucose3
import subprocess
import os

# parser de string qui permet de parcourir un string ligne par ligne
# très utile pour parcourir la CNF générée et la transformer en clauses
def giveLines(str):
    returnChar = ''
    for char in str:
        returnChar += char if not char == '\n' else ''
        if char == '\n':
            yield returnChar
            returnChar = ''
    if returnChar:
        yield returnChar

def satPigeon(pigeons, nids, showModel, giveCNF):
    model = []
    g = Glucose3()
    process = subprocess.Popen(["./cnf.sh", str(pigeons), str(nids)], stdout=subprocess.PIPE)
    output, error = process.communicate()  # retourne un binaire
    res = output.decode('UTF-8').replace("\\n", "\n")

    if giveCNF:
        for f in giveLines(res):
            print(f)

    for f in giveLines(res):
        f = f.split(' ')
        listint = []
        for i in f:
            listint.append(int(i))
        g.add_clause(listint)
    satresult = g.solve()
    # print("satresult", end="")
    # print(satresult)
    if(satresult):
        print("SAT", end="")
        model = g.get_model()
        if showModel:
            print(" : ", end="")
            print(model)
        else:
            print()
    else:
        print("UNSAT")


if __name__ == '__main__':
    model = satPigeon(3, 2, True, False) # test
