# Практическая работа №3
Архипов Данил

**Для копирования проекта и перехода в рабочюю директорию необходимов исполнить команды:**

    https://github.com/urfuproject1/1.git
    cd practice3_arkhipovda


**Установка окружения и зависимостей:**

    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt

**Запуск веб-сервера для разработки:**

    uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000

Далее можно производить HTTP запросы:

    Endpoint: http://127.0.0.1:8000/predict/
    Method: POST
    Content-Type: application/json
    Body: {"url": "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"}

Вставить ссылку на картинку в формате jpeg

Пример curl запроса:

    curl -X 'POST' \
        'http://127.0.0.1:8000/predict/' \
        -H 'Content-Type: application/json' \
        -d '{
        "url": "https://w.forfun.com/fetch/ac/ac4ab3ca5717e7787567def744601ce6.jpeg?w=1200&r=0.5625"
    }'

На выходе описание изображения
