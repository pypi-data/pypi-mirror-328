from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Any

@dataclass
class Participant:
    name: str

@dataclass
class Message:
    sender_name: str
    timestamp_ms: int
    content: Optional[str]
    timestamp: str
    is_geoblocked_for_viewer: bool = False
    # Make it flexible to accept any additional fields without storing them
    def __init__(self, sender_name: str, timestamp_ms: int, content: Optional[str] = None, 
                 timestamp: Optional[str] = None, is_geoblocked_for_viewer: bool = False, **kwargs):
        self.sender_name = sender_name
        self.timestamp_ms = timestamp_ms
        self.content = content
        # Generate timestamp if not provided
        self.timestamp = timestamp or datetime.fromtimestamp(
            timestamp_ms/1000).strftime('%H:%M %d/%m/%Y')
        self.is_geoblocked_for_viewer = is_geoblocked_for_viewer

@dataclass
class Conversation:
    participants: List[Participant]
    messages: List[Message]
    title: str
    is_still_participant: bool
    thread_path: str
    magic_words: None = None

def message_to_mongo_doc(message: Message) -> dict:
    """Convert a Message object to MongoDB document format"""
    return {
        "sender_name": message.sender_name,
        "timestamp_ms": message.timestamp_ms,
        "content": message.content,
        "timestamp": message.timestamp,
        "is_geoblocked_for_viewer": message.is_geoblocked_for_viewer
    }
