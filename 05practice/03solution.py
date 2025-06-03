def pattern3(n):
    for i in range(n):
        for m in range(i+1):
            print((m+1),end="")
        print()

print(pattern3(4))