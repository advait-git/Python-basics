import math

def area_cir(radius):
    circumference = 2*3.14*radius
    area = 3.14 * (radius **2)
    return area, circumference

a,c = area_cir(3)
print(a,c)