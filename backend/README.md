Проект Backend на FastAPI

Это проект на базе FastAPI, который включает Docker для простого развертывания. Backend можно запускать как отдельно, так и в составе Docker Compose вместе с базой данных PostgreSQL.
Основные возможности

    FastAPI: Современный, быстрый веб-фреймворк для создания API на Python 3.6+.
    Docker: Легко разворачиваемый с помощью Docker, поддержка как автономного запуска, так и в составе Docker Compose.
    Интеграция с базой данных: Использует PostgreSQL в связке с Tortoise ORM.
    Логирование: Настроено логирование с ротацией файлов с помощью модуля logging.

Переменные окружения

    Убедитесь, что в корневой директории проекта есть файл .env со следующими переменными:
    
        DATABASE_URL=postgres://myuser:mypassword@db:5432/mydatabase
        POSTGRES_USER=myuser
        POSTGRES_PASSWORD=mypassword
        POSTGRES_DB=mydatabase

Запуск с Docker Compose (с PostgreSQL)

    Вы можете запустить backend вместе с базой данных PostgreSQL с помощью Docker Compose.
        docker compose up --build

API Маршруты

    POST /api/users/: Создание или обновление пользователя.
    GET /api/users/{username}/: Получение информации о пользователе по имени пользователя.
