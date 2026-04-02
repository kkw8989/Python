for i in range(1, 10):
    print(f"# {i}단 #", end= "")
print()

for j in range(1, 10):
    for k in range(2,10):
        print(f"{k}X {j}= {k * j}", end=" ")
    print()