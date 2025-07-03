import matplotlib.pyplot as plt
import streamlit as st

def plot_requests_by_hour(df):
    hour_counts = df['hour'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(hour_counts.index, hour_counts.values)
    ax.set_xlabel('Час суток')
    ax.set_ylabel('Количество запросов')
    ax.set_title('Запросы по часам')
    st.pyplot(fig)

def plot_top_ips(df, top_n=10):
    top_ips = df['ip'].value_counts().head(top_n)
    st.subheader(f"Топ {top_n} IP-адресов")
    st.bar_chart(top_ips)

def plot_top_urls(df, top_n=10):
    top_urls = df['url'].value_counts().head(top_n)
    st.subheader(f"Топ {top_n} URL")
    st.bar_chart(top_urls)

def plot_status_codes_pie(df):
    status_counts = df['status'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.subheader("Коды ответов")
    st.pyplot(fig)
