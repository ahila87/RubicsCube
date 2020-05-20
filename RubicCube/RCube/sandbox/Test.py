'''
Created on Sep 23, 2018

@author: ahila
'''
from furl import furl
if __name__ == '__main__':
    pass
#cubeVal=y,y,b,b,o,g,o,b,w,r,b,b,r,b,w,b,w,r,o,g,g,o,r,g,g,b,b,y,y,o,y,g,o,o,o,g,r,w,w,r,y,r,g,o,y,w,y,r,g,w,r,y,w,w
#cubeVal=y,y,b,b,o,g,o,b,w,r,b,b,r,b,w,b,w,r,o,g,g,o,r,g,g,b,b,y,y,o,y,g,o,o,o,g,r,w,w,r,y,r,g,o,y,w,y,r,g,w,r,y,w,w
resultCube = ['f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
#resultCube = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'y', 'r', 'r', 'y', 'r', 'r', 'y', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'o', 'o', 'w', 'o', 'o', 'w', 'o', 'o', 'w', 'w','w','w','w','w','w','r','r','r','o','o','o','y','y','y','y','y','y']
#cubeVal = ['f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'r', 'r', 'r', 't', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 't', 't', 't', 'r', 't', 't', 't', 't', 't', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
#cubeVal = ['f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'l', 'l', 'u', 'l', 'l', 'l', 'l', 'l', 'l', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'u', 'u', 'l', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
#Con1 = [[cubeVal[15],cubeVal[8],cubeVal[47]],[cubeVal[6],cubeVal[45],cubeVal[35]],[cubeVal[51],cubeVal[33],cubeVal[26]],[cubeVal[17],cubeVal[53],cubeVal[24]],[cubeVal[38],cubeVal[18],cubeVal[11]],[cubeVal[36],cubeVal[20],cubeVal[27]],[cubeVal[42],cubeVal[29],cubeVal[0]],[cubeVal[44],cubeVal[2],cubeVal[9]]]
#resultCube = ['o',  'o',  'o',  'o',  'o',  'o',  'o',  'o',  'o',  'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
#cubeVal = ['y',  'b',  'b',  'b',  'o',  'g',  'o',  'b',  'w',  'r', 'b', 'b', 'r', 'b', 'w', 'b', 'w', 'r', 'o', 'g', 'g', 'o', 'r', 'g', 'g', 'b', 'b', 'y', 'y', 'o', 'y', 'g', 'o', 'o', 'o', 'g', 'r', 'w', 'w', 'r', 'y', 'r', 'g', 'o', 'y', 'w', 'y', 'r', 'g', 'w', 'r', 'y', 'w', 'w']
#resultCube = ['o','o','w','o','r','b','g','r','r','r','r','g','o','g','g','b','r','g','w','g','g','o','o','b','w','r','b','y','g','b','y','b','w','o','w','o','r','y','o','w','y','b','w','y','b','y','y','y','b','w','w','y','g','r']


total = 0; 
sublist = [resultCube[i:i+9] for i in range(0,54,9)] 
print(sublist)
for face in range(0,6):
    for elem1 in range(0,8):
        for elem2 in range(elem1+1,9):
            if sublist[face][elem1] ==sublist[face][elem2]:
                total = total +1
            else:
                total = total + 0
                     
print(total)    
randomness = (float(total)/216)*100
print str(int(round(randomness)))