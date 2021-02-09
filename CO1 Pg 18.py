def Merge(dict1, dict2):
    return(dict2.update(dict1))     
dict1 = {'a': 10, 'b': 20}
dict2 = {'d': 14, 'c': 44}
print(Merge(dict1, dict2))
print("After Merging",dict2)