A=[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]
CHeigth =[0,0,0,0,0,0,0]
def ClearA():
    for x in range(7):
        CHeigth[x] = 0
        for y in range(6):
            A[x][y] = 0

    
def out():
    print("\n")
    for i in range(gr):
        y2 = gr-1-i
        S = ""
        for x2 in range(gr):
            S += str(feld[x2][y2]) + " "
        print(S)
    print("\n")


#Feld
gr = 7
feld = []
for e in range(gr):
    feld.append(0)

for i in range(gr):
    cols = []
    for j in range(gr):
        cols.append(0)
    feld[i] = cols

out()

#Gameloop

player = True
end = True
while end:
    
    
    #Chip Eingabe
    if player:
        print("Spieler 1")

    else:
        print("Spieler 2")


    drop = int(input("Spalte: ")) - 1
    li = feld[drop]

    c = -1
    for n in li:
        c += 1
        if c == gr:
            print("Kein Platz.")
            break
        if n == 0:
            if player:
                li[c] = 1
                player = False
                break
            else:
                li[c] = -1
                player = True
                break

    print(CHeigth)            
    out()

    #Checken
    #Check y-achse
    for y in range(gr):

        sumy = 0

        for a in feld[y]:
            sumy += a

        #Ende
        if sumy == 4:
            print("Spieler 1 hat gewonnen.")
            end = False

        elif sumy == -4:
            print("Spieler 2 hat gewonnen.")
            end = False

        else:
            end = True

   #Check x-achse
   
    for x in range(gr):
        sumx = 0

        for b in range(gr):
            sumx += feld[b][x]
    
        #Ende
        if sumx == 4:
            print("Spieler 1 hat gewonnen.")
            end = False

        elif sumx == -4:
            print("Spieler 2 hat gewonnen.")
            end = False

        else:
            end = True

#::::::::::::::::::::::::::::::::::::::::::::::
