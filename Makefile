start:
	poetry run python manage.py runserver
makemig:
	poetry run python manage.py makemigrations
mig:
	poetry run python manage.py migrate

