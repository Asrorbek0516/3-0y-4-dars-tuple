sonlar = (1,2,3,5,6,7,8,9,34,56,78,12)

min = sonlar[0]

for i in sonlar:
    if i < min:
        min = i

print(f"min son: {min}")