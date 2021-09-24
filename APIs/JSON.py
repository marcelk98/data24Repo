import json

car_data = {"name":"Tesla", "engine":"Electric"}

# json.dumps() #serisalises json to a formatted string (converts to a string)
# json.dump() #creates a stream object and expects a file object to write to

car_data_json = json.dumps(car_data)

print(car_data_json)

with open("new_json_file", "w") as json_file:
    json.dump(car_data, json_file)

with open("new_json_file") as jsonfile:
    car = json.load(jsonfile)


