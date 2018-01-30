s1=input("enter the 1st string:")
s2=input("enter the 2nd string:")
MAX_CHARS = 256
def iso(string1, string2):
	m = len(string1)
	n = len(string2)
	if m != n:
		return "Not isomorphic."
	t = [False] * MAX_CHARS
	map = [-1] * MAX_CHARS
	for i in range(n):
		if map[ord(string1[i])] == -1:
			if t[ord(string2[i])] == True:
				return "Not isomorphic."
			t[ord(string2[i])] = True
			map[ord(string1[i])] = string2[i]
		elif map[ord(string1[i])] != string2[i]:
			return "Not isomorphic."
	return "Yes"
print (iso(s1,s2))
