import io
import boto3


S3_BUCKET_NAME =input("Enter the Bucket Name")

s3_resource = boto3.resource("s3")

s3_bucket = s3_resource.Bucket(S3_BUCKET_NAME)

print('Listing Amazon S3 Bucket objects/files:')

for obj in s3_bucket.objects.all():
    print(f'-- {obj.key}')
