# AWS Services

import boto3

s3_ob=boto3.resource('s3')#, aws_access_key_id="XXX",
                          #aws_secret_access_key="XXX",
                          #region_name=REGION_NAME)

s3_ob_cli=boto3.client('s3')#, aws_access_key_id="XXX",
                            #aws_secret_access_key="XXX",
                            #region_name=REGION_NAME)

for each_b in s3_ob.buckets.all():
    print(each_b.name)
