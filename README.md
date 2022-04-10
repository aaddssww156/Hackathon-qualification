# Hackathon-qualification
Floppers hackathon qualification app
test commit #2


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
