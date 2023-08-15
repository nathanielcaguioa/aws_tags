from datetime import datetime
import boto3
import json
import os
inputtagkey = os.environ['tagkey']
inputtagvalue = os.environ['tagvalue']
print(f"'{inputtagkey}' and '{inputtagvalue}'")

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

def create_new_tags(instance_id, inputtagkey, inputtagvalue):
    ec2_client.create_tags(Resources=[instance_id], Tags=[{'Key': inputtagkey, 'Value': inputtagvalue}])
    print("Tags added successfully.")

        
for instance_name in servernames:
    instance_name = instance_name.upper()
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
    
    ec2_client = boto3.client('ec2',region_name=aws_region)

    instance_id = get_instance_id_by_name(instance_name)
    if instance_id:
        print(f"Instance ID for '{instance_name}' is: {instance_id}")
        create_new_tags(instance_id, inputtagkey, inputtagvalue)
    else:
        print(f"No instance found with the name '{instance_name}'")

    

