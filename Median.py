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
    newData.sort()
    if m%2 == 0:
        median1=float(newData[m//2])
        median2=float(newData[m//2]-1)
        median=(median1+median2)/2
    else:
        median=newData[m//2]
        print(m)
    print("Median is=> " + str(median))