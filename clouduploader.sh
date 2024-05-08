#!/bin/bash

# Parse command-line arguments
FILE_PATH=$1
S3_BUCKET="cyberkenuploader"
S3_DIRECTORY=$2 #Optional
STORAGE_CLASS=$3 #Optional

# Check if all required arguments are provided
if [ $# -lt 2 ]; then
  echo "Usage: $0 <file_path> <s3_bucket> [s3_directory] [storage_class]"
  exit 1
fi

# Check if file exists
if [ ! -f "$FILE_PATH" ]; then
  echo "File not found: $FILE_PATH"
  exit 1
fi

# Upload file to S3
if [ -n "$S3_DIRECTORY" ]; then
  S3_DESTINATION="s3://$S3_BUCKET/$S3_DIRECTORY/"
else
  S3_DESTINATION="s3://$S3_BUCKET/"
fi

if [ -n "$STORAGE_CLASS" ]; then
  aws s3 cp "$FILE_PATH" "$S3_DESTINATION" --storage-class "$STORAGE_CLASS"
else
  aws s3 cp "$FILE_PATH" "$S3_DESTINATION"
fi

# Check upload status
if [ $? -eq 0 ]; then
  echo "File uploaded successfully to S3."
else
  echo "Error uploading file to S3."
fi
