try:
    list1 = [1,2,3,4]
    print(list1[4])

    with open("document.txt") as file:

        data = file.readlines()


except FileNotFoundError:

    print("You have deleted the document")

except IndexError as errmsg:
    print("wrong number index" + " "+ "-" +str(errmsg))

finally:
    print("execution stopped")


