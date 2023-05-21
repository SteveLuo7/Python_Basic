
ages = [12, 23, 26, 63, 45, 12, 36, 18, 45, 78, 3, 6, 8, 9]

x = filter(lambda ele: ele >= 18, ages)

adults = list(x)

print(adults)