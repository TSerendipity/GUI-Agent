import re

def count_tokens(text):
    # tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
    return len(text)

# 精简后的文本
text = """
Tool name: screen_action

Tool function:
Perform screen operations on mobile devices, including tap, back, type text, swipe, long press, and drag.

Parameters:
- device (str): Target device ID. Default is "emulator".
- action (str): Type of screen operation. Options:
    - "tap": Tap coordinates (x, y).
    - "back": Back key operation. No parameters.
    - "text": Input text. Requires parameter: input_str.
    - "long_press": Long press coordinates (x, y). Duration: 1000 ms (default).
    - "swipe": Swipe in four directions ("up", "down", "left", "right"). Requires parameters: x, y, direction, dist ("medium" default), quick (False default).
    - "swipe_precise": Precise swipe from start to end. Requires parameters: start, end, duration (400 ms default).

Returns:
JSON string with fields:
- "status": "success" or "error".
- "action": Operation type.
- "device": Device ID.
- Additional fields based on operation type (e.g., coordinates, input text, swipe points).
"""

# 计算 token 数量
token_count = count_tokens(text)
print(f"Number of tokens: {token_count}")