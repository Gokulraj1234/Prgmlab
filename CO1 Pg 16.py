word=input("Enter a string:")
str=word.split(" ")
for i in reversed(range(0,len(str))):
    print(str[i],end=" ")
