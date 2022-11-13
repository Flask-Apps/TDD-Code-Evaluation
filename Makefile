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
	docker-compose exec users python manage.py test

cov:
	docker-compose exec users python manage.py cov

flake8:
	docker-compose exec users flake8 project

test-run:
	docker-compose \
	run users python manage.py test


seed_db:
	docker-compose \
	run users python manage.py seed_db

create_ec2: |
	docker-machine create --driver amazonec2 \
	--amazonec2-instace-type "t2.micro" \
	--amazonec2-region "ap-south-1" \
	--amazonec2-open-port 5001 \
	tdd-prod