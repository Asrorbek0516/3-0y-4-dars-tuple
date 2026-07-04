sonlar = (1,2,3,5,6,7,8,9,34,56,78,12)

soni = 0

for i in sonlar:
    if i % 2 != 0:
        soni += 1

print(f"toq sonlar soni: {soni}")