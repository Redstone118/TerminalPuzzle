import os
#The maps for the game
maps=[
#level 1, movement
[
["?","?","|","?","?","?","|","-","-","-","-","-","-","-","-","-","|","?","?","?","?","?","?","?","?",],
["?","?","|","?","?","?","|"," "," "," "," "," "," "," "," "," ","|","?","?","?","?","?","?","?","?",],
["?","?","|","?","?","?","|"," "," "," "," "," "," "," "," "," ","|","?","?","?","?","?","?","?","?",],
["?","?","|","-","-","-","|"," "," "," "," "," "," "," "," "," ","|","?","|","-","-","-","|","?","?",],
["?","?","|"," "," "," ","|"," "," "," "," "," "," "," "," "," ","|","-","|"," "," "," ","|","?","?",],
["?","?","|"," ","$"," "," "," "," "," "," ",">",">",">",">",">"," "," "," "," ","@"," ","|","?","?",],
["?","?","|"," "," "," ","|"," "," "," "," "," "," "," "," "," ","|","-","|"," "," "," ","|","?","?",],
["?","?","?","-","-","-","|"," "," "," "," "," "," "," "," "," ","|","?","|","-","-","-","|","?","?",],
["?","?","?","?","?","?","|"," "," "," "," "," "," "," "," "," ","|","?","?","?","?","?","?","?","?",],
["?","?","?","?","?","?","|"," "," "," "," "," "," "," "," "," ","|","?","?","?","?","?","?","?","?",],
["?","?","?","?","?","?","|","-","-","-","-","-","-","-","-","-","|","?","?","?","?","?","?","?","?",],
],
#level 2, hammer time
[
["?","?","?","?","?","?","?","-","-","-","-","-","?","?","?","?","?","?","?","?","?","?",],
["?","?","?","?","?","?","|"," "," "," "," "," ","|","?","?","?","?","?","?","?","?","?",],
["?","?","?","-","-","-","|"," "," "," "," ","&","|","-","-","-","?","?","?","?","?","?",],
["?","?","|"," "," "," ","|"," "," "," "," "," ","X"," "," "," ","|","?","?","?","?","?",],
["?","?","|"," ","T"," "," "," "," "," "," "," ","X"," ","@"," ","|","?","?","?","?","?",],
["?","?","|"," "," "," ","|"," "," "," "," "," ","X"," "," "," ","|","?","?","?","?","?",],
["?","?","?","-","-","-","|"," "," "," "," "," ","|","-","-","-","-","-","-","?","?","?",],
["?","?","?","?","?","?","|"," "," "," "," "," ","X","?","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","?","-","-","-","-","-","?","?","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","|","?","?","?","?"," "," "," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","|","?","?","?","?"," ","$"," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","|","?","?","?","?"," "," "," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","?","-","-","-","-","-","-","-","?","?","?",],
],
#level 3, press and hold
[
["?","?","?","?","?","?","?","-","-","-","-","-","?","?","?","?","?","?","?","?","?",],
["?","?","?","?","?","?","|"," "," "," "," "," ","|","?","?","?","?","?","?","?","?",],
["?","?","?","-","-","-","|"," "," "," "," ","&","|","-","-","-","?","?","?","?","?",],
["?","?","|"," "," "," ","|"," "," "," "," "," ","/"," "," "," ","|","?","?","?","?",],
["?","?","|"," ","O"," "," "," "," "," "," "," ","/"," ","@"," ","|","?","?","?","?",],
["?","?","|"," "," "," ","|"," "," "," "," "," ","/"," "," "," ","|","-","?","?","?",],
["?","?","?","-","-","-","|"," "," "," "," "," ","|","-","/","-","?","?","|","?","?",],
["?","?","?","?","?","?","|"," "," "," "," "," ","|","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","?","-","-","-","-","-","|","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","?","|","?","?"," "," "," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","?","|","?","?"," ","$"," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","?","|","?","?"," "," "," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","?","?","-","-","-","-","-","?","?","?",],
],
#level 4, behind the wall
[
["?","?","?","-","-","-","-","-","-","-","-","-","-","-","?","?","?","?","?",],
["?","?","|"," "," "," ","X"," "," "," ","/"," "," "," ","|","?","?","?","?",],
["?","?","|"," ","O"," ","X"," "," "," ","/"," ","@"," ","|","?","?","?","?",],
["?","?","|"," "," "," ","X"," "," "," ","/"," "," "," ","|","?","?","?","?",],
["?","?","?","-","-","-","|"," "," "," ","|","-","-","X","-","-","?","?","?",],
["?","?","?","?","?","?","?","-"," ","-","?","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","|"," "," "," ","|","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","|"," ","T"," ","|","?","?"," "," "," ","|","?","?",],
["?","?","?","?","?","?","|"," "," "," ","|","?","?"," ","$"," ","|","?","?",],
["?","?","?","?","?","?","-","-","-","-","|","?","?"," "," "," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","?","-","-","-","-","-","?","?","?",],
],
#level 5, a tale of two buttons
[
["?","?","?","-","-","-","-","-","-","-","?","?","?","?","?","?","?","?","?"],
["?","?","|"," "," "," ","|"," "," "," ","|","?","?","?","?","?","?","?","?"],
["?","?","|"," ","$"," ","X"," ","O"," ","|","?","?","?","?","?","?","?","?"],
["?","?","|"," "," "," ","|"," "," "," ","|","?","?","?","?","?","?","?","?"],
["?","?","|","-","-","-","|","/","/","/","|","-","-","-","-","-","?","?","?"],
["?","?","|"," "," "," ","|"," "," "," ","/"," ","/"," "," "," ","|","?","?"],
["?","?","|"," ","T"," "," "," "," "," ","/"," ","/"," ","@"," ","|","?","?"],
["?","?","|"," "," "," ","|"," "," "," ","/"," ","/"," "," "," ","|","?","?"],
["?","?","?","-","-","-","|","X","X","X","|","-","-","-","-","-","?","?","?"],
["?","?","?","?","?","?","|"," "," "," ","|","?","?","?","?","?","?","?","?"],
["?","?","?","?","?","?","|"," ","O"," ","|","?","?","?","?","?","?","?","?"],
["?","?","?","?","?","?","|"," "," "," ","|","?","?","?","?","?","?","?","?"],
["?","?","?","?","?","?","?","-","-","-","?","?","?","?","?","?","?","?","?"],
],
#level 6, boxes
[
["?","?","?","-","-","-","-","-","?","?","?","?","?","?","?","?",],
["?","?","|"," "," "," "," "," ","|","-","-","-","-","?","?","?",],
["?","?","|"," "," "," "," "," ","|"," "," "," "," ","|","?","?",],
["?","?","|"," "," "," "," ","#"," "," "," ","@"," ","|","?","?",],
["?","?","|"," "," "," "," "," ","|"," "," "," "," ","|","?","?",],
["?","?","|"," "," "," "," "," ","?","-","-","-","-","?","?","?",],
["?","?","|","-","-","-","-","-","?","?","|","?","?","?","?","?",],
["?","?","|","?","?","?","?","?","?","?","|","?","?","?","?","?",],
["?","?","|","?","?","?","?","?","?","?","|","?","?","?","?","?",],
["?","?","|","?"," "," "," ","?","?","?","|","?","?","?","?","?",],
["?","?","|","?"," ","$"," ","?","?","?","|","?","?","?","?","?",],
["?","?","|","?"," "," "," ","?","?","?","|","?","?","?","?","?",],
["?","?","?","-","-","-","-","-","-","-","?","?","?","?","?","?",],
],
#level 7, heavy button
[
["?","?","?","?","?","?","?","-","-","-","-","-","?","?","?","?","?","?","?"],
["?","?","?","?","?","?","|"," "," "," "," "," ","|","?","?","?","?","?","?"],
["?","?","?","-","-","-","|"," "," "," "," "," ","|","-","-","-","?","?","?"],
["?","?","|"," "," "," ","&"," "," "," "," "," ","/"," "," "," ","|","?","?"],
["?","?","|"," ","%"," ","#"," "," "," "," "," ","/"," ","@"," ","|","?","?"],
["?","?","|"," "," "," "," "," "," "," "," "," ","/"," "," "," ","|","?","?"],
["?","?","?","-","-","-","|"," "," "," "," "," ","|","-","-","-","?","?","?"],
["?","?","?","?","?","?","|"," "," "," "," "," ","|","?","?","?","?","?","?"],
["?","?","?","?","?","?","|","-","-","-","-","-","|","?","?","?","?","?","?"],
["?","?","?","?","?","?","|","?","?","?","?","?","|","?","?","?","?","?","?"],
["?","?","?","?","?","?","|","?","?","?","?","?","|","?","?","?","?","?","?"],
["?","?","?","?","?","?","|","?"," "," "," ","?","|","?","?","?","?","?","?"],
["?","?","?","?","?","?","|","?"," ","$"," ","?","|","?","?","?","?","?","?"],
["?","?","?","?","?","?","|","?"," "," "," ","?","|","?","?","?","?","?","?"],
["?","?","?","?","?","?","?","-","-","-","-","-","?","?","?","?","?","?","?"],
],
#level 8, Portal 3
[
["?","?","?","-","-","-","-","?","?","?","-","-","-","-","-","?","?","?",],
["?","?","|"," "," "," "," ","|","?","|"," "," "," "," "," ","|","?","?",],
["?","?","|"," "," "," "," ","|","?","|"," "," "," "," "," ","|","?","?",],
["?","?","|"," "," "," "," ",":","|",":"," "," ","@"," "," ","|","?","?",],
["?","?","|"," "," "," "," ","|","?","|"," "," "," "," "," ","|","?","?",],
["?","?","|"," "," "," "," ","|","?","|"," "," "," "," "," ","|","?","?",],
["?","?","?","-","-","-","-","?","?","|","-","-","-","-","?","|","?","?",],
["?","?","?","?","?","?","?","?","?","|","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","?","?","?","|","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","?","?","?","|","?","?","?","?","?","|","?","?",],
["?","?","?","?","?","?","?","?","?","|","?","?"," "," "," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","|","?","?"," ","$"," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","|","?","?"," "," "," ","|","?","?",],
["?","?","?","?","?","?","?","?","?","?","-","-","-","-","-","?","?","?",],
],
#level 9, boxes throughout dimentions
[
["?","?","|","-","-","-","-","-","-","?","?","-","-","-","-","?","?","?",],
["?","?","|","?","?","|"," "," "," ","|","|"," "," "," "," ","|","?","?",],
["?","?","|","?","?","|"," "," ","#",":",":"," "," ","@"," ","|","?","?",],
["?","?","|","?","?","|"," "," "," ","|","|"," "," "," "," ","|","?","?",],
["?","?","|","?","?","?","-","-","-","?","?","-","-","-","-","|","?","?",],
["?","?","|","?","?","?","?","?","?","?","?","?","?","?","?","|","?","?",],
["?","?","|","-","-","-","?","?","?","?","?","?","?","?","?","|","?","?",],
["?","?","|"," "," "," ","|","?","?","?","?","?","?","?","?","|","?","?",],
["?","?","|"," ","$"," ",":","|","?","?","?","?","?","$","?","|","?","?",],
["?","?","|"," "," "," ","|","?","?","?","?","?","?","?","?","|","?","?",],
["?","?","?","-","-","-","-","-","-","-","-","-","-","-","-","?","?","?",],
],
#level 10, big room
[
["?","?","?","?","?","?","?","?","?","-","-","-","-","-","?","-","-","-","-","-","-","?","?","?",],
["?","?","?","-","-","-","?","?","|"," "," "," "," "," ","|","?","?","?","?","?","?","|","?","?",],
["?","?","|"," "," "," ","|","?","|"," "," "," "," "," ","|","?","?"," "," "," ","?","|","?","?",],
["?","?","|"," "," "," ","|","?","|"," "," ","@"," "," ","|","?","?"," ","$"," ","?","|","?","?",],
["?","?","|"," ","O"," ","|","?","|"," "," "," "," "," ","|","?","?"," "," "," ","?","|","?","?",],
["?","?","|"," "," "," ","|","?","|"," "," "," "," "," ","|","?","?","?","?","?","?","|","?","?",],
["?","?","|"," "," "," ","|","?","|"," "," "," "," "," ","|","?","?","?","?","?","?","|","?","?",],
["?","?","|"," "," "," ","|","?","|","/","/","/","/","/","?","?","?","?","?","?","?","|","?","?",],
["?","?","|"," "," "," ","|","?","|"," "," "," "," "," ","|","-","-","-"," ","?","?","|","?","?",],
["?","?","|"," "," "," ","|","?","|"," "," "," "," "," "," "," "," "," ","|","?","?","|","?","?",],
["?","?","|"," ","#"," "," ","|",":"," "," "," "," "," "," "," ","%"," ","|","?","?","|","?","?",],
["?","?","|"," ","|"," ","|","?","|"," "," "," "," "," "," "," "," "," ","|","?","?","|","?","?",],
["?","?","|"," ","|"," ","|","?","|"," "," "," "," "," ","|","-","-","-","?","?","?","|","?","?",],
["?","?","?","-","-","-","?","?","?","-","-","-","-","-","?","?","?","?","-","-","-","?","?","?",],
],
]
#Bunch of misc variables
barrier=["|","-","X","/","#"]
levelstarting=[[5,10],[4,9],[4,9],[2,8],[6,8],[3,5],[4,9],[3,5],[2,6],[7,4]]
level=0
y_position=levelstarting[level][0]
x_position=levelstarting[level][1]
playerscreen=maps[0].copy
has_hammer=0
lastmove=str()
heavybuttontext=""
totalmoves=0
secrets=[]
currentmove=""
for i in maps:
    secrets.append("?")
buttons={
(2,4,4):[[3,12],[4,12],[5,12],[6,14],[" "]],
(3,2,4):[[1,10],[2,10],[3,10],[" "]],
(4,2,8):[[5,12],[6,12],[7,12],[" "]],
(4,10,8):[[5,10],[6,10],[7,10],[4,7],[4,8],[4,9],[" "]],
(6,4,4):[[3,12],[4,12],[5,12],[8,9],[" "]],
(9,4,4):[[10,6],[":"]],
(9,10,16):[[7,9],[7,10],[7,11],[7,12],[7,13],[" "]],
}
NPCs={
(1,2,11):"This wall isn't as strong as those that surround it, perhaps it can be broken down",
(2,2,11):"This part of the wall is inset from the rest, and footprints are cut off at the base",
(6,3,6):"This button will not budge if you stand on it, but perhaps something heavier can weigh it down",
}
portals={
(7,3,7):[[3,10],[3,11]],
(7,3,9):[[3,6],[3,5]],
(8,2,9):[[2,11],[2,12]],
(8,2,10):[[8,5],[8,4]],
(8,8,6):[[2,11],[2,12]],
(9,10,6):[[10,9],[10,10]],
(9,10,8):[[10,5],[10,4]]
}
#Various functions for the game
def showarea(radius):
    global maps
    for i in range(y_position-radius,y_position):
        print("  ".join(maps[level][i%len(maps[level])][x_position-radius:1+x_position+radius]))
    print(str("  ".join(maps[level][y_position][x_position-radius:x_position]))+"  P  "+str("  ".join(maps[level][y_position][x_position+1:x_position+radius+1])))
    for i in range(y_position+1,y_position+radius+1):
        print("  ".join(maps[level][i%len(maps[level])][x_position-radius:1+x_position+radius]))
def do(action):
    global x_position
    global y_position
    global lastmove
    global has_hammer
    global heavybuttontext
    global totalmoves
    global maps
    if action=="w":
        if maps[level][y_position-1][x_position]=="#" and maps[level][y_position-2][x_position]==" ":
            maps[level][y_position-1][x_position]=" "
            maps[level][y_position-2][x_position]="#"
        elif maps[level][y_position-1][x_position]=="#" and maps[level][y_position-2][x_position]==":":
            maps[level][y_position-1][x_position]=" "
            maps[level][portals[(level,y_position-2,x_position)][0][0]][portals[(level,y_position-2,x_position)][0][1]]="#" # type: ignore
        elif maps[level][y_position-1][x_position]=="#" and maps[level][y_position-2][x_position]=="%":
            maps[level][y_position-1][x_position]=" "
            for i in range(len(buttons[(level,y_position-2,x_position)])-1): # type: ignore
                maps[level][buttons[(level,y_position-2,x_position)][i][0]][buttons[(level,y_position-2,x_position)][i][1]]="".join(buttons[(level,y_position-2,x_position)][-1]) # type: ignore
            heavybuttontext="As you push the box atop the plate, you hear at grinding sound"
        if maps[level][y_position-1][x_position] not in barrier:
            y_position-=1
    elif action=="s":
        if maps[level][y_position+1][x_position]=="#" and maps[level][y_position+2][x_position]==" ":
            maps[level][y_position+1][x_position]=" "
            maps[level][y_position+2][x_position]="#"
        elif maps[level][y_position+1][x_position]=="#" and maps[level][y_position+2][x_position]==":":
            maps[level][y_position+1][x_position]=" "
            maps[level][portals[(level,y_position+2,x_position)][0][0]][portals[(level,y_position+2,x_position)][0][1]]="#" # type: ignore
        elif maps[level][y_position+1][x_position]=="#" and maps[level][y_position+2][x_position]=="%":
            maps[level][y_position+1][x_position]=" "
            for i in range(len(buttons[(level,y_position+2,x_position)])-1): # type: ignore
                maps[level][buttons[(level,y_position+2,x_position)][i][0]][buttons[(level,y_position+2,x_position)][i][1]]="".join(buttons[(level,y_position+2,x_position)][-1]) # type: ignore
            heavybuttontext="As you push the box atop the plate, you hear at grinding sound"
        if maps[level][y_position+1][x_position] not in barrier:
            y_position+=1
    elif action=="a":
        if maps[level][y_position][x_position-1]=="#" and maps[level][y_position][x_position-2]==" ":
            maps[level][y_position][x_position-1]=" "
            maps[level][y_position][x_position-2]="#"
        elif maps[level][y_position][x_position-1]=="#" and maps[level][y_position][x_position-2]==":":
            maps[level][y_position][x_position-1]=" "
            maps[level][portals[(level,y_position,x_position-2)][0][0]][portals[(level,y_position,x_position-2)][0][1]]="#" # type: ignore
        elif maps[level][y_position][x_position-1]=="#" and maps[level][y_position][x_position-2]=="%":
            maps[level][y_position][x_position-1]=" "
            for i in range(len(buttons[(level,y_position,x_position-2)])-1): # type: ignore
                maps[level][buttons[(level,y_position,x_position-2)][i][0]][buttons[(level,y_position,x_position-2)][i][1]]="".join(buttons[(level,y_position,x_position-2)][-1]) # type: ignore
            heavybuttontext="As you push the box atop the plate, you hear at grinding sound"
        if maps[level][y_position][x_position-1] not in barrier:
            x_position-=1
    elif action=="d":
        if maps[level][y_position][x_position+1]=="#" and maps[level][y_position][x_position+2]==" ":
            maps[level][y_position][x_position+1]=" "
            maps[level][y_position][x_position+2]="#"
        elif maps[level][y_position][x_position+1]=="#" and maps[level][y_position][x_position+2]==":":
            maps[level][y_position][x_position+1]=" "
            maps[level][portals[(level,y_position,x_position+2)][0][0]][portals[(level,y_position,x_position+2)][0][1]]="#" # type: ignore
        elif maps[level][y_position][x_position+1]=="#" and maps[level][y_position][x_position+2]=="%":
            maps[level][y_position][x_position+1]=" "
            for i in range(len(buttons[(level,y_position,x_position+2)])-1): # type: ignore
                maps[level][buttons[(level,y_position,x_position+2)][i][0]][buttons[(level,y_position,x_position+2)][i][1]]="".join(buttons[(level,y_position,x_position+2)][-1]) # type: ignore
            heavybuttontext="As you push the box atop the plate, you hear at grinding sound"
        if maps[level][y_position][x_position+1] not in barrier:
            x_position+=1
    elif action=="h":
         if has_hammer == 1:
            if lastmove=="w" and maps[level][y_position-1][x_position]=="X":
                maps[level][y_position-1][x_position] = " "
            elif lastmove=="s" and maps[level][y_position+1][x_position]=="X":
                maps[level][y_position+1][x_position] = " "
            elif lastmove=="a" and maps[level][y_position][x_position-1]=="X":
                maps[level][y_position][x_position-1] = " "
            elif lastmove=="d" and maps[level][y_position][x_position+1]=="X":
                maps[level][y_position][x_position+1] = " "

            if lastmove=="w" and maps[level][y_position-1][x_position]=="x":
                maps[level][y_position-1][x_position] = " "
            elif lastmove=="s" and maps[level][y_position+1][x_position]=="x":
                maps[level][y_position+1][x_position] = " "
            elif lastmove=="a" and maps[level][y_position][x_position-1]=="x":
                maps[level][y_position][x_position-1] = " "
            elif lastmove=="d" and maps[level][y_position][x_position+1]=="x":
                maps[level][y_position][x_position+1] = " "
    lastmove=action
    totalmoves+=1
def checkforpickups():
    global y_position
    global x_position
    global has_hammer
    global level
    global lastmove
    global maps
    if maps[level][y_position][x_position]=="T":
        has_hammer+=1
        print("You heft the hammer, it may not break down the walls that surround you, but perhaps it will work on something weaker")
        maps[level][y_position][x_position] = " "
    if maps[level][y_position][x_position]=="O":
        for i in range(len(buttons[(level,y_position,x_position)])-1): # type: ignore
            maps[level][buttons[(level,y_position,x_position)][i][0]][buttons[(level,y_position,x_position)][i][1]]="".join(buttons[(level,y_position,x_position)][-1]) # type: ignore
        maps[level][y_position][x_position]="o"
        print("You hear a creak as you step atop the button")
    if maps[level][y_position][x_position]=="&":
        print(NPCs[(level,y_position,x_position)]) # type: ignore
    if maps[level][y_position][x_position]=="$":
        secrets[level]="$"
        print("You found a secret, good job")
        maps[level][y_position][x_position]=" "
def checkforportals():
    global y_position
    global x_position
    global maps
    if maps[level][y_position][x_position]==":":
        if maps[level][portals[(level,y_position,x_position)][0][0]][portals[(level,y_position,x_position)][0][1]]=="#": # type: ignore
            maps[level][portals[(level,y_position,x_position)][0][0]][portals[(level,y_position,x_position)][0][1]]=" " # type: ignore
            maps[level][portals[(level,y_position,x_position)][1][0]][portals[(level,y_position,x_position)][1][1]]="#" # type: ignore
        y_position,x_position=(portals[(level,y_position,x_position)][0][0],portals[(level,y_position,x_position)][0][1]) # type: ignore
#The main loop for the game
showarea(3)
while True:
    currentmove=input("")
    for i in range(len(currentmove)):
        do(currentmove[i])
        os.system("clear")
        checkforportals()
    showarea(3)
    if heavybuttontext!="":
        print(heavybuttontext)
        heavybuttontext=""
    checkforpickups()
    if maps[level][y_position][x_position]=="@":
        if level<(len(maps)-1):
            print("On to the next level")
            os.system("clear")
        if level==(len(maps)-1):
            os.system("clear")
            print("""You Win:Here's a pizza
       __________
       \\________/
        \\0  0  /
         \\ 0 0/
          \\ 0/
           \\/
""")
            print("And it only took you "+str(totalmoves)+" moves")
            print("Secrets found:")
            print(" - ".join(secrets))
            break
        level+=1
        has_hammer=0
        y_position=levelstarting[level][0]
        x_position=levelstarting[level][1]
        showarea(3)