#importing the library
from app import *
from load_data import *


#using Pytest to test connection to the correct S3 bucket
def test_s3_bucket_connection():
    assert s3_bucket_connection('data-eng-resources') == 'data-eng-resources'


#using Pytest to test connection to the correct S3 client
def testing_s3_client_connection():
    assert s3_client_connection(boto3.client('s3')) == '<botocore.client.S3 object at 0x7fec1f613970>' or '<botocore.client.S3 object at 0x7fec0a4b9940>'



