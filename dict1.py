exDict = {'Jack':[15, 'blonde'], 'BoB':[22,'brawn'], 'Alice':[12, 'black'], 'Kevin':[17, 'red']}

print(exDict['Jack'])

exDict['Tim'] = 14

print(exDict)

exDict['Tim'] = 15

del exDict['Tim']

print(exDict)

print(exDict['Jack'])
print(exDict['Jack'][1])