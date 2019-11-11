import logging
import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
import sys
import json
import threading
from boto3.s3.transfer import TransferConfig
import os

bucket_name=sys.argv[1]

BUCKET_NAME = bucket_name

first_file_name=sys.argv[2]

def check_if_bucket_exists(bucket_name):
   s3 = boto3.client('s3')
   response = s3.list_buckets()

   # Output the bucket names
   buckets = response['Buckets']
   
   print(buckets[0])
   
   for i in range(len(buckets)):
       bucket = buckets[i]
       b = bucket['Name']
       print(b)
       if(bucket_name == b):
           return True;


   return False;


def store_file_s3(bucket_name):
    S3 = boto3.client('s3')
    S3.upload_file(first_file_name, bucket_name, first_file_name)

def create_bucket_and_uploads3(bucket_name):

    # Create bucket
    try:
        if (check_if_bucket_exists(bucket_name)):
            print("bucket already exists");
            #multi_part_upload_with_s3()
            store_file_s3(bucket_name)

        else:
            s3_client = boto3.client('s3', region_name='us-east-1')
            location = {'LocationConstraint': 'us-east-1'}
            s3_client.create_bucket(Bucket=bucket_name,
                          CreateBucketConfiguration={
                              'LocationConstraint': 'eu-west-1'})
            
            store_file_s3(bucket_name)
            #multi_part_upload_with_s3()

    except NoCredentialsError:
        print("Credentials not available")
        return False

create_bucket_and_uploads3(bucket_name)





