username = "advait"

# def func():
#     # username = "tiwari"
#     print(username)

# print(username)
# func()

x = 99 # this is global variable

# def func2(y):
#     z = x+y
#     return z

# r = func2(1)
# print(r)

# def func3():
#     x= 88
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myRes = f1()
myRes()

def chai(n):
    def func(x):
        return x ** n
    return func


f = chai(2)
g = chai(3)

print(f(3))
print(g(3))