import json
from datetime import datetime
import boto3
from urllib.parse import urlparse
from collections import OrderedDict


class S3IncrementalProcessor:
    """
    A class for incrementally processing files from an S3 bucket.
    It keeps track of processed files using a checkpoint mechanism.
    """

    def __init__(self, path, checkpoint_path):
        """
        Initialize the IncrementalFileProcessor.

        :param path: S3 path to the directory containing files to process
        :param checkpoint_path: S3 path to store/retrieve the checkpoint file
        """
        self.path = path
        self.checkpoint_path = checkpoint_path
        self.client = boto3.client('s3')
        self.checkpoint = self._load_checkpoint()
        self.files_to_process = OrderedDict()

    def _load_checkpoint(self):
        """
        Load the checkpoint from S3. If no checkpoint exists, return None.
        This allows the processor to resume from where it left off in the previous run.
        """
        try:
            bucket, key = self._parse_s3_path(self.checkpoint_path)
            response = self.client.get_object(Bucket=bucket, Key=key)
            return json.load(response['Body'])
        except self.client.exceptions.NoSuchKey:
            # If no checkpoint file exists, return None
            return None

    def reset_checkpoint(self):
        """
        Delete the checkpoint file from S3.
        This allows the processor to start from the beginning in the next run.
        """
        bucket, key = self._parse_s3_path(self.checkpoint_path)
        try:
            self.client.delete_object(Bucket=bucket, Key=key)
            print(f"Checkpoint file deleted: s3://{bucket}/{key}")
            self.checkpoint = None
        except Exception as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                print("Checkpoint file does not exist. Nothing to delete.")
            else:
                print(f"Error deleting checkpoint file: {e}")

    def _parse_s3_path(self, s3_path):
        """
        Parse an S3 path into bucket and key components.

        :param s3_path: Full S3 path (e.g., 's3://bucket-name/path/to/file')
        :return: Tuple of (bucket_name, key)
        """
        parsed = urlparse(s3_path)
        return parsed.netloc, parsed.path.lstrip('/')

    def get_new_files(self, batch_size=5, storage_class='STANDARD'):
        """
        Retrieve new files from S3 that haven't been processed yet, in batches.

        :param batch_size: Number of files to process in each batch.
        :param storage_class: Filter files by this storage class. Default is 'STANDARD'.
        :return: List of S3 URIs for new files to process
        """
        bucket, prefix = self._parse_s3_path(self.path)
        paginator = self.client.get_paginator('list_objects_v2')
        all_files = []

        # Step 1: Fetch all files from S3 bucket
        for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
            for obj in page.get('Contents', []):
                if obj['StorageClass'] == storage_class:
                    all_files.append({
                        'Key': obj['Key'],
                        'LastModified': obj['LastModified'].timestamp(),
                        'Size': obj['Size']
                    })

        # Step 2: Sort files by LastModified timestamp and then by Key
        # This ensures a consistent order even for files with the same timestamp
        all_files.sort(key=lambda x: (x['LastModified'], x['Key']))

        # Step 3: Filter out already processed files using the checkpoint
        if self.checkpoint is not None:
            last_processed_time = self.checkpoint['LastModified']
            last_processed_key = self.checkpoint['Key']

            # Keep only files that are:
            # 1. Newer than the last processed file, OR
            # 2. Have the same timestamp but come after the last processed file alphabetically
            all_files = [f for f in all_files if f['LastModified'] > last_processed_time or
                         (f['LastModified'] == last_processed_time and f['Key'] > last_processed_key)]

        # Step 4: Select the batch of files to process
        # This limits the number of files to process in this run
        batch_files = all_files[:batch_size]

        # Step 5: Update the files_to_process OrderedDict
        # This keeps track of the files we're about to process
        self.files_to_process = OrderedDict(
            (f['Key'], {'LastModified': f['LastModified'], 'Size': f['Size']})
            for f in batch_files
        )

        # Step 6: Return the list of S3 URIs for the files to be processed
        return [f"s3://{bucket}/{file['Key']}" for file in batch_files]

    def commit_checkpoint(self):
        """
        Update the checkpoint in S3 with information about the last processed file.
        This allows the next run to start from where this run left off.
        """
        if not self.files_to_process:
            print("No new files were processed. Checkpoint not updated.")
            return

        # Get the last processed file's information
        last_processed_key = next(reversed(self.files_to_process))
        last_processed_file = self.files_to_process[last_processed_key]
        current_time = datetime.now().timestamp()

        # Prepare checkpoint data
        checkpoint_data = json.dumps({
            'Key': last_processed_key,
            'LastModified': last_processed_file['LastModified'],
            'last_ingestion_run': current_time
        })

        # Save checkpoint to S3
        bucket, key = self._parse_s3_path(self.checkpoint_path)
        self.client.put_object(Bucket=bucket, Key=key, Body=checkpoint_data)

        # Log checkpoint update information
        print(f"Checkpoint updated. Last processed file: {last_processed_key}")
        print(f"Last modified: {datetime.fromtimestamp(last_processed_file['LastModified'])}")
        print(f"Ingestion run: {datetime.fromtimestamp(current_time)}")
