x=int(input())
y=int(input())
count=0
for n in range(x,y+1):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            count+=1
print(count)
            
