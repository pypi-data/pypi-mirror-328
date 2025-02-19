import os
from pathlib import Path
from typing import List
from .lib.decoder import decode_facebook_json, process_messages
from .lib.utils import find_json_files, write_json_file

class FacebookMessageParser:
    def __init__(self, input_dir: str, output_dir: str = "decoded_messages"):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def process_files(self) -> List[str]:
        """Process all JSON files in the input directory and return list of output files"""
        json_files = find_json_files(self.input_dir)
        processed_files = []

        for json_file in json_files:
            try:
                # Decode and process the file
                data = decode_facebook_json(str(json_file))
                processed_data = process_messages(data)

                # Generate output filename based on participants
                participants = [p['name'] for p in processed_data.get('participants', [])]
                output_filename = '_'.join(participants) + '.json' if participants else json_file.name

                # Write processed data
                output_file = write_json_file(processed_data, self.output_dir, output_filename)
                processed_files.append(output_file)
                
                print(f"Processed: {json_file.name} -> {output_filename}")
                
            except Exception as e:
                print(f"Error processing {json_file}: {str(e)}")

        return processed_files

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Process Facebook JSON message data')
    parser.add_argument('input_dir', help='Directory containing Facebook JSON files')
    parser.add_argument('--output-dir', default='decoded_messages',
                        help='Directory for decoded output files')
    
    args = parser.parse_args()
    
    processor = FacebookMessageParser(args.input_dir, args.output_dir)
    processed_files = processor.process_files()
    
    print(f"\nProcessed {len(processed_files)} files")
    print(f"Output files saved to: {args.output_dir}")

if __name__ == '__main__':
    main()
