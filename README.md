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
[https://github.com/user-attachments/assets/bd5df58b-59a5-4e1a-b780-147eaf2ce5cd](https://github.com/user-attachments/assets/bd5df58b-59a5-4e1a-b780-147eaf2ce5cd.mp4)

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

