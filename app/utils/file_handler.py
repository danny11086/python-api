import os

def append_to_file(filename: str, content: str):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content)

def read_file_content(filename: str) -> str:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    return ""
