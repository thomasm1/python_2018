import boto3

s3=boto3.client('s3')
s3.upload_file('S3_transfer.txt','rewrite-streaming-dev','S3_script.txt')
