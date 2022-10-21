exp: |
	export FLASK_APP=project/__init__.py
	export FLASK_DEBUG=1
recreate: 
	docker-compose -f docker-compose-dev.yml \
	run users python manage.py recreate_db
database:
	docker exec -it $(docker ps -aqf "name=users-db") psql -U postgres