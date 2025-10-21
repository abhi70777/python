web = ["sena", "daryl", "carol"]
data = ["rick", "dixon", "teena"]
ui = ["jenny", "robert", "chris"]

all_participants = [web, data, ui]

web.append("rock")

data.insert(2, "aloshy")

ui.pop()

new_data = data.copy()
data.clear()

print(web[0:2])

name_len = [len(name) for name in new_data]
print(name_len)

print("asha" in (web, new_data, ui))

first_name = (web[0], new_data[0], ui[0])
print(first_name)