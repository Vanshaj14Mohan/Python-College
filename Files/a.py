a = [10,20,30,40,50]
print(a)
#length+
length_no = len(a)
print(a[0],a[4])
#For checking sum
sum_no = sum(a)
print("Sum is:",sum_no)
#For finding average
avg_no = sum_no/5
print("Average is",avg_no)
print("--"*10)

#2->
import numpy as np
arr_3 =np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_3[0]) #For 0th index
print(arr_3[1]) #For 1th index
print(arr_3[2]) #For 2nd index

#Accessing 0th Index
# print(arr_3[0][0])
# print(arr_3[0][1])
# print(arr_3[0][2])

# print(arr_3[1][0])
# print(arr_3[1][1])
# print(arr_3[1][2])

# print(arr_3[2][0])
# print(arr_3[2][1])
# print(arr_3[2][2])

numbers = [10, 20, 30, 40, 50]
indices = [2, 4]
selected_numbers = [numbers[i] for i in indices]
selected_numbers = [30, 50]
print(selected_numbers)

