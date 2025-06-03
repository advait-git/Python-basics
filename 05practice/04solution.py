def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end="")
        print()

print(pattern4(4))