Инструкция по запуску

1. Настройте свой сервер: убедитесь, что он готов к работе с Docker и Docker Compose, 
настройте SSH-доступ к серверу для деплоя через GitHub Actions.

2. Создайте на сервере SSH-ключ, запульте из репозитория gitlab код проекта. 
При необходимости пропишите в config/settings.py адрес сервера в ALLOWED_HOSTS = [<адрес сервера>] (строка 17). 
Создайте на сервере в корне проекта файл .env по образцу .env-sample.

3. На сервере установите Docker и docker-compose (команда apt-install docker docker-compose)

4. Создайте и запустите контейнер командой docker-compose up -d --build, а затем docker-compose up -d

5. При необходимости заполните базу демонстрационными данными:

docker exec -it <ID контейнера приложения> python3 manage.py loaddata data/users_data.json

docker exec -it <ID контейнера приложения> python3 manage.py loaddata data/habits_data.json