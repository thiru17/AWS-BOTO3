import boto3
 
#list regions
client = boto3.client('ec2')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
 
print("Listing EC2 instances for each region....\n")
 
for i in regions:
    print()
    print(i)
    print('---------')
    Region = i
    client = boto3.client('ec2', region_name=i)
    response = client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["ImageId"])
