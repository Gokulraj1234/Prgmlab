word=input("Enter a word:")
n=len(word)
for i in range(0,n):
    if i==0:
        print(word[n-1])
    elif i==n-1:
        print(word[0])
    else:
        print(word[i])
