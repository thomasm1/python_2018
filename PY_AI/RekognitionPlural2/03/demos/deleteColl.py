import boto3
import json

client = boto3.client('rekognition','us-east-1')

collectID = 'hallPresidents'

response = client.delete_collection(CollectionId=collectID)

print( response['StatusCode'] )