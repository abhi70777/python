grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)
    print("Added " + item)


def remove_last_item():
    print("Removed " + grocery_list.pop())
    
def display_list():
    for item in grocery_list:
        print("Item:", item)


def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

print("Initial list:")
display_list()

add_item("butter")
add_item("apples")

print("\nUpdated list:")
display_list()

remove_last_item()

print("\nAfter removing last item:")
display_list()

print("\nTotal characters:", count_characters(grocery_list))
