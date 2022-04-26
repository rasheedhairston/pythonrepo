#import boto3
import boto3

#variable = instance ids you want to stop 
ids = ['i-0953cb7a7d7f4e335', "i-045116b6d50784a43"]

#ec2 variable = boto3 resource "ec2"
ec2 = boto3.resource('ec2')

# stop variable ids using instance filter 
ec2.instances.filter(InstanceIds = ids).stop()
    
