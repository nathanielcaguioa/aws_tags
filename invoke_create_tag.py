from datetime import datetime
import boto3
import json
import os

def mainFunction():
    inputtagkey = os.environ['tagkey']
    inputtagvalue = os.environ['tagvalue']
    # inputsecretid = os.environ['Pod Exception']
    # inputsecretkey = os.environ['Pod Exception']
    print(f"'{inputtagkey}' and '{inputtagvalue}'")

with open('serverlists.txt', 'r') as file:
    servernames = [line.strip() for line in file]

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


mainFunction()
