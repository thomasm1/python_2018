#!/bin/bash
export S3_BUCKET=example.com-cdn # The site bucket name
export BUILD_DIR=public  # The build directory created by your static site generator

rm -rf $BUILD_DIR
hugo # Set the command to build your static site here

# You need to set up a profile in your AWS CLI credentials
# file or remove the profile tag to use the main profile
aws --profile static-site s3 sync $BUILD_DIR/ s3://$S3_BUCKET/ --delete
