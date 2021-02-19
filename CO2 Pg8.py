n=int(input("Enter a limit:"))
print("Enter the list of words:")
l=[]
h=[]
for i in range(0,n):
    l.append(input())
for i in range(0,n):
    h.append(len(l[i]))
    h.sort()
print(h[-1:])

