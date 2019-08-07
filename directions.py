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
        results.append(cases[prev + ' ' + ele])
        prev = ele
    return results

cases = {
    'PX PX':'f',
    'PX NX':'t',
    'PX PY':'a',
    'PX NY':'c',

    'NX NX':'f',
    'NX PX':'t',
    'NX PY':'c',
    'NX NY':'a',

    'PY PY':'f',
    'PY NX':'a',
    'PY NY':'t',
    'PY PX':'c',

    'NY NY':'f',
    'NY NX':'c',
    'PY NY':'t',
    'NY PX':'a',
}
