import os
import boto3

 
AWS_REGION= os.getenv['AWS_REGION']
AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']
DEVICE_NAME = os.environ['DEVICE_NAME']
DISK_SIZE = os.environ['DISK_SIZE']
TAGS = os.environ['TAGS']
SECURITY_GROUP_ID = os.environ['SECURITY_GROUP_ID']

ec2 = boto3.resource('ec2', region_name=AWS_REGION)


def lambda_handler(event, context):


    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        BlockDeviceMappings = [
           {
            'DeviceName': DEVICE_NAME,
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': int(DISK_SIZE),
                'VolumeType': 'gp2'
                 }
            },
        ],
        TagSpecifications=[
          {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': TAGS
                },
              ]
           },
        ],
        SecurityGroupIds= [SECURITY_GROUP_ID],
        MaxCount=1,
        MinCount=1
        
    )
    

    print("New instance created:", instance[0].id)



 