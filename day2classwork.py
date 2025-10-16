
header = "********** BOOKSTORE RECEIPT **********\nDATE: 16-10-2025\n----------------------------------------\n"


book1_title = "Python Basics"
book1_price = 450
book2_title = "Data Science Intro"
book2_price = 600


a = "{}\t\t₹{}".format(book1_title, book1_price)
b = "{}\t₹{}".format(book2_title, book2_price)


total = book1_price + book2_price
final = "TOTAL\t\t₹{}".format(total)


thank_you = "\n----------------------------------------\nTHANK YOU FOR SHOPPING WITH US!"

receipt = header + a + "\n" + b + "\n" + final + thank_you
print(receipt.upper())

