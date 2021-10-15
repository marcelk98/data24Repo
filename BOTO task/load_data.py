#importing required libraries
from app import *

#function to load the new .csv file into the specified S3 bucket
def load_data(file_name,bucket,key):
    s3_client_connection(boto3.client('s3')).upload_file(Filename=file_name, Bucket=bucket, Key=key)


