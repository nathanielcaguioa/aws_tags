from datetime import datetime
import boto3
import json
import os

inputtagkey = os.environ['tagkey']
inputtagvalue = os.environ['tagvalue']
inputregion = os.environ['awsRegion']
inputservername = os.environ['servername']

print(f"'{servername}' and '{awsRegion}'")

    
def get_instance_id_by_name(inputservername):

    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [inputservername]
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

    
    ec2_client = boto3.client('ec2',region_name=aws_region)

    instance_id = get_instance_id_by_name(inputservername)
    if instance_id:
        print(f"Instance ID for '{inputservername}' is: {instance_id}")
        create_new_tags(instance_id, inputtagkey, inputtagvalue)
    else:
        print(f"No instance found with the name '{inputservername}'")

    

