import time

def fitted_print(print_field):
    for line in print_field:
        for e in line:
            print("%2d " % e, end="")
        print("")
    print("")


bIlegalInput = True

while bIlegalInput:
    size = int(input("X: "))
    if size > 0 and size % 2 == 1:
        bIlegalInput = False

time.sleep(10)

print("(a)")
field = []
cnt = 0
for y in range(size):
    field.append([])
    for x in range(size):
        field[y].append(cnt)

        cnt += 1
        cnt %= 2
fitted_print(field)


print("(b)")
field = []
cnt = 1
for y in range(size):
    field.append([])
    for x in range(size):
        field[y].append(cnt)
        cnt += 1
fitted_print(field)


print("(c)")
field = []
cnt = 1
for y in range(size):
    field.append([])
    for x in range(size):
        field[y].append(cnt + size * x)

    cnt += 1
fitted_print(field)


print("(d)")
field = []
cnt = 0
middle = int((size - 1) / 2)
num = middle
for y in range(size):
    field.append([])
    for x in range(size):
        field[y].append(0)

for m in range(middle + 1):
    for y in range(size - 2 * m):
        for x in range(size - 2 * m):
            field[y + cnt][x + cnt] = num
    num -= 1
    cnt += 1

fitted_print(field)


print("(e)")
field = []
cnt = size ** 2
for y in range(size):
    field.append([])
    for x in range(size):
        field[y].append(cnt)
        cnt -= 1
fitted_print(field)


print("(f)")
field = []
cnt = 1
for y in range(size):
    field.append([])
    for x in range(size):
        field[y].append(cnt)
        cnt += 1
    if y % 2 == 1:
        field[y].reverse()
fitted_print(field)


print("(g)")
field = []
cnt = 0
for y in range(size):
    field.append([])
    cnt = y

    for x in range(size):
        n = 1
        if cnt > 0:
            n = 0
        cnt -= 1

        field[y].append(n)
    cnt += 1
fitted_print(field)


print("(h)")
field = []
cnt = int((size - 1) / 2)
for y in range(size):
    field.append([])
    acnt = abs(cnt)

    for x in range(acnt):
        field[y].append(0)

    for x in range(size - 2 * acnt):
        field[y].append(1)

    for x in range(acnt):
        field[y].append(0)

    cnt -= 1
fitted_print(field)


print("(i)")
field = []
cnt = 1
for y in range(size):
    field.append([])
    for x in range(size):
        field[y].append(cnt + x)
    cnt += 1
fitted_print(field)

