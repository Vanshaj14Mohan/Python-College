import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a)
print(b)
print(a+b)
print(a-b)
print(a[0:4]) #slice in array

print("Dot product")
print(np.dot(a,b))
print("--"*10)

#Matrix operation
matrix1 = np.array([[1,2], [3,4]])
matrix2 = np.array([[5,6], [7,8]])
# x = matrix1*matrix2
x = np.matmul(matrix1, matrix2) #matmul used to multiply
print(x)
tran = np.transpose(matrix1)
print(tran)

print("--"*10)
print("for list")
numbers = [10, 20, 30, 40, 50]
total_sum = sum(numbers)
print("Sum of the list is:", total_sum)
average = total_sum/5
print("Average is:", average)
print("--"*10)

#Min & Max value in list
min_value = min(numbers)
print("Min value is:", min_value)
max_value = max(numbers)
print("Max value is:", max_value)

#Sum of all elements in an array
test = np.array([1,2,3,4,5])
sum_check = sum(test)
print("Sum is:",sum_check)
#Mean of an array
mean_check = np.mean(test)
print("Mean is:", mean_check)

#Standard Deviation
std_dev = np.std(test)
print("Standard Deviation:",std_dev)
print("--"*10)

print("Dot product")
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])
# Multiply the two arrays element-wise
product_array = array1 * array2
# Print the result
print("Product of arrays:", product_array)

print("--"*10)
x_no = np.array([1,2,3,4,5])
y_no = np.array([1,2,3,4,5])
are_equal = np.equal(x_no, y_no)
print("both equal?", are_equal)

#Common elements between two elements
array_1 = np.array([1, 2, 3, 4, 5])
array_2 = np.array([4, 5, 6, 7, 8])
#to check common element
common_elem = np.intersect1d(array_1, array_2)
print("Common elements:", common_elem)

#Comparing and finding elements
array_3 = np.array([1, 2, 3, 4, 5])
array_4= np.array([4, 5, 6, 7, 8])

diff_check = np.setdiff1d(array_3, array_4)
diff_check2 = np.setdiff1d(array_4, array_3)
print("Difference in 1", diff_check)
print("Difference in 2", diff_check2)
print("--"*10)