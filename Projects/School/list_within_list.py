'''
for each nested lst, use additonal bracket to call index
'''

myLst = ['a', [1, 2, 3],['x', 'y','z']] 
'''
myLst[1] = [1, 2, 3] # apply left to right
myLst[1][0] = 1
[1, 2, 3][0]  = 1
'''

#print (myLst[1][2])
print (myLst[2][1])