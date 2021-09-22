def range_of_letters(text):
    text = text.split(':')
    placeholder = text[0].split(" ")
    minimum, maximum = placeholder[0].split("-")
    minimum, maximum = int(minimum),int(maximum)
    return minimum, maximum

def return_password(text):
    text = text.split(':')
    password = text[1].replace(' ', '')
    password = password.replace('\n', '')
    return password

def return_valid_letter(text):
    text = text.split(':')
    return text[0][-1]

with open("input2.txt") as file:
    data = file.readlines()
    valid_passwords_count = 0
    for line in data:
        line = line.replace("\n",'')
        count = 0
        minimum, maximum = range_of_letters(line)
        password = return_password(line)
        letter = return_valid_letter(line)
        if minimum <= password.count(letter) <= maximum:
            valid_passwords_count += 1
    print(valid_passwords_count)
