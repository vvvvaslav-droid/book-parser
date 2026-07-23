# Парсер книг (books.toscrape.com → CSV)

## 📌 Что делает
Скрипт загружает страницу `books.toscrape.com`, парсит все карточки книг (название, цену, ссылку) и сохраняет их в `books.csv`.

## 🛠️ Как запустить
1. Установите Python 3.12+
2. Установите библиотеки:  
   `pip install requests beautifulsoup4 lxml`
3. Запустите:  
   `python parser.py`
4. Результат появится в файле `books.csv`.

## 📸 Пример работы
Пример: https://github.com/vvvvaslav-droid/book-parser/blob/main/image.png

## 📂 Структура
- `parser.py` — основной код
- `books.csv` — результат работы (создаётся автоматически)

## 📦 Зависимости
- `requests`
- `beautifulsoup4`
- `lxml`

## 👨‍💻 Автор
Вячеслав
