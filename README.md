# roboline_test
 
Инструкция по запуску приложения roboline_test

Для операционной системы Windows:

1.  Откройте приложение Выполнить с помощью комбинации клавиш 'Win+R'
2.  Откройте командую строку, введя в приложение Выполнить 'cmd' и подтвердив запрос клавишей Enter
3.  В командной строке введите 'python', чтобы проверить наличие установленного приложения Python
3.1 Если приложение Python не установлено, то откроется Microsoft Store (MS) и откроет страницу с последней версией приложения Python
3.2 Приложение было написано на версии Python 3.12, поэтому установите именно эту версию, перейдя по ссылке https://apps.microsoft.com/detail/9ncvdn91xzqp?ocid=pdpshare&hl=en-us&gl=US, и нажав на кнопку 'View in Store'
3.3 Откроется MS, в котором необходимо будет нажать 'Получить'
4.  Когда Python 3.12 установлен, вы сможете проверить это в командной строке, снова введя 'python'. Откроется терминал для ввода команд. Введите 'exit()' для выхода из него
5.  С помощью команд cd <директория1>\<директория2> перейдите в удобную для вас директорию
6.  Скачайте приложение, введя команду 'git clone https://github.com/KycokKypuzu/roboline_test'
7.  После скачивания, перейдите в папку с проектом командой 'cd roboline_test\rl'
8.  Установите фреймворк django для запуска приложения с помощью команды 'pip install django'
9.  После установки django введите в командную строку 'python manage.py makemigrations' и после выполнения этой команды введите 'python manage.py magrate'
10. После выполнения миграций вы можете запустить проект, либо сначала создать пользователя superadmin
10.1    Для создания пользователя superadmin введите в командную строку 'python manage.py createsuperuser'
10.2    Введите имя пользователя, email, пароль и его подтверждение
11. Запустите проект, введя команду 'python manage.py runserver'
12. После ожидания вы получите ссылку на тестовый сервер с приложением формата http://127.0.0.1:8000/
13. Перейдите по ссылке, чтобы открыть проект в браузере
14. Проект готов к работе