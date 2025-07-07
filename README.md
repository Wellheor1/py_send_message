# py_send_message
Сервис для отправки сообщений на почту по api

## Необходимые инструменты
[Poetry](https://python-poetry.org/docs/)*

[make](https://www.make.com/en)

[docker](https://www.docker.com/)

## Установка
### docker
Сборка образа
```
docker build -t py_send_message dockerfile
```
Запуск контейнера
```
docker run py_send_message
```
### make
```
make install
```
### Вручную
Создание виртуального окружения
```
python3 -m venv .venv
```
Активация виртуального окружения
```
source .venv/bin/activate
```
Установка зависимостей через poetry
```
poetry install
```

## Запуск
### Разработка
```
uvicorn app.main:app --reload
```
