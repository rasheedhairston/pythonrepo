#HOW TO CREATE VPC 

#import boto3
import boto3

# variable = boto3 ec2
aws = boto3.client("ec2")

# create vpc with cidr
aws.create_vpc(CidrBlock='10.0.0.0/16')

#HOW TO DECSRIBE VPCS

#import boto3
import boto3

#variable = boto3 client ec2
aws = boto3.client("ec2")

#variable = describe vpcs
y = aws.describe_vpcs()

# variable = boto3 describe VPCS
no_of_vpcs= y["Vpcs"]

# for vps in variable print vpc ID
for vpc in no_of_vpcs:
    print(vpc["VpcId"])

 #DELETE VPCS USING BOTO3

#import boto3 
import boto3

#variable = boto3 ec2 service
aws = boto3.client("ec2")

#variable = delete vpc and add vpc ID from console
respnse = aws.delete_vpc(
    VpcId = "vpc-0f4ef25bdd3ac180b" ,
    )
