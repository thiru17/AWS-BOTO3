import boto3

AWS_REGION = "us-east-1"

resource = boto3.resource("s3", region_name=AWS_REGION)

iterator = resource.buckets.all()

print("List all Amazon S3 Buckets:")

for bucket in iterator:
    print(f"-- {bucket.name}")

