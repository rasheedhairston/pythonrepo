#UPLOAD FILE TO S3

#import boto3
import boto3

# aws resource s3
s3_resource = boto3.client("s3")

#upload file to aws 
s3_resource.upload_file(
    Filename= "cat.png",
    Bucket="sheedtechnology",
    Key="cat.png", )


#LIST FILE IN S3 BUCKET

#import boto3
import boto3

# aws resource s3
s3_resource = boto3.client("s3")

# variable = list objects from bucket name
objects = s3_resource.list_objects(Bucket="sheedtechnology")["Contents"]
 
# print objects in s3 by key name 
for objects in objects:
    print(objects["Key"])
    
    
#DELETE ITEM/ITEMS FROM S3 BUCKET

#import boto3
import boto3

# aws resouce S3
s3_resource = boto3.client("s3")

#delete object from bucket specified
s3_resource.delete_object(Bucket="sheedtechnology" ,
    Key = 'cat.png')
