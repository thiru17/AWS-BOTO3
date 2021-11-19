import boto3

AWS_REGION = input("Enter the Region: ")
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = input("Enter the instance id: ")

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

instance.start()

print(f'Starting EC2 instance: {instance.id}')
    
instance.wait_until_running()

print(f'EC2 instance "{instance.id}" has been started')
        
    