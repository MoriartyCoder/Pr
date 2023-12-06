
x = 10
i = 2


print(f"{x}")
for l in range(i):
    x = x * 2 + 1
    print(f"{x}")

print(f"Res: {x}")

if x > 255:
    print("Too big")