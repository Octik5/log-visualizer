import re
import pandas as pd
from datetime import datetime

LOG_PATTERNS = {
    "apache_common": {
        "regex": re.compile(
            r'(?P<ip>\S+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'
        ),
        "datetime_format": "%d/%b/%Y:%H:%M:%S %z"
    },
    "custom_format": {
        "regex": re.compile(
            r'(?P<ip>\S+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'
        ),
        "datetime_format": "%Y-%m-%d %H:%M:%S %z"
    }
}

def parse_log_lines(lines, user_regex=None, user_datetime_format=None):
    def detect_pattern(lines):
        for name, info in LOG_PATTERNS.items():
            regex = info['regex']
            matched = True
            for line in lines[:10]:
                if not regex.match(line):
                    matched = False
                    break
            if matched:
                return name
        return None

    pattern_name = detect_pattern(lines)
    if pattern_name:
        print(f"Использован шаблон: {pattern_name}")
        regex = LOG_PATTERNS[pattern_name]['regex']
        datetime_format = LOG_PATTERNS[pattern_name]['datetime_format']
    else:
        if user_regex is None or user_datetime_format is None:
            raise ValueError("Не определён шаблон. Задайте регулярное выражение и формат даты.")
        regex = re.compile(user_regex)
        datetime_format = user_datetime_format

    parsed_data = []
    for line in lines:
        match = regex.match(line)
        if not match:
            continue
        data = match.groupdict()
        if 'datetime' in data:
            try:
                data['datetime'] = datetime.strptime(data['datetime'], datetime_format)
            except Exception:
                data['datetime'] = None
        parsed_data.append(data)

    df = pd.DataFrame(parsed_data)
    if 'datetime' in df.columns:
        df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
        df['hour'] = df['datetime'].dt.hour
    return df