# S3 Incremental File Processor

A Python package that allows users to fetch new files from an S3 bucket in an incremental fashion. It supports checkpointing, ensuring that only new files are accessed in the next run. The package also provides a method to reset the checkpoint, enabling the reprocessing of all data if needed.

## Features

- **Incremental File Processing:** Fetch only new or modified files from an S3 bucket.
- **Checkpointing:** Keeps track of processed files to prevent duplicate processing.
- **Batch Processing:** Process files in configurable batch sizes.
- **Storage Class Filtering:** Fetch files based on their storage class (e.g., `STANDARD`).
- **Reset Checkpoint:** Delete the checkpoint to reprocess all files.
- **Handles Edge Cases:** Ensures correct file ordering when timestamps are identical.

## Installation

```bash
pip install S3IncrementalProcessor
```

# Usage
```agsl
from S3IncrementalProcessor import S3IncrementalProcessor

# Initialize the processor with S3 paths
processor = S3IncrementalProcessor(
    "s3://your-bucket/path/to/files/",
    "s3://your-bucket/checkpoints/checkpoint.json"
)

# Fetch new files in batches
new_files = processor.get_new_files(batch_size=5)

if new_files:
    print(f"Processing {len(new_files)} files:")
    for file in new_files:
        print(f"- {file}")
        # Add your processing logic here

    # Commit the checkpoint after processing
    processor.commit_checkpoint()
else:
    print("No new or modified files found.")

# To reset checkpoint and reprocess all files
# processor.reset_checkpoint()

```

## Test Cases

This package has been tested with the following scenarios:

### 1. 10 Files, Batch Size 5
- **Expected:** Two runs to process all files. A third run should return no new files.

### 2. 10 Files, Batch Size 100
- **Expected:** One run should process all 10 files.

### 3. Files with Identical Timestamps
- **Ensures:** Files uploaded simultaneously using threading are correctly ordered, and only new files are processed.



# Contributing

Contributions are welcome! Please open an issue or submit a pull request.
License

