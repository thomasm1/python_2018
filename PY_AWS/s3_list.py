# AWS Services

import boto3
s3=boto3.resource('s3')
buckets=s3.buckets.all()
for bucket in buckets:
    print (bucket.name)
    
