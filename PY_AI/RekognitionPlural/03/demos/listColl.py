import boto3
import json

client = boto3.client('rekognition','us-east-1')
collectID = 'hallPresidents'

response = client.list_faces(
    CollectionId=collectID,
    MaxResults=100
)

print( json.dumps(response, indent=2 ))