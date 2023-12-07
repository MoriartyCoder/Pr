
a = 5

try:
    print(a + b)
except NameError as e:
    print(e)
except:
    print("Doesnt work")