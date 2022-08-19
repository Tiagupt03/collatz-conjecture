import matplotlib.pyplot
m=int(input("HOW MANY NUMBERS YOU WANT TO COMPARE? "))
for i in range(m):
    n=int(input("ENTER YOUR NUMBER : "))
    c=0
    x=[0]
    y=[]
    while(1<n):
        c+=1
        y.append(n)
        x.append(c)
        if(n%2==0):
            n=int(n/2)
        else:
            n=(3*n+1)
    else:
        print("PROCESSING COMPLETED......")
    x.pop()    
    print("TOTAL STOPPING TIME IS : ",c)     
    matplotlib.pyplot.plot(x,y,marker="D",linestyle="dashed")
    matplotlib.pyplot.title("THE COLLATZ CONJUCTURE")
    matplotlib.pyplot.xlabel("Iteration number")
    matplotlib.pyplot.ylabel("Value")
