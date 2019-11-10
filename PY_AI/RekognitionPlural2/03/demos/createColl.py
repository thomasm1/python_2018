import boto3
import json

client = boto3.client('rekognition','us-east-1')
collectID = 'hallPresidents'

def AddFacialInformation(face_name, filename):
    index_rsp = client.index_faces(
        CollectionId=collectID,
        Image={'S3Object': {'Bucket': 'rekog-face-reg','Name': filename}},
        ExternalImageId=face_name
    )
    print( face_name + '   added')
    
    
create_rsp = client.create_collection(CollectionId=collectID)
retcode = create_rsp['StatusCode']
print( 'Status Code = ' + str(retcode) )
if( retcode != 200 ):
    print( 'could not create collection')
    exit()

AddFacialInformation('BenjaminHarrison','benjamin-harrison-portrait.jpg')
AddFacialInformation('GroverCleveland','grover-cleveland-portrait.jpg')
AddFacialInformation('TheodoreRoosevelt','theodore-roosevelt-portrait.jpg')
AddFacialInformation('WilliamHowardTaft','william-howard-taft-portrait.jpg')
AddFacialInformation('WilliamMcKinley','william-mckinley-portrait.jpg')
