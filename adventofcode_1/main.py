def addition_to_2020(x,y,z):
    if x + y + z == 2020:
        return True
    else:
        return False
full_list = []

with open("input_1") as file:

    data = file.readlines()
    for i in data:
        full_list.append(int(i.replace("\n", "")))

    for i in full_list:
        for j in full_list:
            for t in full_list:
                if addition_to_2020(i,j,t):
                    print(i*j*t)





