release: python manage.py makemigrations blog
release: python manage.py makemigrations registration
release: python manage.py migrate
web: gunicorn mysite.wsgi --log-file -