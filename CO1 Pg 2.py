c=2021
f= int(input("Enter the final year: "))

if(c<f):
    print("Leap year are:")
    for i in range(c,f):
        if (i % 4 == 0 and i % 100 != 0):
            print(i)
else:
    print("Invalid Year")



