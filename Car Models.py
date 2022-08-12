    import numpy as n
a=[]
x1=int(input("Enter the number of models:"))
for i in range(5):
    print("Branch:",i+1)
    temp =[]
    for j in range(x1):
        print("Enter the total sales in model",j+1)
        b=int(input())
        temp.append(b)
        a.append(temp)
c= n.array(a)
d= n.sort(a)
for i in range(5):
    print("Maximum sales in branch ",i+1)
    for j in range(x1):
        if d[i][x1 - 1]==c[i][j]:
            print("Model",j+1)
