# shop-app
Django + Stripe API бэкенд для оплаты заказов
## Установка

### Способ 1. Докер
```bash
git clone https://github.com/wiltort/shop-app.git
cd shop-app

cp .env.example .env # создание .env

# Введите свои ключи для Stripe
    # STRIPE_PUBLIC_KEY=pk_
    # STRIPE_SECRET_KEY=sk_***
docker compose -f docker-compose.dev.yaml up -d
```
    Сервис доступен на http://127.0.0.1:8000/
    Админка - http://127.0.0.1:8000/admin/
### Способ 2. Локально
```bash
git clone https://github.com/wiltort/shop-app.git
cd shop-app

cp .env.example .env # создание .env

# Введите свои ключи для Stripe
    # STRIPE_PUBLIC_KEY=pk_
    # STRIPE_SECRET_KEY=sk_***

# Установите poetry
pip install poetry
poetry install

poetry run python manage.py migrate
poetry run python manage.py runserver
```

## Описание эндпойнтов
- GET	/api/v1/items/{pk}/   Детали товара
- POST	/api/v1/buy/{pk}/	Создать сессию оплаты товара
- GET	/api/v1/orders/{pk}/	Детали заказа
- POST	/api/v1/orders/{pk}/buy/ 	Создать сессию оплаты заказа
