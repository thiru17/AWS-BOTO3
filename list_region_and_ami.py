import boto3

region = input("Enter the Region Name: ")
ami_name = input("Enter the AMI Name: ")

resource = boto3.client('ec2', region_name=region)

def get_all_ami_id():
        image_id = ''
        response = resource.describe_images(
            Filters=[
                {
                    'Name': 'name',
                    'Values': [ami_name]
                },
                {
                    'Name': 'state', 'Values': ['available']
                },

            ]
        )
        response = response.get('Images')
        for i in response:
            image_id = i.get('ImageId')
        print(image_id)

get_all_ami_id()

