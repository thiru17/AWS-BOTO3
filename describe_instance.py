import json
from datetime import date, datetime
import boto3

AWS_REGION =input("Enter the Region: ") 
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)
INSTANCE_ID = input("Enter the Instance Id: ")

# Helper method to serialize datetime fields
def json_datetime_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


response = EC2_CLIENT.describe_instances(
    InstanceIds=[
        INSTANCE_ID,
    ],
)

print(f'Instance {INSTANCE_ID} attributes:')

for reservation in response['Reservations']:
    print(json.dumps(
            reservation,
            indent=4,
            default=json_datetime_serializer
        )
    )