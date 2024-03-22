sum = 0
while True:
    num = float(input())
    if num == -1:
        break
    sum += num

print("{:.2f}".format(sum))
