input_str = "teeteracdacd"

for i in input_str:
    print(i)
    if input_str.count(i)==1:
        print("the single char is : ", i)
        break
