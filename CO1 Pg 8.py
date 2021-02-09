word=str(input("Enter the data:"))
for i in range(0,len(word)):
    if i==0:
        print(word[i])
    else:
        if word[i] == word[0]:
            print("$")
        else:
            print(word[i])

