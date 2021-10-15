from app import *
from load_data import *


#calling the main program functions
s3_bucket_connection('data-eng-resources')
s3_client_connection(boto3.client('s3'))
exporting_to_csv(main_df, 'functions_test.csv')
load_data('functions_test.csv', 'data-eng-resources', 'Data100/fish/functions_test.csv')

