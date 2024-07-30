# Var = (1, 2,3, "hello", 5, 6,7, "guys")
# print(type(Var))
# print(Var)
# print(len(Var))

# x1 = []
# print(type(x1))
# x1 = [1, 2, 3 , "bananas", 1, 2,3]
# print(x1)

# var2 = Var
# print(var2)

#wap to add any 5 numbers using python 
# num1 = int(input("enter a number"))
# num2 = int(input("enter a number"))
# num3 = float(input("enter a number"))
# num4 = int(input("enter a number"))
# num5 = float(input("enter a number"))
# res = ("Result is:",num1+num2+num3+num4+num4)
# print(res)

# initial_value = 0
# for i in range(520):
#     number = int(input("enter number {i+1}"))
#     initial_value += number

#     print("total sum is:", initial_value)

#wap add 10 numbers of 2 digits
# number = float(input(f"Enter number {i+1}: "))
#     total += number

# # Print the total sum
# print("The sum of the numbers is:", total) 



# Loop to take input and add numbers
# for i in range(10):
#     number = int(input(f"Enter number {i+1}: "))
#     total += number

# Print the total sum
# print("The sum of the numbers is:", total)


# sum = []
# for i in range(10):
#     name = int(input("enter a number =>"))
#     sum.add(name)
# print(sum)

# Initialize a variable to store the sum
# total = 0

# List of 10 double-digit numbers (you can modify this list as needed)
# numbers = [15, 23, 45, 67, 89, 34, 56, 78, 91, 12]

# Loop through the list and add each number to total
# for number in numbers:
#     total += number

# Print the total sum
# print("The sum of the numbers is:", total)


# import calendar
# print(calendar.month(2022,8))

# import Calculator
# print(Calculator.Add(5,7))
# print(Calculator.Substract(9,5))
# print(Calculator.Multiply(5,4))
# print(Calculator.Divide(12,4))

# name = "Amazing"
# print(name[::-1])

#25/7/243
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
#Create instances
book1 = Book("Xyz abc", "Harneet", 310)
book2 = Book("Abc cde", "Himamshu", 290)

#Display details
print(book1.display_details())
print(book2.display_details())
