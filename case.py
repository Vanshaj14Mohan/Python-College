#wap to import a regular statement.
import re #import re to 
a = "welcome to the class"
print(re.search("welcome.*class$", a))
b = "Welcome to Delhi Capital of India..+"
print(re.findall("a",b)) #to find that a number
print(re.findall("\.",b))
print(re.findall("\+",b))

c = "Shubham sir welcomes you to christ university today" #2-3 lines in a string and use the same command
print(re.split("\s", c))
#replace a word now
print(re.sub("today", "now", c)) #sub command-> Substraction/Replace

d = "A good day today now as far as I know this university is quite good so far but yeah the place is good as new"
print(re.sub("as", "was", d))

#Use all the four commands for a particular string only
print("--"*10)
# print(re.search("university.*christ$", d))
print(re.findall("a",d))
print(re.split("\s", d))
print(re.sub("as", "were", d))

#Questions
#1->Explain regular expressions, can give some example too.
#2->What is the name of RegEx module
#3->What is the use of : sub(), findall(), split() in re model explain with example

