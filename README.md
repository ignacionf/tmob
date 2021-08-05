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
