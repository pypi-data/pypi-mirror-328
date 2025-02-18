import re
import pathlib
from ..config.logger import Logger

logger = Logger(__name__)


class AppUtil:
    @staticmethod
    def serialize_dict(a) -> dict:
        return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}

    @staticmethod
    def serialize_list(entity) -> list:
        return [AppUtil.serialize_dict(a) for a in entity]
    
    @staticmethod
    def load_file(path: pathlib.Path):
        with open(path, "r") as f:
            return f.read()
        
    @staticmethod
    def parse_messages(messages):
        role_prefixes = {
            "user": "user",
            "assistant": "assistant"
        }

        response_parts = []
        for msg in messages:
            role = msg["role"]
            if role in role_prefixes:
                response_parts.append(f"{role_prefixes[role]}: {msg['content']}")

        return "\n".join(response_parts)

        
    @staticmethod
    def remove_code_blocks(content: str) -> str:
        """
        Removes enclosing code block markers ```[language] and ``` from a given string.

        Remarks:
        - The function uses a regex pattern to match code blocks that may start with ``` followed by an optional language tag (letters or numbers) and end with ```.
        - If a code block is detected, it returns only the inner content, stripping out the markers.
        - If no code block markers are found, the original content is returned as-is.
        """
        pattern = r"^```[a-zA-Z0-9]*\n([\s\S]*?)\n```$"
        match = re.match(pattern, content.strip())
        return match.group(1).strip() if match else content.strip()