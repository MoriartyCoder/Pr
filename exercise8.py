import dis

"""
Task 1
Unfortunately the Python interpreter got sick. But our heroes need to compile some code very urgently!
Can you jump in for the interpreter and generate the byte code for the following source code?
Code:
"""
alice = 5
bruno = 2
charlie = 3
total = alice + bruno + charlie

code = '''
alice = 5
bruno = 2
charlie = 3
total = alice + bruno + charlie
'''
"""
1. Generate the byte code manually without using the dis() function. Write it down on a peace of paper!
"""
"""
2. Verify your answer using the dis() function.
"""
c = compile("alice = 5", "", "single")
print(c.co_code)

c = compile("bruno = 2", "", "single")
print(c.co_code)

c = compile("charlie = 3", "", "single")
print(c.co_code)

c = compile("total = alice + bruno + charlie", "", "single")
print(c.co_code)

"""
3. Draw the stack including the global frame for each single step as done in the lecture script

1)
5
global frame

LOAD_CONST  0 (5)

2)
global frame

STORE_NAME 0 (alice)

3)
2
global frame

LOAD_CONST  1 (2)

4)
global frame

STORE_NAME 1 (bruno)

5)
3
global frame

LOAD_CONST  2 (3)

6)
global frame

STORE_NAME 2 (charlie)

7)
a
global frame

LOAD_NAME 0 (alice)

8)
b
a
global frame

LOAD_NAME 1 (bruno)

9)
7
global frame

BINARY_ADD

10)
charlie
7
global frame

LOAD_NAME 3 (charlie)

11)
10
global frame

BINARY_ADD

12)
global frame

STORE_NAME 4 (total)
"""
c = compile(code, "", "exec")
dis.dis(c)


"""
Task 2
Our heroes try to decrypt the code given below which holds the name of our evil, but there is some bug in
the code.
Code:
"""
code = [77, 56, 114, 34, 46, 100, 32, 111, 69, 69, 23, 10, 118, 11, 129, 77, 105, 23, 7, 89, 108]
for i, c in enumerate(code):
    if i % 2 != 1:
        print(chr(c), end="")