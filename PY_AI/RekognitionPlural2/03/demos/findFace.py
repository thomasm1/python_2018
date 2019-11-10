import boto3
import json

client = boto3.client('rekognition','us-east-1')

collectID = 'hallPresidents'

find_rsp = client.search_faces_by_image(
		Image={
			"S3Object": {
				"Bucket": 'rekog-face-reg',
				"Name": 'Cleveland2.jpg',
			}
		},
		CollectionId=collectID,
		FaceMatchThreshold=85
	)

FaceMatches = find_rsp['FaceMatches']

faceCount = len( FaceMatches ) 

print( 'matches = ' + str(faceCount))
if( faceCount > 0 ):
    for match in FaceMatches:
        face = match['Face']
        #print( json.dumps( face , indent=2))
        print('   Facial Match = ' + face['ExternalImageId'])
