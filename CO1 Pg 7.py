list1=[5,6,7,8,10,20,25]
list2=[5,7,10,6,20,8,29]
s=int(0)
c=int(0)
for i in list1 and list2:
    if len(list1)==len(list2):
        print("Lists have same length")
        break
    else:
        print("Lists have different length")
        break
for i in range(0,len(list1) and len(list2)):
    s=s+list1[i]
    c=c+list2[i]
for i in range(0, len(list1) and len(list2)):
    if s==c:
        print("Sum of values are same")
        break
    else:
        print("Sum of values are different")
        break
print("Elements that matched are:")
l=[]
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i]==list2[j]:
            l.append(list1[i] and list2[j])
        else:
            p=i
            continue
print(l)
