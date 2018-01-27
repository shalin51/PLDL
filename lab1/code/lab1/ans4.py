import  itertools

'sample input'
webStudents=["Shalin","Dev","John","Adarsh","Ravi"]
pythonStudents=["Shalin","Raghav","Jack","Jill","Dev","Ravi"]

'sort both list'
pythonStudents.sort()
webStudents.sort()

'get lenght of both list'
wLen=len(webStudents)
pLen=len(pythonStudents)

'initilize the output variables'
pIndex,wIndex=0,0
commonStudents=[]
uncommonStudent=[]

'logic to findout common and different students'
if wLen>0 and pLen>0:
    if wLen>pLen:
        while (pIndex < pLen):
            if webStudents[wIndex] == pythonStudents[pIndex]:
                commonStudents.append(pythonStudents[pIndex])
                wIndex += 1
                pIndex += 1
            elif webStudents[wIndex] > pythonStudents[pIndex]:
                uncommonStudent.append(pythonStudents[pIndex])
                pIndex+=1
            else:
                uncommonStudent.append(webStudents[wIndex])
                wIndex += 1
        for i in range(wIndex,wLen):
            uncommonStudent.append(webStudents[i])
    else:
        while (wIndex < wLen):
            if webStudents[wIndex] == pythonStudents[pIndex]:
                commonStudents.append(pythonStudents[pIndex])
                wIndex += 1
                pIndex += 1
            elif webStudents[wIndex] > pythonStudents[pIndex]:
                uncommonStudent.append(pythonStudents[pIndex])
                pIndex+=1
            else:
                uncommonStudent.append(webStudents[wIndex])
                wIndex += 1
        for i in range(pIndex,pLen):
            uncommonStudent.append(webStudents[i])


elif wLen>0 and pLen<=0:
    uncommonStudent=webStudents
elif  pLen>0 and wLen<=0:
    uncommonStudent=pythonStudents
else:
    print("List should not be empty")

'print the result'

print("Student who have taken web class")
print(webStudents)

print("Student who have taken python class")
print(pythonStudents)

print("Common Students")
print(commonStudents)
print("Uncommon Students")
print(uncommonStudent)
