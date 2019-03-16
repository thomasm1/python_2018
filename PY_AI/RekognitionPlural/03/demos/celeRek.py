import boto3
import json

import PIL.ImageDraw
import PIL.Image

def DrawBox(draw,boundingBox,width,linecolor):
    boxLeft = float(boundingBox['Left'])
    boxTop = float(boundingBox['Top'])
    boxWidth = float(boundingBox['Width'])
    boxHeight = float(boundingBox['Height'])
    imageWidth = myimage.size[0]
    imageHeight = myimage.size[1]
    rectX1 = imageWidth * boxLeft
    rectX2 = imageHeight * boxTop
    rectY1 = rectX1 + (imageWidth * boxWidth)
    rectY2 = rectX2 + (imageHeight * boxHeight)
    for i in range(0,width):
        draw.rectangle(((rectX1 + i,rectX2 + i),(rectY1 - i,rectY2 - i)), fill=None, outline=linecolor)

rek_client = boto3.client('rekognition','us-east-1')
s3_resource = boto3.resource('s3')
bucket = 'rekog-face-reg'
filename = 'Grant_Russell_Bellemy.jpg'

s3_resource.Bucket('rekog-face-reg').download_file(filename, 'input.jpg')

cele_rsp = rek_client.recognize_celebrities(Image={'S3Object': {'Bucket': bucket,'Name': filename}})

     
celebrityFaces = {}
unrecognizedFaces = {}
draw = {}

celebrityFaces = cele_rsp['CelebrityFaces']
unrecognizedFaces = cele_rsp['UnrecognizedFaces']

with PIL.Image.open('input.jpg') as myimage:
    draw = PIL.ImageDraw.Draw(myimage)
    for celeFace in celebrityFaces:
        print(celeFace['Name'])
        Face = celeFace['Face']
        boundingBox = Face['BoundingBox']
        print(boundingBox)
        DrawBox(draw,boundingBox,4,'red')
    for unknown in unrecognizedFaces:
        boundingBox = unknown['BoundingBox']
        DrawBox(draw,boundingBox,4,"black")

    myimage.save('modified.jpg')
