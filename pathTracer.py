'''
Pravesh Gaire
7/6/2019
Finds the shortest path from a point to another point in mxn grid 
A* Algorithm

TO DO:
Neighbours needs to be generalized
'''
# Func to check if a cell is valid or not
def isValid(x, y):
    return (x< ROW and x>=0 and y<COL and y>=0)

# Func to check if a cell is blocked or not
def isBlocked(x, y):
    return not MAP[x][y]

# Calculate H value using Manhattan Distance
def calculateH(x, y):
    return abs(x - DX) + abs(y - DY)

# Grid Size
ROW = 10
COL = 10

# MAP
# 1 represents movable node & 0 represents blocked node

MAP = [ 
        [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ], 
        [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ], 
        [ 1, 0, 0, 0, 1, 1, 1, 1, 1, 1 ], 
        [ 1, 1, 1, 0, 1, 0, 1, 0, 0, 1 ], 
        [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 0 ], 
        [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ], 
        [ 1, 0, 1, 0, 0, 1, 0, 0, 0, 1 ], 
        [ 1, 0, 1, 0, 1, 1, 1, 1, 1, 1 ], 
        [ 1, 1, 1, 0, 0, 0, 1, 0, 0, 1 ], 
        [ 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ], 
]
# Source
SX, SY = 3, 4
# Destination
DX, DY = 0, 9

destinationFound = False
validity = True

# Check if the given inputs are valid for various conditions
if not isValid(SX, SY):    
    print("Source is not valid")
    validity = False
if not isValid(DX, DY):
    print("Destination is not valid")
    validity = False
if isBlocked(SX, SY):
    print("Source is blocked")
    validity = False
if isBlocked(DX, DY):
    print("Destination is blocked")
    validity = False
if ((SX, SY) == (DX, DY)):
    print("Source and Destination are at same")
    validity = False

# Closed list
closedList = [[0 for j in range(COL)] for i in range(ROW)]

# list to store the details of the cells
cellDetails = [
    [
        {'f':float("inf"), 'g':float('inf'), 'h':float('inf'), 'PX':-1, 'PY':-1} for j in range(COL)
    ] 
    for i in range(ROW)
]

# initialize the source
cellDetails[SX][SY]['f'] = 0.0
cellDetails[SX][SY]['g'] = 0.0
cellDetails[SX][SY]['h'] = 0.0
cellDetails[SX][SY]['PX'] = SX
cellDetails[SX][SY]['PY'] = SY

# Open List
openList = []
openList.append([0, SX, SY])

while(openList and validity):
    parent = min(openList)
    #parent = openList.pop()
    openList.remove(parent)
    closedList[parent[1]][parent[2]] = True # add to closed list

    # Generate the 4 neighbours in E, W, N & S of the popped cell
    # N -->  North       (i-1, j) 
    # S -->  South       (i+1, j) 
    # E -->  East        (i, j+1) 
    # W -->  West        (i, j-1) 

    # North
    # Check if the cell is valid
    if (isValid(parent[1] - 1, parent[2])):
        # Check if destination is reached
        if((parent[1] - 1, parent[2]) == (DX, DY)):
            cellDetails[parent[1] - 1][parent[2]]['PX'] = parent[1]
            cellDetails[parent[1] - 1][parent[2]]['PY'] = parent[2]
            print("Destination is found")
            destinationFound = True
            break
        # check if it is already in closed list or blocked
        elif ((not closedList[parent[1] - 1][parent[2]]) and (not isBlocked(parent[1] - 1, parent[2]))):
            # find new values
            newG = cellDetails[parent[1]][parent[2]]['g'] + 1.0
            newH = calculateH(parent[1] - 1, parent[2])
            newF = newG + newH
            # check if it is in open list
            # if it is in open list compare and replace if it is better
            # if it is not in open list, add it and details
            if ((cellDetails[parent[1] - 1][parent[2]]['f'] == float('inf')) or (cellDetails[parent[1] - 1][parent[2]]['f'] > newF)):
                openList.append([newF, parent[1] - 1, parent[2]])
                cellDetails[parent[1] - 1][parent[2]]['f'] = newF
                cellDetails[parent[1] - 1][parent[2]]['g'] = newG
                cellDetails[parent[1] - 1][parent[2]]['h'] = newH
                cellDetails[parent[1] - 1][parent[2]]['PX'] = parent[1]
                cellDetails[parent[1] - 1][parent[2]]['PY'] = parent[2]

    # South
    # Check if the cell is valid
    if (isValid(parent[1] + 1, parent[2])):
        # Check if destination is reached
        if((parent[1] + 1, parent[2]) == (DX, DY)):
            cellDetails[parent[1] + 1][parent[2]]['PX'] = parent[1]
            cellDetails[parent[1] + 1][parent[2]]['PY'] = parent[2]
            print("Destination is found")
            destinationFound = True
            break
        # check if it is already in closed list or blocked
        elif ((not closedList[parent[1] + 1][parent[2]]) and (not isBlocked(parent[1] + 1, parent[2]))):
            # find new values
            newG = cellDetails[parent[1]][parent[2]]['g'] + 1.0
            newH = calculateH(parent[1] + 1, parent[2])
            newF = newG + newH
            # check if it is in open list
            # if it is in open list compare and replace if it is better
            # if it is not in open list, add it and details
            if ((cellDetails[parent[1] + 1][parent[2]]['f'] == float('inf')) or (cellDetails[parent[1] + 1][parent[2]]['f'] > newF)):
                openList.append([newF, parent[1] + 1, parent[2]])
                cellDetails[parent[1] + 1][parent[2]]['f'] = newF
                cellDetails[parent[1] + 1][parent[2]]['g'] = newG
                cellDetails[parent[1] + 1][parent[2]]['h'] = newH
                cellDetails[parent[1] + 1][parent[2]]['PX'] = parent[1]
                cellDetails[parent[1] + 1][parent[2]]['PY'] = parent[2]
                
    # East
    # Check if the cell is valid
    if (isValid(parent[1], parent[2] + 1)):
        # Check if destination is reached
        if((parent[1], parent[2] + 1) == (DX, DY)):
            cellDetails[parent[1]][parent[2] + 1]['PX'] = parent[1]
            cellDetails[parent[1]][parent[2] + 1]['PY'] = parent[2]
            print("Destination is found")
            destinationFound = True
            break
        # check if it is already in closed list or blocked
        elif ((not closedList[parent[1]][parent[2] + 1]) and (not isBlocked(parent[1], parent[2] + 1))):
            # find new values
            newG = cellDetails[parent[1]][parent[2]]['g'] + 1.0
            newH = calculateH(parent[1], parent[2] + 1)
            newF = newG + newH
            # check if it is in open list
            # if it is in open list compare and replace if it is better
            # if it is not in open list, add it and details
            if ((cellDetails[parent[1]][parent[2] + 1]['f'] == float('inf')) or (cellDetails[parent[1]][parent[2] + 1]['f'] > newF)):
                openList.append([newF, parent[1], parent[2] + 1])
                cellDetails[parent[1]][parent[2] + 1]['f'] = newF
                cellDetails[parent[1]][parent[2] + 1]['g'] = newG
                cellDetails[parent[1]][parent[2] + 1]['h'] = newH
                cellDetails[parent[1]][parent[2] + 1]['PX'] = parent[1]
                cellDetails[parent[1]][parent[2] + 1]['PY'] = parent[2]
                
    # West
    # Check if the cell is valid
    if (isValid(parent[1], parent[2] - 1)):
        # Check if destination is reached
        if((parent[1], parent[2] - 1) == (DX, DY)):
            cellDetails[parent[1]][parent[2] - 1]['PX'] = parent[1]
            cellDetails[parent[1]][parent[2] - 1]['PY'] = parent[2]
            print("Destination is found")
            destinationFound = True
            break
        # check if it is already in closed list or blocked
        elif ((not closedList[parent[1]][parent[2] - 1]) and (not isBlocked(parent[1], parent[2] - 1))):
            # find new values
            newG = cellDetails[parent[1]][parent[2]]['g'] - 1.0
            newH = calculateH(parent[1], parent[2] - 1)
            newF = newG + newH
            # check if it is in open list
            # if it is in open list compare and replace if it is better
            # if it is not in open list, add it and details
            if ((cellDetails[parent[1]][parent[2] - 1]['f'] == float('inf')) or (cellDetails[parent[1]][parent[2] - 1]['f'] > newF)):
                openList.append([newF, parent[1], parent[2] - 1])
                cellDetails[parent[1]][parent[2] - 1]['f'] = newF
                cellDetails[parent[1]][parent[2] - 1]['g'] = newG
                cellDetails[parent[1]][parent[2] - 1]['h'] = newH
                cellDetails[parent[1]][parent[2] - 1]['PX'] = parent[1]
                cellDetails[parent[1]][parent[2] - 1]['PY'] = parent[2]
# Tracing the path   
tracedPath = [(SX, SY), (DX, DY)]                 
if not destinationFound:
    print("Sorry, couldnot find the destination")
else:
    print("\nThe path is\n")
    row = cellDetails[DX][DY]['PX']
    col = cellDetails[DX][DY]['PY']
    while(not (row == SX and col == SY)):
        tracedPath.insert(1, (row, col))
        x = cellDetails[row][col]['PX']
        y = cellDetails[row][col]['PY']
        row, col = x, y
    
#print(*tracedPath)

from Point_Direction import directions

print(directions(tracedPath))
