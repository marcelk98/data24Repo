#importing the library
from pathlib import Path
from app import *


#creating a debug test which will confirm .csv file's existance with the data
def testing_file_creation(file):
    try:
        my_path = Path(file).resolve(strict=True)
    except FileNotFoundError:
        return ('File not found')
    else:
        return (f'Required file found at: ', {my_path})

