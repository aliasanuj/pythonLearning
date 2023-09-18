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
