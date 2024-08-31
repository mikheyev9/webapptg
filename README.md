Запуск проекта 

1. Настройка окружения

    Создайте файл .env в корне проекта и заполните его следующим образом:
    
        POSTGRES_USER=myuser
        POSTGRES_PASSWORD=mypassword
        POSTGRES_DB=mydatabase
        DATABASE_URL=postgres://myuser:mypassword@db:5432/mydatabase

    Для фронтенда создайте файл vueone/.env.production и добавьте в него URL для входа:

    VITE_API_URL=https://your-backend-url.com

2. Сборка и запуск контейнеров

    Чтобы собрать и запустить контейнеры для фронтенда, бекенда и базы данных, выполните команду:

        docker-compose up --build

    Это создаст и запустит следующие сервисы:

        db: PostgreSQL база данных
        backend: Бекенд на FastAPI, работающий на порту 8000
        frontend: Фронтенд на Vue.js, работающий на порту 3000
        nginx: Nginx сервер, проксирующий запросы на фронтенд и бекенд

3. Запуск бота вручную

    Чтобы запустить бота Telegram, выполните следующие шаги:

     Перейдите в директорию с ботом:

        Запустите бота с использованием Poetry:

            poetry run start-bot

