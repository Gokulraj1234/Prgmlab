a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
i = 1
while i<=a and i<=b:
  if a%i==0 and b%i==0:
    gcd = i
  i = i + 1
print("GCD is", gcd)