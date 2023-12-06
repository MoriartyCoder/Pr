import datetime

"""
2. An program that prints the biggest one of given numbers a, b and c.
"""
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
maxx = a
if b > maxx:
    maxx = b
if c > maxx:
    maxx = c

print(maxx)
print(max(max(a, b), c))


"""
3. To a given time represented as integer values hours, minutes and seconds, one second should be
added. This means that the time 12:59:59 becomes 13:00:00 o?clock. Read the three values using
input and print the new time to the screen. (From the book Klein 2018, Page 74)
"""
a = int(input("Hour: "))
b = int(input("Minute: "))
c = int(input("Second: "))

now = datetime.datetime.now()
now = datetime.timedelta(hours=a, minutes=b, seconds=c)
print(now)

now_plus_one_second = now + datetime.timedelta(seconds=1)
print(now_plus_one_second)


"""
4. In this exercise, we get to know a special frog that can only be defined by a mathematician. Especially
the kind this frog is crossing roads let us assume that he will not make it very long in the real world. At
his first jump, he manages to jump exactly 1 meter. With the next one, only half it, thus 0.5 meters and
so on. So the distance he covers in total is the account_balance of 1 + 0.5 + 0.25, . . .. Try to find out using Python
if the frog manges to cross a 2.5 meter road.
"""
add = 1
distance = 0
result = False
for i in range(10000):
    distance += add
    add = add / 2

    if distance >= 2.5:
        result = True
        print(f"After {i + 1} iteration 2.5 meters have been reached.")
        break
if not result:
    print(f"After 10000 iterations 2.5 meters could not be reached. Only {distance}.")


"""
5. A smart sales women tries to optimize her business by adjusting the prices of her articles based on
the operating system her customers are using in the following way:
• MacOS users pay 20% extra
• Windows users pay the normal price
• Linux users get 20% off
• Anything else pays 5% more than the regular price 
Implement a program that calculates the price
for a given operating system that can be set using input and test it for MacOS, Windows, Linux
and Android.
"""
OSes = {"MacOS": 1.2,
        "Windows": 1,
        "Linux": 0.8,
        "else": 1.05
        }

price = 1000
os = "Linux"
new_price = price * OSes[os]
print(f"OS-based price: {new_price}")

