import os
from pathlib import Path
import json
from typing import List
import pymongo
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
import getpass
from tqdm import tqdm

from ..lib.decoder import decode_facebook_json, process_messages
from ..lib.utils import find_json_files
from .models import Message, message_to_mongo_doc

class MongoUploader:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def upload_messages(self, messages: List[dict]):
        """Upload messages to MongoDB"""
        if messages:
            self.collection.insert_many(messages)

def merge_message_files(input_dir: str) -> List[dict]:
    """Merge all message files into a single list of messages"""
    json_files = find_json_files(input_dir)
    all_messages = []

    for json_file in tqdm(json_files, desc="Processing files"):
        try:
            data = decode_facebook_json(str(json_file))
            processed_data = process_messages(data)
            all_messages.extend([
                message_to_mongo_doc(Message(**msg))
                for msg in processed_data.get('messages', [])
            ])
        except Exception as e:
            print(f"Error processing {json_file}: {str(e)}")

    return all_messages

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Upload Facebook messages to MongoDB')
    parser.add_argument('input_dir', help='Directory containing Facebook JSON files')
    args = parser.parse_args()

    # Get MongoDB connection details
    print("\nMongoDB Connection Setup:")
    uri = input("Enter MongoDB URI: ")
    db_name = input("Enter database name: ")
    collection_name = input("Enter collection name: ")

    try:
        # Process and merge files
        print("\nProcessing message files...")
        messages = merge_message_files(args.input_dir)
        
        if not messages:
            print("No messages found to upload!")
            return

        # Upload to MongoDB
        print(f"\nUploading {len(messages)} messages to MongoDB...")
        uploader = MongoUploader(uri, db_name, collection_name)
        uploader.upload_messages(messages)
        
        print(f"\nSuccessfully uploaded {len(messages)} messages to MongoDB")
        print(f"Database: {db_name}")
        print(f"Collection: {collection_name}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
