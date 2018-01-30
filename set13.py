num=int(input("Enter the number to be reversed:"))
r=0
while(num>0):
    digit=num%10
    r=r*10+digit
    num=num//10
print("Reverse of the given number:",r)
