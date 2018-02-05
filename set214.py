
s = input("Enter the string: ")
n = s

vowels = ('a', 'e', 'i', 'o', 'u')
for x in s.lower():
	if x in vowels:
		n = n.replace(x,"")
		
def rev(n):
  str = ""
  for i in n:
    str = i + str
  return str

print (rev(n))
