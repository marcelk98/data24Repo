#required libraries
import boto3
import pandas as pd

#specifying which S3 bucket will be used along wiht the S3 client
bucket_name = 'data-eng-resources'
s3_client = boto3.client('s3')

#assigning S3 objects to variables for each of the files
s3_object_1 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market.csv')
s3_object_2 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-tues.csv')
s3_object_3 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-mon.csv')

#creating a dataframe for each of the files bodies
df_1 = pd.read_csv(s3_object_1['Body'])
df_2 = pd.read_csv(s3_object_2['Body'])
df_3 = pd.read_csv(s3_object_3['Body'])

#concatinating the 3 dataframes into a 'comb' variable
all_frames = [df_1, df_2, df_3]
comb = pd.concat(all_frames)


#extracting the average values for each category based on 'species' using the new 'comb' dataframe
avg_weight = comb.groupby('Species').Weight.mean()
avg_length1 = comb.groupby('Species').Length1.mean()
avg_length2 = comb.groupby('Species').Length2.mean()
avg_length3 = comb.groupby('Species').Length3.mean()
avg_height = comb.groupby('Species').Height.mean()
avg_width = comb.groupby('Species').Width.mean()

data = [avg_width,avg_weight,avg_length1,avg_length2,avg_length3,avg_height]

#function for extracting the data as a .csv file
def exporting_to_csv():
    data_comb = pd.concat(data).to_csv('marcel1_fish.csv')
    return data_comb


