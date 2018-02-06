def rshift(arr, num, s):
    for i in range(num):
        right(arr, s)
 

def right(arr, s):
    temp = arr[0]
    for i in range(s-1):
        arr[i] = arr[i+1]
    arr[s-1] = temp
         
def parray(arr,size):
    for i in range(size):
        print ("%d"% arr[i],end=" ")
arr = []
x=int(input("Enter the array size:"))
p=int(input("Enter the shift key:"))
for i in range(x):
    y=int(input())
    arr.append(y)
rshift(arr, p, x)
parray(arr, x)
