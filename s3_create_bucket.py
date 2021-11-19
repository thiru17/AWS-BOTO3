import boto3


resource = boto3.resource("s3")

bucket_name = str(input('Enter the Bucket Name: '))

bucket = resource.create_bucket(

    Bucket=bucket_name,
    ACL='private'
)

def enable_version(bucket_name):
    versioning = resource.BucketVersioning(bucket_name)
    versioning.enable()

enable_version(bucket_name)

print("Amazon S3 bucket has been created")
