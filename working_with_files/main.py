# with open("order.txt","r") as file:
#     file_content = file.readlines()
#     for line in file_content:
#         print(line)
#     file.close()



with open("order.txt", "w") as file:

    order_items = ["Fries", "onion rings", "drink"]

    for item in order_items:
        file.write(item + "\n")

