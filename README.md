# log-visualizer
Визуализатор логов для анализа сетевого трафика и веб-запросов

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Pandas](https://img.shields.io/badge/Pandas-1.5.3-blueviolet)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7.1-orange)

# Визуализатор логов с фильтрацией и графиками

Этот проект предоставляет удобный веб-интерфейс на Streamlit для анализа лог-файлов (txt, csv, json) с возможностью интерактивной фильтрации и построения графиков.

## 🔥 Возможности

- Автоматический парсинг популярных форматов логов (Apache Common Log, кастомные)  
- Фильтрация по IP, времени, HTTP статусам и портам  
- Визуализация: распределение запросов по часам, HTTP статусам, топ IP и URL  
- Поддержка пользовательских регулярных выражений для парсинга  
- Удобный web-интерфейс для быстрого анализа логов  

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/YourUsername/log-visualizer.git
cd log-visualizer
```
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
🚀 Запуск
```bash
streamlit run logs_visualizer.py
```
Откройте в браузере адрес, который выдаст Streamlit (обычно http://localhost:8501)
