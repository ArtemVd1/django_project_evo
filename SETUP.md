# Cars park
Welcome project with Python and Django

---

### Project setup in IDE
* You should uncomment parts of code with comment
'Settings for running in pycharm or deploying to heroku' in [settings.py](./welcome_proj/settings.py)
* You should comment parts of code with comment
'Settings for running with Docker' in [settings.py](./welcome_proj/settings.py)
* You should install python 3.10 from [python.org](https://www.python.org/downloads/)

---

In Terminal for starting project (you should be in the folder 'welcome_proj' of the project):
```
$ pip install -r requirements.txt
$ python manage.py runserver
```

---

For filling database with test data:
```
$ python manage.py shell
>>> from welcome.fill_db import create_users
>>> create_users()
```

---

Open in browser [welcome_proj](http://127.0.0.1:8000/welcome/)

---
### Project setup in Docker

---
* You should comment parts of code with comment
'Settings for running in pycharm or deploying to heroku' in [settings.py](./welcome_proj/settings.py)
* You should uncomment parts of code with comment
'Settings for running with Docker' in [settings.py](./welcome_proj/settings.py)
* In Terminal for starting project (you should be in the root folder of the project):
```
$ docker-compose up -d --build
```

---

Open in browser [welcome_proj](http://127.0.0.1:8000/welcome/)

---
