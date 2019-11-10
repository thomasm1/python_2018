from __future__ import print_function

import json
import urllib
import boto3

import PIL.ImageDraw
import PIL.ImageFont
import PIL.Image

print('Loading function')

s3_client = boto3.client('s3')

def DrawBox(myimage,draw,boundingBox,width,linecolor,name):
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
    fontSans = PIL.ImageFont.truetype("FreeSans.ttf", 30)
    draw.text((rectX1 + width,rectX2 + width), name, fill=(255,255,0),font=fontSans)
    for i in range(0,width):
        draw.rectangle(((rectX1 + i,rectX2 + i),(rectY1 - i,rectY2 - i)), fill=None, outline=linecolor)

def RunRekognition(bucket, filename, download_path, upload_path):
    rekog_client = boto3.client('rekognition','us-east-1')
    cele_rsp = rekog_client.recognize_celebrities(Image={'S3Object': {'Bucket': bucket,'Name': filename}})
    celebrityFaces = {}
    unrecognizedFaces = {}
    draw = {}
    celebrityFaces = cele_rsp['CelebrityFaces']
    unrecognizedFaces = cele_rsp['UnrecognizedFaces']
    with PIL.Image.open(download_path) as myimage:
        draw = PIL.ImageDraw.Draw(myimage)
        for celeFace in celebrityFaces:
            name = celeFace['Name']
            print(name)
            Face = celeFace['Face']
            boundingBox = Face['BoundingBox']
            #print(boundingBox)
            DrawBox(myimage,draw,boundingBox,4,'green',name)
        for unknown in unrecognizedFaces:
            boundingBox = unknown['BoundingBox']
            DrawBox(myimage,draw,boundingBox,4,'red','unknown')
    
        myimage.save(upload_path)


def lambda_handler(event, context):
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print('Bucket = %s, Key = %s' % (bucket,key))
        download_path = '/tmp/input.jpg'
        #print(download_path)
        s3_client.download_file(bucket, key, download_path)
        upload_path = '/tmp/output.jpg'
        #print(upload_path)
        RunRekognition(bucket, key, download_path , upload_path )
        s3_client.upload_file(upload_path,bucket, 'output/celeBoxed.jpg')
        s3_client.put_object_acl(ACL='public-read',Bucket=bucket,Key='output/celeBoxed.jpg')
