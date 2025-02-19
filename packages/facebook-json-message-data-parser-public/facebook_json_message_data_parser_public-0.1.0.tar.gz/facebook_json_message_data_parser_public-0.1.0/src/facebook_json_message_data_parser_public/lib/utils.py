import os
import json
from pathlib import Path
from typing import List, Set

def find_json_files(input_dir: str) -> List[Path]:
    """Recursively find all JSON files in the input directory"""
    input_path = Path(input_dir)
    return list(input_path.rglob("*.json"))

def get_safe_filename(base_name: str, existing_files: Set[str]) -> str:
    """Generate a unique filename that doesn't conflict with existing files"""
    if base_name not in existing_files:
        return base_name
    
    counter = 1
    name = Path(base_name)
    while True:
        new_name = f"{name.stem}_{counter}{name.suffix}"
        if new_name not in existing_files:
            return new_name
        counter += 1

def write_json_file(data: dict, output_dir: str, filename: str) -> str:
    """Write JSON data to file, handling filename conflicts"""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    existing_files = set(f.name for f in output_path.iterdir())
    safe_filename = get_safe_filename(filename, existing_files)
    
    output_file = output_path / safe_filename
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    return str(output_file)
