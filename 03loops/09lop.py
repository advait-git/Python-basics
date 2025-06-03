items = ["apple","banana","mango","orange","apple"]
unique_item = set()

for i in items:
    if i in unique_item:
        print("Duplicate", i)
        break
    unique_item.add(i)