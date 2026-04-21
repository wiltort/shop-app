# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем переменную окружения, чтобы логи Python выводились сразу
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы с зависимостями и устанавливаем их
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry self add poetry-plugin-dotenv && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --without dev

# Копируем весь код проекта в контейнер
COPY . .

# Указываем порт, который будет слушать приложение
EXPOSE 8000
