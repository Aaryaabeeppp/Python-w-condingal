cp=int(input("enter ur cost price: "))
sp=int(input("enter ur selling price: "))
if sp>cp :
    p=sp-cp
    print ("The profit made is:",p)
else :
    l=cp-sp
    print ("The loss made is:",l)
