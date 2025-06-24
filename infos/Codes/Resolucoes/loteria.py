s = list(map(int, input().split()))

c6 = 0
c5 = 0
c4 = 0

while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0, 0, 0]:
        break

    ac = 0
    for num in a:
        if num in s:
            ac += 1

    if ac == 6:
        c6 += 1
    elif ac == 5:
        c5 += 1
    elif ac == 4:
        c4 += 1

print(f"6 {c6}")
print(f"5 {c5}")
print(f"4 {c4}")
