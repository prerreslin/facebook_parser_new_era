# Facebook Group parser

Скрипт на Python с использованием Selenium для автоматического парсинга постов в Facebook-группах. Ищет ключевые слова в тексте постов и сохраняет подходящие в `results.txt`.

## 📌 Возможности

- Авторизация через cookies (`cookies.json`)
- Обход списка групп из `groups.txt`
- Автоматическое раскрытие скрытого текста постов (кнопки "Ещё", "More", "Ще")
- Поиск ключевых слов из `keywords.txt`
- Сохранение найденных постов с ссылкой и текстом

## 🛠 Установка

1. Установите Python 3.7 или выше  
2. Установите зависимости:

```bash
pip install selenium
```

3. Установите ChromeDriver под свою версию Chrome:  
   https://sites.google.com/chromium.org/driver/

## 📁 Структура проекта

```
facebook_scraper/
├── get_posts.py          # основной скрипт
├── cookies.json        # cookies для входа
├── groups.txt          # список групп Facebook
├── keywords.txt        # список ключевых слов
└── results.txt         # файл для результатов
```

## 📂 Формат входных файлов

### cookies.json

Файл cookies, экспортированный из вашего браузера.  
Нужен для входа без логина/пароля.

Расширение: https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm
Демонстрация:
https://private-user-images.githubusercontent.com/156519116/432258245-ee629258-514d-49aa-9090-41e94d0c26c2.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQyODMxMjgsIm5iZiI6MTc0NDI4MjgyOCwicGF0aCI6Ii8xNTY1MTkxMTYvNDMyMjU4MjQ1LWVlNjI5MjU4LTUxNGQtNDlhYS05MDkwLTQxZTk0ZDBjMjZjMi5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQxMFQxMTAwMjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00ZmM3OWU3MTFjMjJlOTI2NWFhOGUwN2U2MDMzZGMwMWM1Mjk0ZGRjY2IzYWI0ZTcyMDcyOTJmOTM2MjM4YTA4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.E-YJOCVtjfpVWB7sJ9Qr2xbXk9Df6Y5kVrZ_asr47pE.mp4

### groups.txt

Список ссылок на Facebook-группы, по одной на строку:

```
https://www.facebook.com/groups/yourgroup1
https://www.facebook.com/groups/yourgroup2
```

### keywords.txt

Список ключевых слов, по одному на строку:

```
работа
удалёнка
вакансия
```

## 🚀 Запуск

```bash
python get_posts.py
```

## ✅ Результат

Все посты, содержащие ключевые слова, сохраняются в `results.txt`:

```
https://www.facebook.com/groups/yourgroup/posts/1234567890
Текст поста...
--------------------------------------------------
```

## ⚠️ Важно

- Facebook может временно ограничить доступ, если запрашивать слишком часто.
- Используйте только в личных и образовательных целях.
- Скрипт не предназначен для массового сбора данных или спама.

## 📄 Лицензия

Проект распространяется под лицензией **MIT**.

