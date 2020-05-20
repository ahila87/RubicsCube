from collections import Counter
from random import choice
def dispatch(parm={}):
    
    httpResponse = {}
   
    if((not('op' in parm)) or (parm['op'] != 'create') and (parm['op'] != 'check') and (parm['op'] != 'rotate') and (parm['op'] != 'scramble') ):
        httpResponse['status'] = 'error: op code is missing'        
                 
    elif(parm['op'] == 'create'): 
        httpResponse = createOP(parm)
    elif (parm['op'] == 'check'): 
        httpResponse = checkOP(parm)
    elif (parm['op'] == 'rotate'):            
        httpResponse = rotateOP(parm)    
    elif (parm['op'] == 'scramble'):            
        httpResponse = scrambleOP(parm) 
        
    return httpResponse
           
#Createop function          
def createOP (parm):
    httpResponse = {}
            
    if '' in parm.values() :
        httpResponse['status'] = 'error: face color is missing'               
        
    else:             
        result = createCube(parm)
        if len(set(result)) != 6: 
            httpResponse['status'] = 'error: at least two faces have the same color' 
                 
        else:
            httpResponse['status'] = 'created'          
            httpResponse['cube'] = result
    return httpResponse


# #------ inward facing methods ------

def createCube(parm):
    parm1 = {'op':'create', 'f':'f', 'r':'r', 'b':'b', 'l':'l', 't':'t', 'u':'u'}  
    colors = {'f':'green', 'r':'yellow', 'b':'blue', 'l':'white', 't':'red', 'u':'orange'} 
    cube = []  
       
    if parm == {'op': 'create'}:                   
        actualFaces = ['f', 'r', 'b', 'l', 't', 'u']     
        for faces in actualFaces:        
            for _ in range(0,9):
                cube.append(colors[faces])    
          
    elif parm.keys() == parm1.keys():                  
        actualFaces = ['f', 'r', 'b', 'l', 't', 'u']     
        for faces in actualFaces:        
            for _ in range(0,9):
                cube.append(parm[faces])

    elif  parm.keys() != parm1.keys():        
        actualFaces = ['f', 'r', 'b', 'l', 't', 'u']     
        for faces in actualFaces:
            for _ in range(0,9):
                if faces not in parm.keys():
                    cube.append(colors[faces])
                else:
                    cube.append(parm[faces])       
    return cube


#Check Operation Function

def checkOP(parm):
         
    httpResponse = {} 
    if(not('cube' in parm)):
        httpResponse['status'] = 'error: cube must be specified' 
        return httpResponse  
    
    val = parm['cube']
    cubeVal=val.split(',')      
    
    if cubeVal == ['']: 
        httpResponse['status'] = 'error: cube is empty'
        return httpResponse    

    parm.pop('cube')  
    parm['op'] = 'create'               
    result = createOP(parm)    
    
    if 'cube' not in result:
        return result
    resultCube = result['cube'] 

    status = validateCube(cubeVal,resultCube)
    if 'valid' not in status:
        httpResponse['status'] = status            
           
    else:   
        httpResponse['status'] = checkPattern(resultCube,cubeVal)

    return httpResponse


def checkPattern(resultCube,cubeVal):
    
    resultFull = checkIsFull(resultCube,cubeVal)
    resultSpots = checkIsSpots(cubeVal)
    resultCrosses = checkIsCrosses(cubeVal)
    if resultFull =='Full':
        result = 'full'                        
    elif resultSpots =='Spots':
        result = 'spots'
    elif resultCrosses == 'Crosses':
        result = 'crosses'          
    else:
        result = 'unknown'
    return result
    

def checkIsFull(resultCube,cubeVal):
    if cubeVal == resultCube:
        return 'Full'
    else:
        return
    
     
def checkIsSpots(cubeVal):
    sublist = [cubeVal[i:i+9] for i in range(0,54,9)] 
    for i in range(0,6):
        if (len(set(sublist[i]))) != 2:
            return
         
    for x in range(0,6):
        for y in [0,1,2,3,5,6,7,8]:
            if sublist[x][y]==sublist[x][4]:
                return
 
    return 'Spots'
 
def checkIsCrosses(cubeVal):
    sublist = [cubeVal[i:i+9] for i in range(0,54,9)] 
    for i in range(0,6):
        if (len(set(sublist[i]))) != 2:
            return
         
    for x in range(0,6):
        for y in [1,3,5,7]:
            if sublist[x][y]!=sublist[x][4]:
                return
 
    return 'Crosses' 

def validateCorners(cubeVal,resultCube):
    count =0 
    corners = [[cubeVal[15],cubeVal[8],cubeVal[47]],[cubeVal[6],cubeVal[45],cubeVal[35]],[cubeVal[51],cubeVal[33],cubeVal[26]],[cubeVal[17],cubeVal[53],cubeVal[24]],[cubeVal[38],cubeVal[18],cubeVal[11]],[cubeVal[36],cubeVal[20],cubeVal[27]],[cubeVal[42],cubeVal[29],cubeVal[0]],[cubeVal[44],cubeVal[2],cubeVal[9]]]
    sortCon= [sorted(i) for i in corners]
    dupCorner = sum(y for y in Counter(tuple(x) for x in sortCon).values() if y > 1)
    if dupCorner > 0:
        return 'invalid'
    
    result = [[resultCube[15],resultCube[8],resultCube[47]],[resultCube[6],resultCube[45],resultCube[35]],[resultCube[51],resultCube[33],resultCube[26]],[resultCube[17],resultCube[53],resultCube[24]],[resultCube[38],resultCube[18],resultCube[11]],[resultCube[36],resultCube[20],resultCube[27]],[resultCube[42],resultCube[29],resultCube[0]],[resultCube[44],resultCube[2],resultCube[9]]]
     
    for i in result:        
        for j in corners:
            if (Counter(i) == Counter(j)):
                count+=1
                 
    if count != 8:
        return 'invalid'
    else:
        return
    
def validateEdges(cubeVal,resultCube):
    count = 0  
    edges = [[cubeVal[43],cubeVal[1]],[cubeVal[39],cubeVal[28]],[cubeVal[37],cubeVal[19]],[cubeVal[41],cubeVal[10]],[cubeVal[46],cubeVal[7]],[cubeVal[48],cubeVal[34]],[cubeVal[52],cubeVal[25]],[cubeVal[50],cubeVal[16]],[cubeVal[5],cubeVal[12]],[cubeVal[3],cubeVal[32]],[cubeVal[21],cubeVal[14]],[cubeVal[23],cubeVal[30]]]
    sortEdge = [sorted(i) for i in edges]
    dupEdge = sum(y for y in Counter(tuple(x) for x in sortEdge).values() if y > 1)
    if dupEdge > 0:
        return 'invalid'
        

    result = [[resultCube[43],resultCube[1]],[resultCube[39],resultCube[28]],[resultCube[37],resultCube[19]],[resultCube[41],resultCube[10]],[resultCube[46],resultCube[7]],[resultCube[48],resultCube[34]],[resultCube[52],resultCube[25]],[resultCube[50],resultCube[16]],[resultCube[5],resultCube[12]],[resultCube[3],resultCube[32]],[resultCube[21],resultCube[14]],[resultCube[23],resultCube[30]]]
    for i in result:
        for j in edges:
            if (Counter(i) == Counter(j)):
                count+=1
                 
    if count != 12:
        return 'invalid'
    else:
        return
    

def validateCube(cubeVal,resultCube):
    var =list(set(cubeVal))       
 
    if len(cubeVal)!= 54:
        status = 'error: cube is not sized properly'
    elif len(set(cubeVal))!=6:
        status = 'error: cube does not contain 6 unique colors' 
    elif any(cubeVal[i]!= resultCube[i] for i in [4,13,22,31,40,49]):
        status = 'error: illegal cube'
    elif any(cubeVal.count(var[i])!=9 for i in range(0,6)):
        status = 'error: illegal cube'
    elif validateCorners(cubeVal,resultCube) == 'invalid':
        status = 'error: illegal cube with wrong corners'
    elif validateEdges(cubeVal,resultCube) == 'invalid':
        status = 'error: illegal cube with wrong edges' 
    else:
        status = 'valid'        
        
    return status 

# rotate operation function    
def rotateOP(parm):
   
    httpResponse = {} 
    
    if(not('cube' in parm)):       
        httpResponse['status'] = 'error: cube must be specified'         
        return httpResponse  
    
    if(not('face' in parm)):
        httpResponse['status'] = 'error: face is missing' 
        return httpResponse 
    
    val = parm['cube']
    cubeVal=val.split(',')  
    face = parm['face']    
    
    if cubeVal == ['']: 
        httpResponse['status'] = 'error: cube is empty'
        return httpResponse  
    
    if not face:
        httpResponse['status'] = 'error: face is empty'
        return httpResponse
    
    if face not in ['f', 'F', 'r', 'R', 'b', 'B', 'l', 'L', 't', 'T', 'u', 'U']:
        httpResponse['status'] = 'error: face is unknown'
        return httpResponse 
    
    parm.pop('cube') 
    parm.pop('face') 
    parm['op'] = 'create'     
                
    result = createOP(parm) 
    if 'cube' not in result:
        return result

    resultCube = result['cube']        
    status = validateCube(cubeVal,resultCube)
    
    if 'valid' not in status:
        httpResponse['status'] = status
        
    else:   
        httpResponse['status'] = 'rotated'
        httpResponse['cube'] = cubeRotation(cubeVal,face)
        
    return httpResponse
         
         
def cubeRotation(cubeVal,face):    
    rotatedCube = list(cubeVal)     
 
    if face == 'f':          
        for i,j in zip([9,12,15], [42,43,44]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([29,32,35], [45,46,47]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([42,43,44], [35,32,29]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([45,46,47], [15,12,9]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([0,1,2,3,4,5,6,7,8], [6,3,0,7,4,1,8,5,2]): rotatedCube[i] = cubeVal[j] 
        
    elif face == 'F':        
        for i,j in zip([9,12,15], [47,46,45]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([29,32,35], [44,43,42]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([42,43,44], [9,12,15]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([45,46,47], [29,32,35]): rotatedCube[i] = cubeVal[j] 
        for i,j in zip([0,1,2,3,4,5,6,7,8], [2,5,8,1,4,7,0,3,6]): rotatedCube[i] = cubeVal[j] 
        
        
    elif face == 'r':
        for i,j in zip([2,5,8], [47,50,53]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([18,21,24], [44,41,38]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([38,41,44], [2,5,8]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([47,50,53], [24,21,18]): rotatedCube[i] = cubeVal[j] 
        for i,j in zip([9,10,11,12,13,14,15,16,17], [15,12,9,16,13,10,17,14,11]): rotatedCube[i] = cubeVal[j] 
        
    elif face == 'R':        
        for i,j in zip([2,5,8], [38,41,44]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([18,21,24], [53,50,47]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([38,41,44], [24,21,18]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([47,50,53], [2,5,8]): rotatedCube[i] = cubeVal[j]  
        for i,j in zip([9,10,11,12,13,14,15,16,17], [11,14,17,10,13,16,9,12,15]): rotatedCube[i] = cubeVal[j]   
        
        
    elif face == 'b':
        for i,j in zip([11,14,17], [53,52,51]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([27,30,33], [38,37,36]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([36,37,38], [11,14,17]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([51,52,53], [27,30,33]): rotatedCube[i] = cubeVal[j]  
        for i,j in zip([18,19,20,21,22,23,24,25,26], [24,21,18,25,22,19,26,23,20]): rotatedCube[i] = cubeVal[j]   
        
    elif face == 'B':        
        for i,j in zip([11,14,17], [36,37,38]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([27,30,33], [51,52,53]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([36,37,38], [33,30,27]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([51,52,53], [17,14,11]): rotatedCube[i] = cubeVal[j] 
        for i,j in zip([18,19,20,21,22,23,24,25,26], [20,23,26,19,22,25,18,21,24]): rotatedCube[i] = cubeVal[j]  
        
    elif face == 'l':
        for i,j in zip([0,3,6], [36,39,42]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([20,23,26], [51,48,45]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([36,39,42], [26,23,20]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([45,48,51], [0,3,6]): rotatedCube[i] = cubeVal[j] 
        for i,j in zip([27,28,29,30,31,32,33,34,35], [33,30,27,34,31,28,35,32,29]): rotatedCube[i] = cubeVal[j]
        
    elif face == 'L':        
        for i,j in zip([0,3,6], [45,48,51]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([20,23,26], [42,39,36]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([36,39,42], [0,3,6]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([45,48,51], [26,23,20]): rotatedCube[i] = cubeVal[j]  
        for i,j in zip([27,28,29,30,31,32,33,34,35], [29,32,35,28,31,34,27,30,33]): rotatedCube[i] = cubeVal[j]  
        
    elif face == 't':        
        for i,j in zip([0,1,2], [9,10,11]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([9,10,11], [18,19,20]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([18,19,20], [27,28,29]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([27,28,29], [0,1,2]): rotatedCube[i] = cubeVal[j] 
        for i,j in zip([36,37,38,39,40,41,42,43,44], [42,39,36,43,40,37,44,41,38]): rotatedCube[i] = cubeVal[j]
        
    elif face == 'T':        
        for i,j in zip([0,1,2], [27,28,29]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([9,10,11], [0,1,2]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([18,19,20], [9,10,11]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([27,28,29], [18,19,20]): rotatedCube[i] = cubeVal[j] 
        for i,j in zip([36,37,38,39,40,41,42,43,44], [38,41,44,37,40,43,36,39,42]): rotatedCube[i] = cubeVal[j]  
        
    elif face == 'u':        
        for i,j in zip([6,7,8], [33,34,35]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([15,16,17], [6,7,8]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([24,25,26], [15,16,17]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([33,34,35], [24,25,26]): rotatedCube[i] = cubeVal[j] 
        for i,j in zip([45,46,47,48,49,50,51,52,53], [51,48,45,52,49,46,53,50,47]): rotatedCube[i] = cubeVal[j] 
        
    elif face == 'U':        
        for i,j in zip([6,7,8], [15,16,17]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([15,16,17], [24,25,26]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([24,25,26], [33,34,35]): rotatedCube[i] = cubeVal[j]
        for i,j in zip([33,34,35], [6,7,8]): rotatedCube[i] = cubeVal[j]   
        for i,j in zip([45,46,47,48,49,50,51,52,53], [47,50,53,46,49,52,45,48,51]): rotatedCube[i] = cubeVal[j]
           
    return rotatedCube

# Scramble operation function
def scrambleOP(parm):
    httpResponse = {} 
    if(not('method' in parm)):
        parm.update( {'method' : 'random'} )  
    if (parm['method']!= 'random' and parm['method']!= 'transition') :
        httpResponse['status'] = 'error: method is unknown'  
        return httpResponse 
     
    if(not('n' in parm)):
        parm.update( {'n' : 0} )     
    elif parm['n'].lstrip('+-').isdigit():
        parm['n'] = int(parm['n'])  
        
    if (not(isinstance(parm['n'],int)))or (parm['n']<0 or parm['n']>99):
        httpResponse['status'] = 'error: n is invalid'
        return httpResponse
    
    
    if parm['method'] == 'random':
        httpResponse = random(parm)
        return httpResponse
    elif parm['method'] == 'transition':
        httpResponse = transition(parm)
        return httpResponse
        
    
def random(parm):
    httpResponse = {}    
    rotations = []
    direction = ['f','F', 'r','R', 'b','B', 'l','L', 't','T', 'u','U'] 
    cubeVal = ['f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
    if parm['n'] == 0:
        randomness = randomnessCalc(cubeVal)
        httpResponse['status'] = 'scrambled'+' ' +str(randomness)
        httpResponse['rotations'] = []
    else:
        for _ in range (0,parm['n']): 
            FaceDir =  choice(direction)           
            cubeVal = cubeRotation(cubeVal,FaceDir)            
            randomness = randomnessCalc(cubeVal)           
            httpResponse['status'] = 'scrambled'+' ' +randomness            
            rotations.append(FaceDir)            
            httpResponse['rotations'] = rotations
            
    return httpResponse


def randomnessCalc(cubeVal):
     
    total = 0; 
    sublist = [cubeVal[i:i+9] for i in range(0,54,9)]    
    for face in range(0,6):
        for elem1 in range(0,8):
            for elem2 in range(elem1+1,9):
                if sublist[face][elem1] ==sublist[face][elem2]:
                    total = total +1
                else:
                    total = total + 0                     
      
    randomness = (float(total)/216)*100
    return str(int(round(randomness)))

def transition(parm):    
    httpResponse = {}
    rotations = []
    randomnessDict={}
    direction = ['f','F', 'r','R', 'b','B', 'l','L', 't','T', 'u','U'] 
    cubeVal = ['f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
    if parm['n'] == 0:
        randomness = randomnessCalc(cubeVal)
        httpResponse['status'] = 'scrambled'+' ' +str(randomness)
        httpResponse['rotations'] = []
    else:
        for _ in range(0,parm['n']):  
            randomnessDict = {}
            for i in direction:
                resultCube = cubeRotation(cubeVal,i) 
                randomness = randomnessCalc(resultCube) 
                randomnessDict.update( {i : int(randomness)} )                
            mn = min(randomnessDict.values())
            minList = ([k for k, v in randomnessDict.items() if v == mn])            
            minimum = choice(minList)                    
            cubeVal = cubeRotation(cubeVal,minimum)            
            rotations.append(minimum)
        randomness = randomnessDict[minimum]    
        httpResponse['status'] = 'scrambled'+' ' +str(randomness)      
        httpResponse['rotations'] = rotations
    return httpResponse