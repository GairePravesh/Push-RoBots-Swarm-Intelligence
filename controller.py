# import serial

# old = serial.Serial()
# old.baudrate = 9600
# old.port = 'COM14'

# new = serial.Serial()
# new.baudrate = 9600
# new.port = 'COM11'

# while(True):
#     if(not old.is_open or not new.is_open):
#         try:
#             old.open()
#             new.open()
#         except:
#             print("Can't connect to bluetooth")   
#             old.close()
#             new.close()

#     elif(old.inWaiting() and new.inWaiting()):
#         old.read()
#         new.read()
#         old.write(b"c")
#         new.write(b"c")

# old.close()
# new.close()

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

    # Open List
    openList = []

    # initialize the source
    cellDetails[SX][SY]['f'] = 0.0
    cellDetails[SX][SY]['g'] = 0.0
    cellDetails[SX][SY]['h'] = 0.0
    cellDetails[SX][SY]['PX'] = SX
    cellDetails[SX][SY]['PY'] = SY

    openList.append([0, SX, SY])

    while(openList and validity and not destinationFound):
        parent = min(openList)
        #parent = openList.pop()
        openList.remove(parent)
        closedList[parent[1]][parent[2]] = True # add to closed list

        # Generate the 4 neighbours in E, W, N & S of the popped cell
        # N -->  North       (i-1, j) 
        # S -->  South       (i+1, j) 
        # E -->  East        (i, j+1) 
        # W -->  West        (i, j-1) 

        for i in range(4):
            if (isValid(parent[1] + neighbours[i][0], parent[2] + neighbours[i][1])):
            # Check if destination is reached
                if((parent[1] + neighbours[i][0], parent[2] + neighbours[i][1]) == (DX, DY)):
                    cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['PX'] = parent[1]
                    cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['PY'] = parent[2]
                    destinationFound = True
                    break
                # check if it is already in closed list or blocked
                elif ((not closedList[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]) and (not isBlocked(parent[1] + neighbours[i][0], parent[2] + neighbours[i][1]))):
                    # find new values
                    newG = cellDetails[parent[1]][parent[2]]['g'] + 1.0
                    newH = calculateH(parent[1] + neighbours[i][0], parent[2] + neighbours[i][1])
                    newF = newG + newH
                    # check if it is in open list
                    # if it is in open list compare and replace if it is better
                    # if it is not in open list, add it and details
                    if ((cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['f'] == float('inf')) or (cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['f'] > newF)):
                        openList.append([newF, parent[1] + neighbours[i][0], parent[2] + neighbours[i][1]])
                        cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['f'] = newF
                        cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['g'] = newG
                        cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['h'] = newH
                        cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['PX'] = parent[1]
                        cellDetails[parent[1] + neighbours[i][0]][parent[2] + neighbours[i][1]]['PY'] = parent[2]

    tracedPath = []                 
                        
    if destinationFound:
        row = cellDetails[DX][DY]['PX']
        col = cellDetails[DX][DY]['PY']
        while(not (row == SX and col == SY)):
            tracedPath.append((row, col))
            x = cellDetails[row][col]['PX']
            y = cellDetails[row][col]['PY']
            row, col = x, y
    return [(SX,SY)] + tracedPath[::-1] +[(DX,DY)]
        

if __name__ == "__main__":

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

    neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
     
    source = (1, 1)
    dest = (3, 2)
    robo1 = (0, 0)
    robo2 = (0, 2)

    source_to_dest = directions(tracer(source, dest))
    print(source_to_dest)

    robo1_to_source = directions(tracer(robo1, source))
    print(robo1_to_source)
    
    robo2_to_source = directions(tracer(robo2, source))
    print(robo2_to_source)


