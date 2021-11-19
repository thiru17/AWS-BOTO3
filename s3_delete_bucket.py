import boto3

resource = boto3.resource("s3")

bucket_name = str(input('Enter the Bucket Name: '))

s3_bucket = resource.Bucket(bucket_name)
s3_bucket.delete()

print("Amazon S3 Bucket has been deleted")
