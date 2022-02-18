import random

tower_points = []
soldier_points = []

for match in range(100):
    square = [[0 for i in range(8)] for j in range(8)]
    tower_coordinates = []
    for i in range(2):
        cord = random.randint(0,7)
        tower_coordinates.append(cord)

    soldier_coordinates = tower_coordinates
    while soldier_coordinates == tower_coordinates:
        soldier_coordinates = []
        for i in range(2):
            cord = random.randint(0,7)
            soldier_coordinates.append(cord)

    square[tower_coordinates[0]][tower_coordinates[1]] = 1
    square[soldier_coordinates[0]][soldier_coordinates[1]] = 2

    for i in range(8):
        if square[i][tower_coordinates[1]] == 2:
            tower_points.append(1)
        if square[tower_coordinates[0]][i] == 2:
            tower_points.append(1)

    x,y=soldier_coordinates[0],soldier_coordinates[1]

    #
    while x>0 and y>0:
        x-=1
        y-=1
    while x<=7 and y<=7:
        if square[x][y] == 1:
            soldier_points.append(1)
        x+=1
        y+=1

    x,y=soldier_coordinates[0],soldier_coordinates[1]
    #
    while x>0 and y<7:
        x-=1
        y+=1

    while x<=7 and y>=0:
        if square[x][y] == 1:
            soldier_points.append(1)
        x+=1
        y-=1
print("Στην σκακιέρα 8x8, σε 100 παιχνίδια ο πύργος απέκτησε {} πόντους, ενώ ο αξιωματικός {}".format(len(tower_points),len(soldier_points)))

tower_points = []
soldier_points = []
for match in range(100):
    square = [[0 for i in range(7)] for j in range(7)]
    tower_coordinates = []
    for i in range(2):
        cord = random.randint(0,6)
        tower_coordinates.append(cord)

    soldier_coordinates = tower_coordinates
    while soldier_coordinates == tower_coordinates:
        soldier_coordinates = []
        for i in range(2):
            cord = random.randint(0,6)
            soldier_coordinates.append(cord)

    square[tower_coordinates[0]][tower_coordinates[1]] = 1
    square[soldier_coordinates[0]][soldier_coordinates[1]] = 2

    for i in range(7):
        if square[i][tower_coordinates[1]] == 2:
            tower_points.append(1)
        if square[tower_coordinates[0]][i] == 2:
            tower_points.append(1)

    x,y=soldier_coordinates[0],soldier_coordinates[1]
    #
    while x>0 and y>0:
        x-=1
        y-=1
    while x<=6 and y<=6:
        if square[x][y] == 1:
            soldier_points.append(1)
        x+=1
        y+=1

    x,y=soldier_coordinates[0],soldier_coordinates[1]
    #
    while x>0 and y<6:
        x-=1
        y+=1

    while x<=6 and y>=0:
        if square[x][y] == 1:
            soldier_points.append(1)
        x+=1
        y-=1
print("Στην σκακιέρα 7x7, σε 100 παιχνίδια ο πύργος απέκτησε {} πόντους, ενώ ο αξιωματικός {}".format(len(tower_points),len(soldier_points)))

tower_points = []
soldier_points = []
for match in range(100):
    square = [[0 for i in range(8)] for j in range(7)]
    tower_coordinates = []
    cord = random.randint(0,6)
    tower_coordinates.append(cord)
    cord = random.randint(0,7)
    tower_coordinates.append(cord)

    soldier_coordinates = tower_coordinates
    while soldier_coordinates == tower_coordinates:
        soldier_coordinates = []
        cord = random.randint(0,6)
        soldier_coordinates.append(cord)
        cord = random.randint(0,7)
        soldier_coordinates.append(cord)

    square[tower_coordinates[0]][tower_coordinates[1]] = 1
    square[soldier_coordinates[0]][soldier_coordinates[1]] = 2

    for i in range(7):
        if square[i][tower_coordinates[1]] == 2:
            tower_points.append(1)
    for i in range(8):
        if square[tower_coordinates[0]][i] == 2:
            tower_points.append(1)

    x,y=soldier_coordinates[0],soldier_coordinates[1]
    #
    while x>0 and y>0:
        x-=1
        y-=1
    while x<=6 and y<=7:
        if square[x][y] == 1:
            soldier_points.append(1)
        x+=1
        y+=1

    x,y=soldier_coordinates[0],soldier_coordinates[1]
    #
    while x>0 and y<7:
        x-=1
        y+=1

    while x<=6 and y>=0:
        if square[x][y] == 1:
            soldier_points.append(1)
        x+=1
        y-=1
print("Στην σκακιέρα 7x8, σε 100 παιχνίδια ο πύργος απέκτησε {} πόντους, ενώ ο αξιωματικός {}".format(len(tower_points),len(soldier_points)))
