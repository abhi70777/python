list_fru = ["apple", "orange", "kiwi"]
list_veg = ["tomato", "onion", "cabbage"]
list_bev = ["pepsi", "7up", "fanta"]

list_fru.append("strawberry")
list_veg.insert(2, "carrot")
list_bev.pop(2)

inventory = [list_bev, list_fru, list_veg]

print(list_fru[0:2])
print(list_veg[:-1])

fru_len = [len(item) for item in list_fru]
print("length of fruits:", fru_len)

print("water" in list_bev)

first_item = (list_fru[0], list_bev[0], list_veg[0])
print(first_item)