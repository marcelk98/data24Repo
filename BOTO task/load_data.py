#importing required libraries
from app import *

#function to load the new .csv file into the specified S3 bucket
def load_data():
    s3_client.upload_file(Filename='marcel_fish_test', Bucket=bucket_name, Key='Data100/fish/marcel_fish.csv')
