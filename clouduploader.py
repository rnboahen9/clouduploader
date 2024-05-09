
# Import the necessary models for this code
import boto3
import argparse
import os

# Set S3 destination path for S3 
def upload_to_bucket(file_path, cyberkenuploader, s3_directory = None, storage_class = None) :
    s3 = boto3.client('s3')
    s3_bucket = f"s3://cyberkenuploader/"
    if s3_directory:
       s3_bucket += f"s3_directory/"

#Use boto3 to upload file to S3
    try:
        if storage_class:
            extra_args = {'StorageClass' : storage_class}
            s3.upload_file(file_path, cyberkenuploader, os.path.join(s3_directory, os.path.basename(file_path)), ExtraArgs=extra_args)
        else:
            s3.upload_file(file_path, cyberkenuploader, os.path.join(s3_directory, os.path.basename(file_path)))
        print("File uploaded successfully to Cloud")
    except Exception as error:
        print(f"Error uploading file to Cloud: error")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload files to AWS S3 bucket")
    parser.add_argument("file_path", help="Path to the file to upload")
    parser.add_argument("Cyberkenuploader", help="Name of the AWS S3 bucket")
    parser.add_argument("--s3-directory", help="Optional directory within the S3 bucket")
    parser.add_argument("--storage-class", help="Optional storage class for the uploaded file")
    args = parser.parse_args()

    upload_to_bucket(args.file_path, args.bucket_name, args.s3_directory, args.storage_class)
