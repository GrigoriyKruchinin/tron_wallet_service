# Tron Wallet Service

Этот микросервис предоставляет информацию по адресу в сети Tron, включая его bandwidth, energy и баланс TRX. Также все запросы на информацию сохраняются в базе данных для дальнейшего использования и анализа.

## Структура проекта

Проект состоит из нескольких компонентов:
- **FastAPI**: для создания веб-API.
- **SQLAlchemy**: для работы с базой данных.
- **Tronpy**: для взаимодействия с сетью Tron.
- **Pytest**: для юнит- и интеграционных тестов.

## Установка и настройка

Для работы с проектом вам нужно установить необходимые зависимости и настроить окружение.

### 1. Клонировать репозиторий

```bash
git clone git@github.com:GrigoriyKruchinin/tron_wallet_service.git
cd tron_wallet_service
```
### 2. Создать файл .env
Скопируйте пример конфигурации .env.example в файл .env:
```
cp .env.example .env
```

В файле .env необходимо будет настроить параметры подключения к базе данных и другие конфигурационные параметры.

### 3. Запустить проект с помощью Docker Compose
Проект использует docker-compose для настройки и запуска всех необходимых сервисов, включая базу данных и приложение.

```
make up
```
Для остановки приложения:

```
make down
```

### 4. Доступ к API
После запуска проекта, микросервис будет доступен по следующему адресу:

http://localhost:8000

Документация swagger доступна по:
http://localhost:8000/docs 

### 5. Эндпоинты API

**POST /wallet-info**
Этот эндпоинт принимает адрес кошелька в сети Tron и возвращает информацию о его балансе TRX, bandwidth и energy. Также запрос будет записан в базу данных.

Тело запроса:
```json
{
  "address": "TQFSyTc7eRR1C8auUN3dmBde2g6iHZMz9f"
}
```
Ответ:
```json
{
  "address": "TQFSyTc7eRR1C8auUN3dmBde2g6iHZMz9f",
  "bandwidth": 1234,
  "energy": 5678,
  "trx_balance": 100.5
}
```

**GET /wallet-info**
Этот эндпоинт позволяет получить список последних запросов к API с пагинацией.

Запрос:
`GET /wallet-info?page=1&limit=10`

Ответ:

```json
{
  "results": [
    {
      "address": "TQFSyTc7eRR1C8auUN3dmBde2g6iHZMz9f",
      "bandwidth": 1234,
      "energy": 5678,
      "trx_balance": 100.5,
      "timestamp": "2025-02-14T12:00:00Z"
    },
    {
      "address": "TJhS7d2gB5yt6UwK7PrZyV86Sh1Za5MKXu",
      "bandwidth": 2000,
      "energy": 8000,
      "trx_balance": 250.0,
      "timestamp": "2025-02-14T12:05:00Z"
    }
  ]
}
```

## Контакты
- Автор: Grigoriy Kruchinin
- [GitHub](https://github.com/GrigoriyKruchinin)
- [Email](mailto:gkruchinin75@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/grigoriy-kruchinin/)