import csv

with open("user_details.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        print(row[-1])

#no headers
   # csvreader = list(csvreader[1:])
   #  print(csvreader)

# def transform_user_details(csv_file_name):
#     new_user_data = []
#     with open(csv_file_name) as csvfile:
#         user_details_csv = csv.reader(csvfile, delimiter = ",")
#
#     for user in user_details_csv:
#         transformation = []
#         transformation.append(user[1])
#         transformation.append(user[2])
#         transformation.append(user[-1])
#         new_user_data.append(transformation)
#
#         return new_user_data
#
# transform_user_details("user_details.csv")
#
# with open("user_details.csv") as file:
#     csvreader = csv.reader(file)
#
#     for row in csvreader:
#         print(row)