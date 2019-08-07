import serial
import numpy
from directions import directions

# Func to check if a cell is valid or not
def isValid(x, y):
    return (x< ROW and x>=0 and y<COL and y>=0)

# Func to check if a cell is blocked or not
def isBlocked(x, y):
    return not MAP[x][y]

# Calculate H value using Manhattan Distance
def calculateH(x, y):
    return abs(x - DX) + abs(y - DY)

def tracer(source, dest):
    destinationFound = False
    validity = True

    SX, SY = source
    DX, DY = dest

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
        return [(SX, SY)]

     # Closed list
    closedList = [[0 for j in range(COL)] for i in range(ROW)]

    # list to store the details of the cells
    cellDetails = [
        [
            {'f':float("inf"), 'g':float('inf'), 'h':float('inf'), 'PX':-1, 'PY':-1} for j in range(COL)
        ] 
        for i in range(ROW)
    ]

    # Open List
    openList = []

    # initialize the source
    cellDetails[SX][SY]['f'] = 0.0
    cellDetails[SX][SY]['g'] = 0.0
    cellDetails[SX][SY]['h'] = 0.0
    cellDetails[SX][SY]['PX'] = SX
    cellDetails[SX][SY]['PY'] = SY

    openList.append([0, SX, SY])

    while(openList and validity):
        
        parent = min(openList)
        # parent = openList.pop()
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
                destinationFound = True
                break
            # check if it is already in closed list or blocked
            elif ((not closedList[parent[1]][parent[2] - 1]) and (not isBlocked(parent[1], parent[2] - 1))):
                # find new values
                newG = cellDetails[parent[1]][parent[2]]['g'] + 1.0 
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
                       
                            
    if destinationFound:
        tracedPath = [] 
        row = cellDetails[DX][DY]['PX']
        col = cellDetails[DX][DY]['PY']
        while(not (row == SX and col == SY)):
            tracedPath.append((row, col))
            x = cellDetails[row][col]['PX']
            y = cellDetails[row][col]['PY']
            row, col = x, y
        return [(SX,SY)] + tracedPath[::-1] +[(DX,DY)]
    else:
        return []

def updateMap(toChange):
    maap = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
    for i in range(len(toChange)):
        maap[toChange[i][0]][toChange[i][1]] = 0
    return maap

# Grid Size
ROW = 4
COL = 3

MAP = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]

SX, SY = 0, 0
DX, DY = 0, 0

source = (2,1)
dest = (3,0)
robo1 = (0, 2)
robo2 = (0, 1)
robo = [robo1, robo2]

source_to_dest = (gen for gen in tracer(source, dest))

pre = next(source_to_dest)
nex = next(source_to_dest)
diff = tuple(numpy.subtract(pre, nex))

path = [[pre, nex]]
i = 0

pre = nex

while(True):
    try:
        nex = next(source_to_dest)
    except:
        break
    if diff == tuple(numpy.subtract(pre, nex)):
        path[i].append(nex)
    else:
        i += 1
        diff = tuple(numpy.subtract(pre, nex))
        path.append([pre])
        path[i].append(nex)
    pre = nex

swarmPaths = []

for i in range(len(path)):
    prevNode = tuple(numpy.add(numpy.subtract(path[i][0], path[i][1]), path[i][0]))
    toChange = []
    toChange.append(path[i][0])
    for r in robo:
        if r != robo[i]:
            toChange.append(r)
    MAP = updateMap(toChange)
    temp = tracer(robo[i], prevNode)
    if temp == []:
        print("Not Possible")
        break
    temp += path[i]
    # print("Path for Robo" + str(i))
    # print(temp)
    robo[i] = temp[-2]
    source = temp[-1]

    swarmPaths.append(' '.join(directions(temp)))
print(swarmPaths)


robo0 = serial.Serial()
robo1 = serial.Serial()

robo0.BaudRate = 9600
robo0.port = "COM14"
robo1.BaudRate = 9600
robo1.port = "COM11"

while(True):
    try:
        if not robo0.is_open or not robo0.is_open:
        robo0.open()
        robo1.open()
    except:
        print("Couldnot Open Port")
    else:
        if robo0.in_waiting and robo1.in_waiting:
            robo0.read()
            robo1.read()

            robo0.write(swarmPaths[0])
            robo1.write(swarmPaths[1])
            break
            
robo0.close()
robo1.close()


