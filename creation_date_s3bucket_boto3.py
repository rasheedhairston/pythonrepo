#Import boto3
import boto3

# variable = s3 
s3_resource = boto3.client("s3")

#variable = resource list buckets 
creation_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]

# for bucket in resource print the buckets and creation date 
for bucket in s3_resource.list_buckets() ["Buckets"]:
    print(bucket)
    
