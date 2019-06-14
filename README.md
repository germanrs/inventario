# inventario
git clone https://github.com/germanrs/inventario

cd inventario

git checkout theme2

pip install -r Requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000
