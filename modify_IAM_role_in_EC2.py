import boto3

region = input("Enter the Region: ")
INSTANCE_ID= input("Enter the Instance Id: ")

arn= input("Enter the Instance Profile Arn: ")
name= input("Enter the Name: ")


client=boto3.client('ec2',region_name=region)

response = client.associate_iam_instance_profile(
    IamInstanceProfile={
        'Arn': arn,
        'Name': name
    },
    InstanceId=INSTANCE_ID
)