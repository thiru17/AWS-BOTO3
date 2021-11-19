import boto3

AWS_REGION = input("Enter the Region: ")
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = input("Enter the Instance Id: ")

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

instance.stop()

print(f'Stopping EC2 instance: {instance.id}')
    
instance.wait_until_stopped()

print(f'EC2 instance "{instance.id}" has been stopped')