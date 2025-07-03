import streamlit as st
import pandas as pd
from log_parser import parse_log_lines

def plot_visualizations(df):
    st.subheader("Визуализации")

    if 'hour' in df.columns:
        st.write("Запросы по часам")
        hour_counts = df['hour'].value_counts().sort_index()
        st.bar_chart(hour_counts)

    if 'status' in df.columns:
        st.write("Распределение HTTP-статусов")
        status_counts = df['status'].value_counts()
        st.bar_chart(status_counts)

    if 'ip' in df.columns:
        st.write("Топ 10 IP-адресов по количеству запросов")
        top_ips = df['ip'].value_counts().head(10)
        st.bar_chart(top_ips)

    if 'url' in df.columns:
        st.write("Топ 10 запрашиваемых URL")
        top_urls = df['url'].value_counts().head(10)
        st.bar_chart(top_urls)

def main():
    st.title("Визуализатор логов (txt, csv, json)")

    uploaded_file = st.file_uploader("Выберите лог файл", type=["txt", "log", "csv", "json"])
    if uploaded_file is not None:
        try:
            file_type = uploaded_file.name.split('.')[-1].lower()
            if file_type in ['csv']:
                df = pd.read_csv(uploaded_file)
            elif file_type in ['json']:
                df = pd.read_json(uploaded_file)
            else:
                # Для txt/log - читаем строки и парсим через наш лог-парсер
                content = uploaded_file.read().decode('utf-8').splitlines()
                df = parse_log_lines(content)

            st.subheader("Превью данных")
            st.dataframe(df.head())

            plot_visualizations(df)

        except Exception as e:
            st.error(f"Ошибка при обработке файла: {e}")

if __name__ == "__main__":
    main()
