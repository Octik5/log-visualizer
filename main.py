import re
import pandas as pd
from datetime import datetime

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\w+) (?P<url>[^ ]+) HTTP/[\d.]+" (?P<status>\d{3}) (?P<size>\d+)'
)

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        data = match.groupdict()
        data['datetime'] = datetime.strptime(data['datetime'], "%Y-%m-%d %H:%M:%S %z")
        data['status'] = int(data['status'])
        data['size'] = int(data['size'])
        return data
    return None

def parse_log_file(filepath):
    entries = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                entries.append(parsed)
    return pd.DataFrame(entries)

if __name__ == "__main__":
    df = parse_log_file("access_v2.log")
    print(df.head())

    # Пример статистики
    print("Запросов по IP:")
    print(df['ip'].value_counts())

    print("\nКоды ответов:")
    print(df['status'].value_counts())

    print("\nЗапросов по URL:")
    print(df['url'].value_counts().head(10))

    # Временной график — количество запросов по часам
    df['hour'] = df['datetime'].dt.hour
    print("\nЗапросов по часам:")
    print(df.groupby('hour').size())
