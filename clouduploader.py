
# Import the necessary models for this code
import boto3
import argparse
import os

# Set S3 destination path for S3 
def upload_to_bucket(file_path, s3_bucket) :
    s3 = boto3.client('s3')
    s3_destination = f"s3://{s3_bucket}/"

#Use boto3 to upload file to S3
    try:
        s3.upload_file(file_path, s3_bucket, os.path.join(os.path.basename(file_path)))
        print("File uploaded successfully to Cloud")
    except Exception as error:
        print(f"Error uploading file to Cloud: {error}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload files to AWS S3 bucket")
    parser.add_argument("file_path", help="Path to the file to upload")
    parser.add_argument("s3_bucket", help="Name of the AWS S3 bucket")
    args = parser.parse_args()

    upload_to_bucket(args.file_path, args.s3_bucket)
