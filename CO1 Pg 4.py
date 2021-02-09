word=input("Enter a sentence:")
counts = dict()
s = word.split()
for word in s:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)

