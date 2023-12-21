# Программная инженерия. Итоговый проект (PJ)
Проект направлен на создание веб-приложения, которое позволяет определить достопримечательность города Москва по фотографии.  
Также реализован API, позволяющий передать в json формате URL картинки для распознания достопримечательности.  
Для проекта использована собственная модель https://huggingface.co/Poliandr/moscow-attractions  
Обучение модели произведено на датасете из 150 картинок, найденных поисковой машиной Hugging Face, для каждого из 5 сетов.

**Инструкция по локальной установке**

git clone git@github.com:urfuproject1/1.git   
cd 1  
pip install -r requirements.txt

***Запуск приложения***

streamlit run main.py

***Запуск API***

uvicorn api:app

***Запуск теста***

pytest

автотест Continuous Integration осуществляет GitHub Actions

## Структура приложения
main.py - код web-приложения  
api.py - код API  
test_api.py - код автотестирования  
requirements.txt - файл зависимостей

## Пример использования

***Использование web приложения***
1. Открыть приложение
2. Использовать форму "Загрузка изображения"
3. Выбрать и загрузить файл формата jpeg  
   Картинки соответсвующей тематики можно взять из описания модели: https://huggingface.co/Poliandr/moscow-attractions
5. Получить результат предсказания модели

***Использование API приложения***

Посредстом curl передать http://127.0.0.1:8000/predict/ POST-запрос, формата json {"url": "ссылка_на_картинку"}.  
URL картинок соответсвующей тематики можно взять из описания модели: https://huggingface.co/Poliandr/moscow-attractions  
Пример передаваемого на сервер запроса:  
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://huggingface.co/Poliandr/moscow-attractions/resolve/main/images/Grand_Kremlin_Palace.jpg"
}'

## Команда
-  Дуплин Александр, ML
-  Архипов Даниил, Full Stack-разработчик
-  Павел Завражин, Тестировщик-QA инженер