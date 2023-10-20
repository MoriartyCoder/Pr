"""
Data types
1. List all numeric data types that you know and give an example for each.
See point 3.1.

2. Boolean type
• Which values can a boolean variable have?
True/False

• What happens when you add two booleans? Try different combinations.
"""
print(f"T/T: {True + True}\nT/F: {True + False}\nF/F: {False + False}\nT/T/T: {True + True + True}")
# Each True has the value 1 and each False the value 0

"""

3. In Python, we can change the type of a variable by casting it to another type.
• For every of the data types int, float, bool and str, define a variable and assign a valid
value for it.
• Try to cast all the variables to all other data types.
"""

short = 1
iint = 1
long = 1

ffloat = 7.5
double = 7.5

char = 'H'
string = "Hi"  # Actually str

bbool = True

print(f"int to float: {float(iint)}")
print(f"int to bool: {bool(iint)}")
print(f"int to str: {str(iint)}")
print(f"float to int: {int(ffloat)}")
print(f"float to bool: {bool(ffloat)}")
print(f"float to str: {str(ffloat)}")
print(f"bool to int: {int(bbool)}")
print(f"bool to float: {float(bbool)}")
print(f"bool to str: {str(bbool)}")
# print(f"str to int: {int(string)}")   # Results in error
print(f"str to bool: {bool(string)}")
# print(f"str to float: {float(string)}  # Results in error



"""
Strings
1. Use Python to correct the spelling error in the word buuy.
2. Prof. Turtle likes fish very much, thus he accidentally wrote it two times to the list. Please remove the
characters of one of the Fish words.
3. Cucumber was written at the start of the node. Please remove it there and add it to the end of the list.
4. To get a better overview of the list, write each item in a new line and indent it using a tab.
5. Print the list using the print function.
6. What is the length of the final string. What do you note?
"""
# 4
notes = "Cucumber, Please remember to buuy the following things: \
\n\tFish,\n\tShell Polish,\n\tFish,\n\tSlippers.\n"

# 1
notes = notes.replace("buuy", "buy")
print(notes)

# 2
notes = notes.replace("Fish, ", "", 1)
print(notes)

# 3
notes = notes.replace("Cucumber, ", "", 1) + " Cucumber"
print(notes) # 5

# 6
print(f"Final string length: {len(notes)}")