
'input numbers'
numbers=[1,0,2,5,-8,-2,9,2,-5,6,1,-4,5,10]
'sort the numbers'
numbers.sort()
'take length of number'
nLen=len(numbers)-1

'number dictionary'
numDict={}

'add all variables to dict'
for n in numbers:
    numDict[n]=n

'index declaration'
innerIndex=0
outerIndex=1

'result variable'
result=list()

'logic to findout zero sum'
while innerIndex<outerIndex:
    outerIndex=innerIndex+1
    for i in range(outerIndex,nLen):
        if (numbers[innerIndex]+numbers[i]) in numDict.values():
            result.append((numbers[innerIndex],numbers[i],-(numbers[innerIndex]+numbers[i])))
        outerIndex += 1
    innerIndex +=1

'print result'
print(result)
