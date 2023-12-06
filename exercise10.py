import math

def fib(depth):
    if depth <= 0:
        return 0
    if depth == 1:
        return 1

    return fib(depth - 1) + fib(depth - 2)

print("Fib:")
v = 3
print(f"The {v}. Fibbunaci-number is {fib(v)}.")

# Tests
# Correct functionality
assert fib(3) == 2
assert fib(20) == 6765

# Possible  failures
assert fib(v) > 0, "The result is smaller than 0"
assert fib(0) == 0, "With input 0, result is not 0!"


print("\nApproximation of e:")
def approximation_of_e(depth, power):
    summ = 1

    for i in range(1, depth + 1):
        summ += (power ** i) / (math.factorial(i))

    return summ


v = 10
v2 = 2
r = approximation_of_e(v, v2)
print(f"The approximation of e^{v2} with the depth of {v} is {r}")

# Tests
# Correct functionality
assert 7.38 < approximation_of_e(v, v2) < 7.39
assert 91.41 < approximation_of_e(5, 5) < 92

# Possible failures
assert approximation_of_e(v, v2) > 0, "The result is smaller than 0"
assert approximation_of_e(v, v2) != 0, "The result is 0!"


print("\nCounting down:")
def counting_down(start_value):
    summe = 0

    for i in range(start_value, 0, -1):
        summe += i

    return summe

v = 5
print(f"The result of the first {v} is {counting_down(v)}.")

# Tests
# Correct functionality
assert counting_down(v) == 15
assert counting_down(v) == (v * (v + 1) / 2)

# Possible failures
assert counting_down(v) > 0, "The result is smaller than 0"
assert v > 0, "The input is smaller 0!"


print("\nThird chars:")
def third_char(text: str):
    output = ""

    for letter in range(2, len(text), 3):
        output += text[letter]

    return output


v = "Tippmylitlehonorin"
print(f"The strings {v} every third letter results in {third_char(v)}.")

assert third_char(v) == "python"
assert third_char(v * 2) == "pythonpython"

assert third_char("") == "", "An empty input-string results in an non-empty output string"
assert len(third_char(v)) <= len(v), "The result is longer than the text!"