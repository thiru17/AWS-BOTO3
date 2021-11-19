import boto3

region = input("Enter the Region: ")
owner = input("Enter the AMI Owner: ")
ami_name = input("Enter the AMI Name: ")

client = boto3.client('ec2', region_name=region)

response = client.describe_images(

         Owners=[owner],
          Filters=[
                {
                    'Name': 'name',
                    'Values': [ami_name]
                },
                {
                    'Name': 'virtualization-type', 'Values': ['hvm']
                },
                {
                    'Name': 'state', 'Values': ['available']
                },
                {
                    'Name': 'platform', 'Values': ['windows']
                },

                {
                    'Name': 'root-device-type', 'Values': ['ebs']
                },
                {
                    'Name': 'architecture', 'Values': ['x86_64']
                }
            ]
        )

for ami in response['Images']:
  print (ami['ImageId'])

