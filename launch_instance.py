import boto3

AWS_REGION = "us-east-1"                                            # give Aws region
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)        
KEY_PAIR_NAME = 'my-ssh-key-pair'                                   # give the keypair name
AMI_ID = 'ami-0cc00ed857256d2b4'                                    # give AMI Id
INSTANCE_TYPE = 't2.micro'                                          # give instance type

instances = EC2_RESOURCE.create_instances(
    MinCount = 1,
    MaxCount = 1,
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_PAIR_NAME,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'my-ec2-instance'
                },
            ]
        },
    ]
)

for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
    
    instance.wait_until_running()
    print(f'EC2 instance "{instance.id}" has been started')

    