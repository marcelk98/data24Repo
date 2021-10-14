#importing the library
from pathlib import Path


#creating a test which will confirm .csv file existance with the data
def testing_file_creation():
    try:
        my_abs_path = Path('marcel_fish.csv').resolve(strict=True)
    except FileNotFoundError:
        print('File not found')
    else:
        print('Required file found')


