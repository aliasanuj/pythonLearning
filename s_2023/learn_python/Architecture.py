import os
import json
import csv
import logging
import pydoop.hdfs as hdfs
from ftplib import FTP
import pyarrow.parquet as pq
# Load configurations from environment variables or a configuration file
# Configuration for Hadoop and MFT server
hadoop_host = "your_hadoop_server_hostname"
hadoop_port = 8020  # HDFS port
hadoop_user = "your_hadoop_username"
hadoop_path = "/your/hadoop/data/directory"
mft_server = "your_mft_server"
mft_user = "your_mft_username"
mft_password = "your_mft_password"
# Specify the year and month you want to process
target_year = 2023
target_month = 9  # September
# Connect to Hadoop HDFS
hdfs_handle = hdfs.hdfs(host=hadoop_host, port=hadoop_port, user=hadoop_user)
# Configure logging
logging.basicConfig(filename='data_transfer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
# Function to read and send files of various formats for a specific year and month
def read_and_send_monthly_data(year, month):
    try:
        # List files in the Hadoop directory
        files = hdfs_handle.ls(hadoop_path)
        for file in files:
            # Check if the file matches the year and month
            filename = os.path.basename(file)
            if f"{year}-{month:02}" in filename:
                # Determine the format based on the file extension
                _, file_extension = os.path.splitext(filename)
                format = file_extension[1:]  # Remove the leading dot
                # Read and send the file
                read_and_send_file(filename, format)
        logging.info(f"Successfully transferred files for {year}-{month:02}.")
    except Exception as e:
        error_message = f"Error processing files for {year}-{month:02}: {str(e)}"
        logging.error(error_message)
        print(error_message)
# Function to read and send files of various formats
def read_and_send_file(filename, format):
    file_data = None
    with hdfs_handle.open(os.path.join(hadoop_path, filename), "rb") as hdfs_file:
        if format == "json":
            file_data = json.load(hdfs_file)
        elif format == "csv":
            csv_reader = csv.DictReader(hdfs_file)
            file_data = [row for row in csv_reader]
        elif format == "parquet":
            # Read the Parquet file using pyarrow
            table = pq.read_table(hdfs_file)
            file_data = table.to_pandas().to_dict(orient="records")
        else:
            raise ValueError("Unsupported format: " + format)
    if file_data:
        # Prepare the destination filename based on the format
        destination_filename = filename.replace(".parquet", f".{format}")
        # Connect to MFT server via FTP
        ftp = FTP(mft_server)
        ftp.login(mft_user, mft_password)
        # Send the data to the MFT server
        with open(destination_filename, "w" if format == "json" else "wb") as local_file:
            if format == "json":
                json.dump(file_data, local_file)
            elif format == "csv":
                csv_writer = csv.DictWriter(local_file, fieldnames=file_data[0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(file_data)
        ftp.storbinary(f"STOR {destination_filename}", open(destination_filename, "rb"))
        # Clean up local file
        os.remove(destination_filename)
        ftp.quit()
        logging.info(f"Successfully transferred {filename} in {format} format.")
# Example usage: Read and send files for the specified year and month
read_and_send_monthly_data(target_year, target_month)
=========================================================


import os
import pandas as pd
# Specify the directory where your files are located
files_directory = '/path/to/your/files/'
# List of file extensions to process
file_extensions = ['.csv', '.parquet', '.json']
# Function to add a new column to each file
def add_new_column(file_path, new_column_name, new_column_data):
    file_extension = os.path.splitext(file_path)[-1].lower()
    if file_extension == '.csv':
        df = pd.read_csv(file_path)
    elif file_extension == '.parquet':
        df = pd.read_parquet(file_path)
    elif file_extension == '.json':
        df = pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")
    # Add a new column with the specified name and data
    df[new_column_name] = new_column_data
    # Save the modified DataFrame back to the file
    if file_extension == '.csv':
        df.to_csv(file_path, index=False)
    elif file_extension == '.parquet':
        df.to_parquet(file_path, index=False)
    elif file_extension == '.json':
        df.to_json(file_path, orient='records', lines=True)
# Specify the new column name and data (example)
new_column_name = 'new_column'
new_column_data = ['value1', 'value2', 'value3']
# Process files with specified extensions in the directory
for file_name in os.listdir(files_directory):
    if any(file_name.endswith(ext) for ext in file_extensions):
        file_path = os.path.join(files_directory, file_name)
        add_new_column(file_path, new_column_name, new_column_data)
        print(f"Added a new column to {file_name}")
print("Script completed.")

=============================================
import os
import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError
# AWS credentials and S3 bucket information
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
aws_session_token = 'YOUR_SESSION_TOKEN'  # If using temporary credentials
s3_bucket_name = 'your-s3-bucket-name'
s3_folder = 'your-folder-path-in-s3'
# Specify the directory where your modified files are located
files_directory = '/path/to/your/modified/files/'
# List of file extensions to process
file_extensions = ['.csv', '.parquet', '.json']
# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  aws_session_token=aws_session_token)
# Function to upload a file to Amazon S3
def upload_to_s3(file_path, s3_bucket, s3_key):
    try:
        s3.upload_file(file_path, s3_bucket, s3_key)
        print(f"Uploaded {file_path} to S3 bucket {s3_bucket} with key {s3_key}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except NoCredentialsError:
        print("AWS credentials not available or invalid.")
# Specify the new column name and data (example)
new_column_name = 'new_column'
new_column_data = ['value1', 'value2', 'value3']
# Process files with specified extensions in the directory
for file_name in os.listdir(files_directory):
    if any(file_name.endswith(ext) for ext in file_extensions):
        file_path = os.path.join(files_directory, file_name)
        # Add a new column to the file (example)
        if file_name.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_name.endswith('.parquet'):
            df = pd.read_parquet(file_path)
        elif file_name.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_name}")
        df[new_column_name] = new_column_data
        # Save the modified DataFrame back to the file
        if file_name.endswith('.csv'):
            df.to_csv(file_path, index=False)
        elif file_name.endswith('.parquet'):
            df.to_parquet(file_path, index=False)
        elif file_name.endswith('.json'):
            df.to_json(file_path, orient='records', lines=True)
        # Upload the modified file to Amazon S3
        s3_key = os.path.join(s3_folder, file_name)
        upload_to_s3(file_path, s3_bucket_name, s3_key)
print("Script completed.")

==================================
# Initialize an S3 client
s3 = boto3.client('s3')
# Specify the local file path and S3 bucket and key (destination)
local_file_path = 'path/to/your/local/file.csv'
s3_bucket_name = 'your-s3-bucket-name'
s3_key = 'desired-folder-path-in-s3/your-file.csv'
# Upload the file to S3
s3.upload_file(local_file_path, s3_bucket_name, s3_key)
==============================================
import boto3
import os
# AWS credentials and S3 bucket information
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
aws_session_token = 'YOUR_SESSION_TOKEN'  # If using temporary credentials
s3_bucket_name = 'your-s3-bucket-name'
s3_folder = 'desired-folder-path-in-s3/'
# Directory where your files are located on the second SIT server
source_directory = '/path/to/your/files/'
# Initialize the S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  aws_session_token=aws_session_token)
# Function to upload a file to Amazon S3
def upload_to_s3(local_file_path, s3_bucket, s3_key):
    try:
        s3.upload_file(local_file_path, s3_bucket, s3_key)
        print(f"Uploaded {local_file_path} to S3 bucket {s3_bucket} with key {s3_key}")
    except FileNotFoundError:
        print(f"The file {local_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while uploading {local_file_path} to S3: {str(e)}")
# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    if os.path.isfile(os.path.join(source_directory, filename)):
        # Specify the full path of the local file
        local_file_path = os.path.join(source_directory, filename)
        # Determine the S3 key (destination) by combining the folder path and filename
        s3_key = os.path.join(s3_folder, filename)
        # Upload the file to Amazon S3
        upload_to_s3(local_file_path, s3_bucket_name, s3_key)
print("File upload completed.")
======================
import json
def lambda_handler(event, context):
    # Your API logic here
    response = {
        "statusCode": 200,
        "body": json.dumps("Hello, World!")
    }
    return response
=======================================
import json
import boto3
# Initialize AWS Athena client
athena = boto3.client('athena', region_name='us-east-1')
# Athena query execution function
def execute_athena_query(query_string):
    try:
        response = athena.start_query_execution(
            QueryString=query_string,
            QueryExecutionContext={'Database': 'your-athena-database'},
            ResultConfiguration={'OutputLocation': 's3://your-athena-query-results/'}
        )
        query_execution_id = response['QueryExecutionId']
        return query_execution_id
    except Exception as e:
        return str(e)
# Lambda handler function
def lambda_handler(event, context):
    http_method = event['httpMethod']
    query_string_parameters = event.get('queryStringParameters', {})
    if http_method == 'GET':
        # Extract query parameter (e.g., SELECT * FROM your_table)
        query = query_string_parameters.get('query', '')
        if query:
            # Execute Athena query
            query_execution_id = execute_athena_query(query)
            return {
                'statusCode': 200,
                'body': json.dumps({'message': f'Query execution started with ID: {query_execution_id}'})
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing query parameter'})
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Unsupported HTTP method'})
        }

==========================================================




