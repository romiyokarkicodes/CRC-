mydata =list()
containerdata =list()
templist =list()
maincounter =0
nullvalue =list(("0","0","0","0"))
mydata =input("Your data in binary format \n")
maincounter =len(mydata)
mydivisor =input("Your divisor \n")
for m in range(len(mydivisor)-1):
    mydata =str(mydata)+str(0)
tocall =mydata[len(mydivisor):]
print(mydata)
mydata =mydata[:len(mydivisor)]
tocall2 =list(tocall)
print(tocall2)
print(mydata)

# degree =len(mydivisor-1)
# print(degree)
countter=0
 #Counter 
while True:
    if(countter==0):
        i=0
        while(i<len(mydata)):  #WE cant use forloop beccause it doesnt allow range conversion in process 
            containerdata.insert(i,str(int(mydata[i])^int(mydivisor[i])))
            i+=1
    if(containerdata[0] ==str(0)):
        print(tocall2)
        if not tocall2 and countter >1:
            print("Lunching")
            m=0
            while(m<len(containerdata)):  #WE cant use forloop beccause it doesnt allow range conversion in process 
                templist.insert(m,str(int(containerdata[m])^int(nullvalue[m])))
                m+=1
            containerdata =templist
            break
        del containerdata[0]
        containerdata.append(tocall2[0])
        
        del tocall2[0]
        j=0
        while(j<len(containerdata)):  #WE cant use forloop beccause it doesnt allow range conversion in process 
            templist.insert(j,str(int(containerdata[j])^int(nullvalue[j])))
            j+=1
        
    else:
        print(tocall2)
        if not tocall2 and countter >1:
            print("Lunching")
            m=0
            while(m<len(containerdata)):  #WE cant use forloop beccause it doesnt allow range conversion in process 
                templist.insert(m,str(int(containerdata[m])^int(mydivisor[m])))
                m+=1
            containerdata =templist
            break
        j=0
        while(j<len(containerdata)):  #WE cant use forloop beccause it doesnt allow range conversion in process 
            templist.insert(j,str(int(containerdata[j])^int(mydivisor[j])))
            j+=1
     
    


    
       
        
        


    containerdata =templist
    templist =list()
    countter+=1

print("The final data to send is "+str(containerdata[-3:]))
    

   