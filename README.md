# tmob test

## Install

```
docker-compose up -d
python3 -mvenv env
source env/bin/activate
cd tmob
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

## Test

En el directorio raíz del repo:

```
cat test_db.sql | mysql -h 127.0.0.1 -u root -p
<escribir root>
source env/bin/activate
cd tmob
./manage.py test
```
