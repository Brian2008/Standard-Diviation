import csv
with open('Height-Weight.csv',newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)
    fileData.pop(0)
    newData=[]
    for i in range(len(fileData)):
        numb=fileData[i][1]
        newData.append(float(numb))
    m=len(newData)
    total=0
    for x in newData: 
        total+=x
    mean=total/m
    print("Mean is=> "+str(mean))