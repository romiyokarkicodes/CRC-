from typing import Counter, final


mydata =list()
containerdata =list()
templist =list()
nullvalue =list(("0","0","0","0"))
mydata =input("Your data in binary format \n")
mydivisor =input("Your divisor \n")
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
        del containerdata[0]
        containerdata.append(str(0))
        j=0
        while(j<len(containerdata)):  #WE cant use forloop beccause it doesnt allow range conversion in process 
            templist.insert(j,str(int(containerdata[j])^int(nullvalue[j])))
            j+=1
    else:
        j=0
        while(j<len(containerdata)):  #WE cant use forloop beccause it doesnt allow range conversion in process 
            templist.insert(j,str(int(containerdata[j])^int(mydivisor[j])))
            j+=1
     
    


    
       
        
        


    containerdata =templist
    templist =list()
    countter+=1
    if(countter==len(mydata)):
        break
if(containerdata[0] ==str(0)):
    del containerdata[0]
print("Your previous data is "+mydata)
final =mydata+str(''.join(containerdata))
print("The final data to send is "+final)