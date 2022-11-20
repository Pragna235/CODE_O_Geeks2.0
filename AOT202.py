# cook your dish here
cmi,cei=0,0
for n in range(int(input())):
    mi,ei=map(int,input().split())
    if(mi>ei):
        cmi+=1 
    elif (ei>mi):
        cei+=1 
if(cmi>cei):
    print("Mikasa")
elif(cei>cmi):
    print("Eren")
else:
    print("Friendship is magic!")
        
    
