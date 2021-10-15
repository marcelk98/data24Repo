#required libraries
import boto3
import pandas as pd


#function to connect to the S3 bucket
def s3_bucket_connection(bucket_name):
    bucket_name = bucket_name
    return bucket_name


#function to connect to the S3 client
def s3_client_connection(s3_client):
    s3_client = s3_client
    return s3_client


#assigning S3 objects to variables for each of the files
s3_object_1 = s3_client_connection(boto3.client('s3')).get_object(Bucket=s3_bucket_connection('data-eng-resources'), Key='python/fish-market.csv')
s3_object_2 = s3_client_connection(boto3.client('s3')).get_object(Bucket=s3_bucket_connection('data-eng-resources'), Key='python/fish-market-tues.csv')
s3_object_3 = s3_client_connection(boto3.client('s3')).get_object(Bucket=s3_bucket_connection('data-eng-resources'), Key='python/fish-market-mon.csv')

#creating a dataframe for each of the files bodies
df_1 = pd.read_csv(s3_object_1['Body'])
df_2 = pd.read_csv(s3_object_2['Body'])
df_3 = pd.read_csv(s3_object_3['Body'])

all_frames = [df_1, df_2, df_3]


#function for concatinating the dataframes
def concat(df_list):
    comb = pd.concat(df_list)
    return comb


comb = concat(all_frames)

#extracting the average values for each category based on 'species' using the new 'comb' dataframe
avg_weight = comb.groupby('Species').Weight.mean()
avg_length1 = comb.groupby('Species').Length1.mean()
avg_length2 = comb.groupby('Species').Length2.mean()
avg_length3 = comb.groupby('Species').Length3.mean()
avg_height = comb.groupby('Species').Height.mean()
avg_width = comb.groupby('Species').Width.mean()

main_df = [avg_width,avg_weight,avg_length1,avg_length2,avg_length3,avg_height]
main_df = concat(main_df)


#function for extracting the data as a .csv file
def exporting_to_csv(data,file):
    data.to_csv(file)