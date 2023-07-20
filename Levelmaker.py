currentrow=0
newgrid=[]
newrow=[]
currentcharacter=0
newnpcs={}
newnpcpositions=[0,0,0]
newbuttons={}
newbuttonpositions=[0,0,0]
newbuttonoutputs=[0,0,0]
newportals={}
newportalpositions=[0,0,0]
newportaloutputs=[0,0,0]
newstartingposition=[]
filepath=input()
#Generates the map and the level starting position
while open(filepath).readlines()[currentrow][0] != "!":
    for i in range(len(open(filepath).readlines()[0].strip())):
        if open(filepath).readlines()[currentrow][i]=="S":
            newstartingposition=[currentrow,i]
            newrow.append(" ")
        else:
            newrow.append(open(filepath).readlines()[currentrow][i])
    newgrid.append(newrow)
    newrow=[]
    currentrow+=1
currentrow+=1
currentcharacter=0
#Generates the NPC dialogue and positions
while open(filepath).readlines()[currentrow][0] != "!":
    for i in range(0,3):
        while open(filepath).readlines()[currentrow][currentcharacter] != ",":
            newnpcpositions[i]=newnpcpositions[i]*10+int(open(filepath).readlines()[currentrow][currentcharacter].strip())
            currentcharacter+=1
        currentcharacter+=1
    newnpcs[tuple(newnpcpositions)]=open(filepath).readlines()[currentrow][currentcharacter:].strip()
    newnpcpositions=[0,0,0]
    currentcharacter=0
    currentrow+=1
currentrow+=1
currentcharacter=0
#Generates the button positions and outputs
while open(filepath).readlines()[currentrow][0] != "!":
    currentcharacter=2
    for i in range(3):
        while open(filepath).readlines()[currentrow][currentcharacter] != ",":
            newbuttonpositions[i]=newbuttonpositions[i]*10+int(open(filepath).readlines()[currentrow][currentcharacter].strip())
            currentcharacter+=1
        currentcharacter+=1
    newbuttons[tuple(newbuttonpositions)]=[]
    while open(filepath).readlines()[currentrow][currentcharacter] != "\n":
        for j in range(3):
            while open(filepath).readlines()[currentrow][currentcharacter] != ",":
                newbuttonoutputs[j]=(newbuttonoutputs[j]*10)+int(open(filepath).readlines()[currentrow][currentcharacter].strip())
                currentcharacter+=1
            currentcharacter+=1
        newbuttons[tuple(newbuttonpositions)].append(newbuttonoutputs)
        newbuttonoutputs=[0,0,0]
    newbuttons[tuple(newbuttonpositions)].append(open(filepath).readlines()[currentrow][0])
    currentrow+=1
currentrow+=1
currentcharacter=0
#Generates the portal positions and outputs
while open(filepath).readlines()[currentrow][0] != "!":
    for i in range(3):
        while open(filepath).readlines()[currentrow][currentcharacter] != ",":
            newportalpositions[i]=newportalpositions[i]*10+int(open(filepath).readlines()[currentrow][currentcharacter])
            currentcharacter+=1
        currentcharacter+=1
    newportals[tuple(newportalpositions)]=[]
    for i in range(2):
        for i in range(3):
            while open(filepath).readlines()[currentrow][currentcharacter] != ",":
                newportaloutputs[i]=newportaloutputs[i]*10+int(open(filepath).readlines()[currentrow][currentcharacter])
                currentcharacter+=1
            currentcharacter+=1
        newportals[tuple(newportalpositions)].append(newportaloutputs)
        newportaloutputs=[0,0,0]
    currentrow+=1
print("[")
for i in range(len(newgrid)):
    print(f"{newgrid[i]},")
print("],")
print(f"{newstartingposition},")
print(f"{newnpcs},")
print(f"{newbuttons},")
print(f"{newportals},")
open(filepath).close()