i = 1

while i < 10:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j}", end='\t')
        j += 1

    print()
    i += 1
