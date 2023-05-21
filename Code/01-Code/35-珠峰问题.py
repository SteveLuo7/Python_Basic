
height = 0.08 / 1000
count = 0

while True:
    height *= 2
    count += 1

    if height >= 8848.13:
        break
print(count)