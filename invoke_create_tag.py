from datetime import datetime
import boto3
import json
import os

def mainFunction():
    inputtagkey = os.environ['tagkey']
    inputtagvalue = os.environ['tagvalue']
    inputsecretid = os.environ['AWS_ACCESS_KEY_ID']
    inputsecretkey = os.environ['AWS_SECRET_ACCESS_KEY']
    print(f"'{inputtagkey}' and '{inputtagvalue}' and '{inputsecretid}' and '{inputsecretkey}'")

with open('serverlists.txt', 'r') as file:
    servernames = [line.strip() for line in file]
    
def get_instance_id_by_name(instance_name):

    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [instance_name]
            }
        ]
    )
    if response['Reservations']:
            instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
            return instance_id
    else:
            return None

def create_new_tags(instance_id, new_tagkey, new_tagvalue):
    ec2_client.create_tags(Resources=[instance_id], Tags=[{'Key': new_tagkey, 'Value': new_tagvalue}])
    print("Tags added successfully.")

        
for instance_name in servernames:

    region_lookup = {
        "USEA":"us-east-1",
        "USWE":"us-west-2",
        "CACE":"ca-central-1",
        "EUWE":"eu-west-1",
        "EUCE":"eu-central-1",
        "APSP":"ap-southeast-1",
        "APAU":"ap-southeast-2"
    }
    aws_region  = region_lookup[instance_name[:4]]
    print(f"'{aws_region}'")
    
    ec2_client = session.client('ec2',region_name=awsregion)

    instance_id = get_instance_id_by_name(instance_name)
    if instance_id:
        print(f"Instance ID for '{instance_name}' is: {instance_id}")
    else:
        print(f"No instance found with the name '{instance_name}'")

    create_new_tags(instance_id, new_tagkey, new_tagvalue)

mainFunction()
