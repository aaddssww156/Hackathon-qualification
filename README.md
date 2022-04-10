# Hackathon-qualification
Floppa hackathon qualification app

# Android
Стек:
- Для http соединения с сервером использовались retrofit+okhttp3+coroutines+gson
- Для отрисовки графиков использовалась библиотека [AAChartModel](https://github.com/AAChartModel/AAChartCore-Kotlin)

Как использовать:
- Запустите backend сервер по инструкции ниже. Без этих шагов приложение не будет работать!
- Создайте два устройства (1 - temperature, 2 - lights)
- Temperature - датчик температуры в офисе
- Lights - датчик освещенности офиса
- После создания устройств, добавьте им записей (через swagger, описано ниже)
- Измените свой baseURL в файле RetrofitHelper на ip адрес, по которому запущен сервер
- Когда тестовые устройства и данные будут добавлены, а сервер запущен, то смело запускайте приложение - оно вам понравится!

# Backend
Стек:
- Для Api использовались django+drf
- Для бд использовался postgres

Эндпоинты:
- POST: /data/ - отправить данные на устройство(через postman эмулировать отправку данных с умного устройства)
- GET: /data/ - получить данные со всех устройств, 2 опциональных параметра: id устройства(получить данные только с него), timestamps(получить данные за последние n часов)
- POST: /device/ - добавить умное устройство в бд 

Билд и запуск
1. Переименовать *.env.dev-sample* to *.env.dev*.
2. Ввести 2 команды в терминал, и всё, всё работает, очень круто как по мне

    ```sh
    $ docker-compose up -d --build
    $ docker-compose up
    ```

    Проверить можно по адресу [http://localhost:8000](http://localhost:8000). Также если перейти на [http://localhost:8000/swagger](http://localhost:8000/swagger) можно увидеть автодоки сваггера, которые приятные+полезные
