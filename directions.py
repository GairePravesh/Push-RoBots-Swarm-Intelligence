'''
Pravesh Gaire
7/10/2019

Converts the point form output to useable direction format
'''
def movingAxis(tracedPath):
    prev = tracedPath[0]
    direction = []
    for ele in tracedPath:
        res = [ele[0] - prev[0], ele[1] - prev[1]]
        prev = ele
        if res == [1, 0]:
            direction.append('PX')
        if res == [-1, 0]:
            direction.append('NX')
        if res == [0, 1]:
            direction.append('PY')
        if res == [0, -1]:
            direction.append('NY')
    return direction

def directions(tracedPath):
    inputs = movingAxis(tracedPath)
    prev = 'PX'
    results = []
    for ele in inputs:
        #print(prev + ' ' + ele)
        #print(cases[prev + ' ' + ele])
        results.append(cases[prev + ' ' + ele])
        prev = ele
    return results

cases = {
    'PX PX':'F',
    'PX NX':'R180 F',
    'PX PY':'A90 F',
    'PX NY':'C90 F',

    'NX NX':'F',
    'NX PX':'R180 F',
    'NX PY':'C90 F',
    'NX NY':'A90 F',

    'PY PY':'F',
    'PY NX':'A90 F',
    'PY NY':'R180 F',
    'PY PX':'C90 F',

    'NY NY':'F',
    'NY NX':'C90 F',
    'PY NY':'R180 F',
    'NY PX':'A90 F',
}
