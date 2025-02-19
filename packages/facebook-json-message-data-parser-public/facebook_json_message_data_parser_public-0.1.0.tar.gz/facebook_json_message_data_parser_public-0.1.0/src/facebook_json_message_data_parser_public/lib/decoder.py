import io
import json
from datetime import datetime

class FacebookDecoder(io.FileIO):
    """Handles decoding of Facebook's Unicode-escaped JSON messages"""
    
    def read(self, size: int = -1) -> bytes:
        data: bytes = super().readall()
        new_data: bytearray = bytearray()
        i: int = 0
        
        while i < len(data):
            if data.startswith(b'\\u00', i):
                u: int = 0
                new_char = bytearray()
                while data.startswith(b'\\u00', i + u):
                    hex_val = int(data[i+u+4:i+u+6], 16)
                    new_char.append(hex_val)
                    u += 6

                new_chars = new_char.decode('utf-8').encode('utf-8')
                new_data += new_chars
                i += u
            else:
                new_data.append(data[i])
                i += 1

        return bytes(new_data)

def decode_facebook_json(input_path: str) -> dict:
    """Decode a Facebook JSON file and return the parsed data"""
    with FacebookDecoder(input_path, 'rb') as f:
        return json.load(f)

def process_messages(data: dict) -> dict:
    """Process message data to convert timestamps and sort messages"""
    for message in data.get('messages', []):
        if 'timestamp_ms' in message:
            timestamp_ms = message['timestamp_ms']
            message['timestamp'] = datetime.fromtimestamp(
                timestamp_ms/1000).strftime('%H:%M %d/%m/%Y')

    # Sort messages by timestamp
    data['messages'] = sorted(
        data['messages'],
        key=lambda x: datetime.strptime(x['timestamp'], '%H:%M %d/%m/%Y')
    )
    
    return data
