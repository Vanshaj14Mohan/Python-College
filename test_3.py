#WAP to Compare Two Arrays for Equality
# Test case 1: Equal arrays
def compare_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
print(compare_arrays(arr1, arr2))  #True

# Test case 2: Unequal arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 6]
print(compare_arrays(arr1, arr2))  #False

#2 WAP to perform Standard Deviation of an Array
