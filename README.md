# Short-url
### Create virtual environment
**Windows**
1. virtualenv venv
2. .\venv\Scripts\activate
3. pip install -r requirements.txt

**Linux**
1. virtualenv venv
2. source venv/bin/activate
3. pip3 install -r requirements.txt

### Initialize database
**Windows**
1. python manage.py makemigrations
2. python manage.py migrate

**Linux**
1. python3 manage.py makemigrations
2. python3 manage.py migrate

### Run app
**Windows**
1. python manage.py runserver 8000
2. python manage.py runserver 8000

**Linux**
1. python3 manage.py runserver 8000
2. python3 manage.py runserver 8000
