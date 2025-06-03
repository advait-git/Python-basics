def print_kargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kargs(name='advait',power='cute')
print_kargs(name='advait',power='cute',kpi='handsome')