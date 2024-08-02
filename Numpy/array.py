import numpy as np
# arr= np.array([10,20,30,40,50])
# indices = np.array([0,2,4])
# selected_elements = arr[indices]
# print(selected_elements)

#WAP TO FIND MULTIPLE ELEMENTS USING NUMPY FANCY INDEXING ARRAY=[1,2,3,4,5,6,7,8] ELEMENTS TO BE SELECTED =[1,2,5,7]
arr = np.array([1,2,3,4,5,6,7,8])
indices = np.array([1,2,5,7])
elements = arr[indices]
print(elements)

print("--"*10)
# a = np.array([9,8,7,6,5,10,11,1,2])
# new = np.sort(a)
# print("Sorted array:", new)

print("For variables")
a = np.array(["z","b","a","g","h","v"])
new = np.sort(a)
print("Sorted array:", new)

# arr = np.array([9,8,7,6,5,10,11,1,2])
# new = np.sort(arr)
# print("Sorted array:", new)

array1 = np.array([2,3,5,4,6,1])
sorted_array = array1[np.argsort(-array1)] #- sign will sort in descending order
print(sorted_array)

#Wap to find using fancy indexing for sorting of numpy array
b= np.array([20,18,40,39,42])
indices = np.argsort(b)
new_arr = b[indices]
print("Sorted array:", new_arr)

# For descending order
c= np.array([15,10,22,21,16,18,96,90])
indx = np.argsort(c)
new_arr2 = c[indx]
print("Descending array:", new_arr2)

#Wap using fancy indexing for sorting numpy array in random order
rand = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
indices = np.random.permutation(len(rand))
sorted_array = rand[indices]
print(indices)
print("Sorted array:", sorted_array)