#import boto3 
import boto3

# resource is S3 bucket
aws_resource = boto3.resource("s3")

# bucket name is sheedtechnology2 
bucket = aws_resource.Bucket("sheedtechnology2")

#create bucket, public
response = bucket.create(
    ACL='public-read'

    
)

print(response)
