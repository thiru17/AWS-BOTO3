import boto3

region = input("Enter the Region: ")
client = boto3.client('ec2',region_name= region)

# Insert your Instance ID here
my_instance = input("Enter the Instance Id: ")

# Stop the instance
client.stop_instances(InstanceIds=[my_instance])
waiter=client.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[my_instance])

# Change the instance type

instancetype = input("Enter the Instance Type: ")
client.modify_instance_attribute(InstanceId=my_instance, Attribute='instanceType', Value=instancetype)

# Start the instance
client.start_instances(InstanceIds=[my_instance])

