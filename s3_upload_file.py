import boto3

S3_BUCKET_NAME = input("Enter the Bucket_Name: ")
file_name = input("Enter the File_Name: ")
s3_filename = input("Enter the S3_File_Name: ")

s3_client = boto3.client("s3")

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")

upload_files(s3_filename , S3_BUCKET_NAME)



