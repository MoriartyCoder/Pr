import math


"""
Assignments and Variables
1. Solve the following tasks using the Python interactive shell.
• Define two variables a and b and assign them the values 8 and 4.
• Build the sum of both variables and store the result in a new variable named c.
• Check what id and data type the c has.
• Create a new variable d and assign the value of c to it.
• Divide c by 3 and overwrite the variable c with the new result.
• What id and data type has c now?
• What id and data type has d?
"""
a = 8
b = 4
c = a + b
print(f"id {id(c)}   data type {c}")
d = c
c = c / 3
print(f"id {id(c)}   data type {c}")
print(f"id {id(d)}   data type {d}")


"""
2. Rewrite the following example to follow the syntax rules and naming conventions of Python:
• Use a Python script for more convenience.
• Note how the error messages tell you what goes wrong.
"""
# Calculate the average age of students
student1 = 20  # years old
student2 = 25
student3 = 23
student4 = 19
student5 = 21
averageStudentAge = (student4 + student5 + student1 + student2 + student3) / 5
print(f"Average Studentage: {averageStudentAge}")

# Or the better way
students = (20, 25, 23, 19, 21)
averageStudentAge = sum(students) / len(students)
print(f"Average Studentage: {averageStudentAge}")


def exercise1():
    def exercise1_function(x):
        # x^3-1.8x^2-1.2x+1.6
        return math.pow(x, 3) - 1.8 * math.pow(x, 2) - 1.2 * x + 1.6

    interval = (0.0, 1.5)

    for i in range(5):
        """
        To determine which half of the interval is closer to y = 0
        the middle of each half gets inputted to the function.
        Depending on which side is closer the interval gets split
        and the process begins again.
        """

        minn = min(interval)
        forth_of_the_interval_difference = (max(interval) - min(interval)) / 4

        # The function input
        leftside_value = minn + forth_of_the_interval_difference
        rightside_value = minn + forth_of_the_interval_difference * 3

        print(f"Function input: LV: {leftside_value}   RV: {rightside_value}")

        leftside_result = exercise1_function(leftside_value)
        rightside_result = exercise1_function(rightside_value)

        print(f"Function results: Left: {leftside_result}    Right: {rightside_result}")

        # Shortcuts
        minn = min(interval)
        maxx = max(interval)

        # Which side is closer to y = 0?
        if abs(leftside_result) < abs(rightside_result):
            print("Left side is closer.")
            # Update the interval
            interval = (minn, minn + (maxx - minn) / 2)
        else:
            print("Right side is closer.")
            interval = (minn + (maxx - minn) / 2, maxx)

        print(f"New Interval: [{min(interval)};{max(interval)}]")
        print("\n")


def exercise2():
    """
    Calculates angels of a rectangle.
    """
    a = 4
    b = 5
    # Calculate length of c
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

    # Calculate angle alpha
    angle_alpha = math.degrees(math.atan(a / b))

    angle_asin = math.asin(a / c)
    angle_cosine = math.cos(angle_alpha)
    angle_tan = angle_asin/angle_cosine

    print(f"{angle_alpha} degrees")
    print(f"Angle alpha via arcsin in degrees: {math.degrees(angle_asin)}")
    print(f"Cos of alpha: {math.degrees(angle_cosine)}")
    print(f"tan via sine/cosine: {math.degrees(angle_tan)}")


def exercise3():
    """
    Calculates the distance between to points which the user can input
    """
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))

    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    print(f"Distance: {distance}")


def exercise4():
    """
    A drone starts at some point and flies up to the height the user inputs and goes to the
    other point at the same height and lands.
    The distance of the flight is to be calculated including the start and the landing.
    """
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))
    height = int(input("Height: "))

    distance = 2 * height + math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    print(f"Traveled distance: {distance}")


def exercise5():
    """
    See function exercise4() but this time we start in a quarter arc and land the same way.
    Because the start and the landing are both together half of an arc the circumference gets
    calculated based on the flight height and divided by 2.
    The distance between the start and landing point must be calculated and then the radius must be
    subtracted for the start and landing and be replaced by distance of the start and landing.
    """
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))
    height = int(input("Height: "))

    # Umfang
    circumference = 2 * height * math.pi

    distance = circumference / 2 + (math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)) - height * 2)

    print(f"Traveled distance: {distance}")


if "__main__" == __name__:
    exercise = 1
    bInputIncorrect = True

    while bInputIncorrect:
        bInputIncorrect = False

        exercise = int(input("Please enter a number between 1 and 5: "))

        if exercise == 1:
            exercise1()
        elif exercise == 2:
            exercise2()
        elif exercise == 3:
            exercise3()
        elif exercise == 4:
            exercise4()
        elif exercise == 5:
            exercise5()
        else:
            bInputIncorrect = True
