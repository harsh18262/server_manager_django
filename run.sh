#/usr/local/bin/wssh --origin='http://127.0.0.1:8000' &
python /code/manage.py runserver 0.0.0.0:8000 &
/usr/local/bin/wssh --origin='http://127.0.0.1:8000'
