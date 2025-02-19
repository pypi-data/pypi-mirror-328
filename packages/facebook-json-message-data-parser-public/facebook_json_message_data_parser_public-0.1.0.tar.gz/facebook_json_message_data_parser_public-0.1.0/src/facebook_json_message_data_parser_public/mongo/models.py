from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

@dataclass
class Participant:
    name: str

@dataclass
class Message:
    sender_name: str
    timestamp_ms: int
    content: Optional[str]
    timestamp: str  # Generated field
    is_geoblocked_for_viewer: bool = False

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
