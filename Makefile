exp: |
	export FLASK_APP=project/__init__.py
	export FLASK_DEBUG=1
recreate: 
	docker-compose \
	run users python manage.py recreate_db
database:
	docker exec -it $(docker ps -aqf "name=users-db") psql -U postgres
build:
	docker-compose build

test:
	docker-compose \
	run users python manage.py test