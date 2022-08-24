# apache2ctl -D FOREGROUND
python3 manage.py makemigrations new
python3 manage.py makemigrations apijson
python3 manage.py migrate new
python3 manage.py migrate apijson
python3 manage.py runserver 0.0.0.0:8000



