n=int(input("Enter a limit:"))
a=[]
b=[]
print("Enter First and second list:")
for i in range(0,n):
    print("First:",end="")
    a.append(input())
    print("Second:",end="")
    b.append(input())
for i in range(0,n):
    if a[i]==b[i]:
        continue
    else:
        print(a[i])