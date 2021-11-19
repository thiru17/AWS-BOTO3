import boto3

region = input("Enter the Region Name: ")
image_id = input("Enter an AMI ID: ")
key_name = input("Enter the key name to use: ")
instance_type = input("Enter the instance type: ")
max_count = input("Enter how many EC2 Servers: ")
name_tag = input("Enter the name tag: ")
device_name = input("Enter the device name: ")
disk_size = input("Enter the disk size: ")
security_group_id = input("Enter the security group id: ")
subnet_id = input("Enter the Subnet Id: " )

EC2_RESOURCE = boto3.resource('ec2', region_name=region)
instances = EC2_RESOURCE.create_instances(
    MinCount = 1,
    MaxCount = int(max_count),
    ImageId=image_id ,
    InstanceType=instance_type,
    KeyName=key_name,
    SubnetId=subnet_id,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': name_tag
                },
            ]
        },
    ],
    BlockDeviceMappings = [
           {
            'DeviceName': device_name,
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': int(disk_size),
                'VolumeType': 'gp2'
                 }
            },
        ],
    SecurityGroupIds= [security_group_id]
)

for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
