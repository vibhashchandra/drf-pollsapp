# drf-pollsapp
### Install requirements
```
pip install -r requirements.txt
```

### Migrate and start server
```
python pollsapp/manage.py makemigrations

python pollsapp/manage.py migrate

python pollsapp/manage.py runserver
```

### Endpoints
http://localhost:8000/api/questions/

http://localhost:8000/api/choices/
