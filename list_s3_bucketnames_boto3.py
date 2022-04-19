#import boto3
import boto3

#set resource s3 
resource = boto3.resource("s3")

#list s3 bucket names 
for bucket in resource.buckets.all():
    print(bucket.name)
    
