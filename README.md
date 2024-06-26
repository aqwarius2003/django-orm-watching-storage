## Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.
Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.
### Установка и запуск

Python3 должен быть уже установлен. 

Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

        pip install -r requirements.txt
### Переменные
Создайте файл .env на рядом с manage.py и заполните его данными (**ЗНАЧЕНИЕ**=**ПЕРЕМЕННАЯ**):

* **DB_ENGINE** - к примеру _django.db.backends.postgresql_psycopg2_
* **DB_HOST** - хост
* **DB_PORT** - порт
* **DB_NAME** - название БД
* **DB_USER** - имя пользователя к БД
* **DB_PASSWORD** - пароль к БД
* **SECRET_KEY** - ключ к БД

**DEBUG**=_True/False_ - включает/отключает отладочную информацию на сайте. 
При отсутствии этого параметра, по умолчанию _**False**_

**ALLOWED_HOSTS** - настройка безопасности вашего сайта. Укажите домены и IP-адреса,
которые могут обращаться к вашему приложению.

Например: 

            ALLOWED_HOSTS = ['127.0.0.1','localhost']



### Запуск
Сервер запускается командой

        python manage.py runserver 0.0.0.0:8000

По адресу [127.0.0.1:8000](127.0.0.1:8000), вы увидите заглавную страницу сайта

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).