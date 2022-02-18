import random

total_moves=[]

for i in range(100):
    square = [[-1 for i in range(3)] for j in range(3)]
    squarecells=[[[] for i in range(3)] for j in range(3)]
    circles = [9 for i in range(3)]
    moves = 0
    while True:
        used_circle = random.randint(0,2)
        if circles[used_circle] != 0:
            box_x = random.randint(0,2)
            box_y = random.randint(0,2)
            if used_circle not in squarecells[box_x][box_y]:
                if square[box_x][box_y]<used_circle:
                    square[box_x][box_y] = used_circle
                squarecells[box_x][box_y].append(used_circle)
                circles[used_circle]-=1
                moves+=1
                leave = False

                #horizontal check
                for i in square:
                    if i[0] == i[1] and i[1]==i[2] and i[1] != -1:
                        leave=True
                for i in square:
                    exists = False
                    for j in range(3):
                        if i[j] == -1:
                            exists = True
                    if not exists:
                        if (i[0]<i[1] and i[1]<i[2]) or (i[0]>i[1] and i[1]>i[2]):
                            leave = True

                #vertical check
                for j in range(3):
                    exists = False
                    for i in range(3):
                        if square[i][j] == -1:
                            exists = True
                    if not exists:
                        if square[0][j] == square[1][j] and square[1][j] == square[2][j]:
                            leave = True
                        if square[0][j] < square[1][j] and square[1][j] < square[2][j]:
                            leave = True
                        if square[0][j] > square[1][j] and square[1][j] > square[2][j]:
                            leave = True

                #Kyria Diagwnios
                exists = False
                for i in range(3):
                    if square[i][i] == -1:
                        exists = True
                if not exists:
                    if square[0][0]==square[1][1] and square[1][1]==square[2][2]:
                        leave=True
                    if square[0][0]>square[1][1] and square[1][1]>square[2][2]:
                        leave=True
                    if square[0][0]<square[1][1] and square[1][1]<square[2][2]:
                        leave=True
                
                #Deyterevousa Diagwnios
                exists = False
                for i in range(3):
                    if square[i][2-i] == -1:
                        exists = True
                if not exists:
                    if square[0][2]==square[1][1] and square[1][1]==square[2][0]:
                        leave=True
                    if square[0][2]>square[1][1] and square[1][1]>square[2][0]:
                        leave=True
                    if square[0][2]<square[1][1] and square[1][1]<square[2][0]:
                        leave=True

                if leave or (moves == 27):
                    break
    total_moves.append(moves)
sum = 0
for i in total_moves:
    sum+=i
sum = sum/len(total_moves)
print("Ο μέσος όρος των βημάτων για να λήξει το παιχνίδι σε 100 γύρους είναι {}".format(sum))