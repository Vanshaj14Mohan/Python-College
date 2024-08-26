#Question 2
arr3 = [2,4,6,8, 10]
arr4 = [1,3,5,7,9]
print(arr3, arr4)
temp1 = arr3
arr3 = arr4
print(temp1, arr3)

#Question 3
import numpy as np

def product_of_list(numbers):
    return np.prod(numbers)

# Example usage
my_list = [10, 20,25, 30, 45]
result = product_of_list(my_list)
print("Product of the list:", result)

#Question 4
arr1 = [12,10,15,25,17]
arr2 = [16,17,19,28,15]
print(arr1[0] == arr2[1])
print(arr1[3] >= arr2[4])
print(arr1[4] <= arr2[3])
print(arr1[2] != arr2[2])



