import json
from datetime import datetime
from ..models import AlarmCallback
from ..utils.file_handler import append_to_file, read_file_content
import re
from ..config import MARKDOWN_FILE

def save_alarm_data(alarm_data: AlarmCallback) -> str:
    json_data = json.dumps(alarm_data.dict(), indent=2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    markdown_entry = f"""
## Alarm Entry [{timestamp}]

```json
{json_data}
```

---
"""
    
    append_to_file(MARKDOWN_FILE, markdown_entry)
    return f"数据已成功追加到文件 {MARKDOWN_FILE}"

def get_alarm_entries():
    markdown_content = read_file_content(MARKDOWN_FILE)
    entries = markdown_content.split('---\n')
    formatted_entries = []
    
    for entry in entries:
        if entry.strip():
            # 使用正则表达式提取时间和 JSON 内容
            title_match = re.search(r'## Alarm Entry \[(.*?)\]', entry)
            json_match = re.search(r'```json\n(.*?)\n```', entry, re.DOTALL)
            
            if title_match and json_match:
                header = title_match.group(1)
                json_content = json_match.group(1)
                formatted_entries.append({
                    'header': header,
                    'json_content': json_content
                })
    
    return formatted_entries

# 使用 MARKDOWN_FILE 替换硬编码的文件路径

