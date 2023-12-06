"""
1. Create a list that contains the weights of the packages as seen in the image above so that Pip has a
reference of all his packages.
"""
weights_list = [2, 5, 8, 10, 12, 14, 18, 20]
print(weights_list)

"""
2. A new package is arriving for Asmee with a weight of 25. Add it to the list.
"""
weights_list.append(25)
print(weights_list)

"""
3. Pip already handled packages with list index 2-5, remove them from the list.
"""
del weights_list[5]
del weights_list[4]
del weights_list[3]
del weights_list[2]
print(weights_list)

"""
4. Pip now wants to handle the heaviest packages first, sort the list in descending order.
"""
weights_list.sort(reverse=True)
print(weights_list)

"""
5. Oh that was not a good idea, let?s start with the lightest first. Reverse the order of the list.
"""
weights_list.sort()
print(weights_list)

"""
6. Pip notices that it is hard to find the packages only by the weight. He starts to label them with the
names of the receivers.
• Create a list with names for the remaining packages in the correct order of their weights!
• Use zip to create tuples of name and weight pairs for the remaining list elements.
"""
names = ["Adam", "Bob", "Doro", "Prof. Turtle", "Asmee"]
weights_list_with_names = zip(names, weights_list)
# NO PRINT!!!

"""
7. Pip wants to know the weight of the package going to Prof. Turtle. Get it from the tuples created with
zip.
"""
for e in weights_list_with_names:
    if e[0] == "Prof. Turtle":
        print(str(e[1]))

"""
8. Pip notices that it is somehow ine?icient to loop through all packages every time he wants to get the
weight for a given name.
"""
names_and_weights_dict = {}
for i in range(len(names)):
    names_and_weights_dict[names[i]] = weights_list[i]
print(names_and_weights_dict)

"""
9. Pip is not sure if he has shipped Adam’s package already. Use the result from the last exercise to
check that.
"""
print("Adam" in names_and_weights_dict)

"""
10. Get the weight of the packages and change it to gram instead of kg if they are less than 10 kg using
a list comprehension.
"""
weights_list_new = [x if x > 10 else x * 1000 for x in names_and_weights_dict.values()]
print(weights_list_new)

"""
11. Give Pip one entry after the other, order doesn?t matter, until the work is done using the result of
answer 8 B.
"""
for k, v in names_and_weights_dict.items():
    print(f"Key: {k}      Value: {v}")

"""
Sort
Write a program that takes as input the following list of numbers: [1,4,7,3,2,8,6,9,5] and outputs the
list in a sorted order without using the built-in sort function.
"""
numbs = [1, 4, 7, 3, 2, 8, 6, 9, 5]
tmp = 0
for i in range(len(numbs) - 1):
    for o in range(len(numbs) - i - 1):
        if numbs[i] > numbs[i + 1]:
            tmp = numbs[i]
            numbs[i] = numbs[i + 1]
            numbs[i + 1] = tmp
print(numbs)

"""
Pythagoras
For which integers a, b and c applies a2 + b2 = c2?
• Use list comprehensions to create all tuples (a, b, c) where a2 + b2 = c2 applies where a ≤ c,
b ≤ c, c ≤ 100.
"""
n = 100
list_comprehention = [(a, b, c) for a in range(n) for b in range(n) for c in range(n) if a ** 2 + b ** 2 == c ** 2 if
                      a <= c if b <= c if c <= 100]
print(f"Length: {len(list_comprehention)}\n{list_comprehention}")

"""
• Write a script that solves the same problem by using a loop.
"""
list_script = []
for a in range(n):
    for b in range(n):
        for c in range(n):
            if not (a <= c or b <= c or c <= 100):
                continue

            if a ** 2 + b ** 2 == c ** 2:
                list_script.append((a, b, c))
print(len(list_script))
