import numpy as np
array = np.array([15,22,33,44,55])
print(array)
result = array + 10
print(result)
result = array + 5.5
print(result)
result = array - 5.5
print(result)
total = np.sum(array)
print(total)
mean = np.mean(array)
print(mean)
max_value = np.max(array)
print(max_value)
#1->Explain in detail numpy 
#2-> Create an array using np and perform addition of any integer value higher than 6.6.
#3-> Create an array and perform substraction of any integer value higher than 17.9. array = [22,34,26,25,24, or any no. higher than 17.9
print("--"*10)
array = np.array([11, 33, 45, 5, 56, 34, 84, 92, 100])
mean = np.mean(array)
print("mean value is:",mean)
max = np.max(array)
print("max value is:",max)
sum = np.sum(array)
print("the sum is:",sum)
min = np.min(array)
print("min value is:",min)
print("--"*10)

b = np.array([15,25,145,120,90])
max_value =np.max(b)
print("max value is:",max_value)
min_value =np.min(b)
print("min value is:",min_value)
mean_value =np.mean(b)
print("mean value is:",mean_value)
sum_value =np.sum(b)
print("total sum is:",sum_value)
multiply = b*2
print("Multipy one:",multiply)
print("--"*15)

#Wap to multiply each element of array by two.
c = np.array([10,20])
res = c * 2  #for multiplication
print("Multiply res is:",res)
new = c **2 #for square root
print("Square root:", new)
com = c > 4
print("Comaprison", com)

d = np.array([5010])
comp = d > 1010
print(comp)
print("--"*10)

#Wap to compare each element to see if it's > 20 , array = [20,21,22,24,25]
new_arr = np.array([25,55,66,58,48])
rem = new_arr >20
print(rem)
#array=[20.5,22.5,23]
#array=[25,55,66,58,48]

#WAP to compare each element to see if it's less than 5
test_arr = np.array([1,2,3,4,5])
less = test_arr < 5
print("Comparison test:", less)
great = test_arr >5
print("Greater Comparison:", great)
print("--"*10)
#.	Equality check:
#equality = array == 3 # Check if each element is equal to 3
#print(equality) # Print the boolean array
e = np.array([1,2.7, 4.9, 3, 5.2])
equality = e == 3
print(equality)
print("--*10")
comparison = e >=3
print("Greater than:",comparison)
less_than = e <=3
print("Less than:",less_than)

#WAP to compare each element to see if it's less than equal to 6
new_arr = np.array([1,12,24,5,4])
compare = new_arr <=6
print("result", compare)
print("--"*10)

#WAP to compare each element to see if it's greater than equal to 5
new_type = np.array([1,3,5,7,8,9])
test_compare = new_type <=5
print("result", test_compare)
print("--"*10)

#Try for all comparsion operators
#also check practice problems shared