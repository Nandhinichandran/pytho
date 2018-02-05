asc = 256
def rep(str):
    n = [0] * asc
    max = -1
    c = ''
    for i in str:
        n[ord(i)]+=1;
 
    for i in str:
        if max < n[ord(i)]:
            max = n[ord(i)]
            c = i
 
    return c
str = input("Enter the string:")
print("Most repeated character:" + rep(str))
