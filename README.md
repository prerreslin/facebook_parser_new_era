# Facebook Group Parser

Скрипт на Python с использованием Selenium для автоматического парсинга постов в Facebook-группах. Ищет ключевые слова в тексте постов и сохраняет подходящие в `results.txt`.

## 📌 Возможности

- Авторизация через cookies (`cookies.json`)
- Обход списка групп из `groups.txt`
- Автоматическое раскрытие скрытого текста постов (кнопки "Ещё", "More", "Ще")
- Поиск ключевых слов из `keywords.txt`
- Сохранение найденных постов с ссылкой и текстом

## 🧰 Для новичков

Если вы впервые работаете с Python, выполните следующие шаги:

1. **Скачайте и установите Visual Studio Code (VS Code)**  
   https://code.visualstudio.com/

2. **Скачайте и установите Python (рекомендуется 3.10+)**  
   https://www.python.org/downloads/

3. **Откройте папку проекта в VS Code**

4. **Откройте терминал VS Code**  
   Меню → Вид → Терминал или `Ctrl + ~`

5. **Создайте виртуальное окружение**  
   В терминале выполните:

   ```bash
   python -m venv .venv
   ```

6. **Активируйте виртуальное окружение**:

   - **Windows:**

     ```bash
     .venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source .venv/bin/activate
     ```

7. **Установите зависимости:**

   ```bash
   pip install selenium
   ```

8. **Установите ChromeDriver под свою версию Chrome:**  
   https://sites.google.com/chromium.org/driver/

## 📁 Структура проекта

```
facebook_scraper/
├── get_posts.py          # основной скрипт
├── cookies.json          # cookies для входа
├── groups.txt            # список групп Facebook
├── keywords.txt          # список ключевых слов
└── results.txt           # файл для результатов
```

## 📂 Формат входных файлов

### cookies.json

Файл cookies, экспортированный из вашего браузера.  
Нужен для входа без логина/пароля.

Расширение: https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm  
Туториал: https://youtu.be/1JeNheUHCis

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

