import boto3

bucket_name=input("Enter the Bucket Name: ")
filename = input("Enter the filename: ")

s3_resource = boto3.resource("s3")

s3_object = s3_resource.Object(bucket_name, filename)

s3_object.delete()

print('S3 object deleted')
