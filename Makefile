
help:
	@echo "up:\t\t\t container up"
	@echo "down:\t\t\t container down"
	@echo "stop:\t\t\t container stop"
	@echo "test:\t\t\t start tests"
	@echo "makemigrations:\t\t makemigrations"
	@echo "migrate:\t\t migrate"
	@echo "shell:\t\t shell"
	@echo "logs:\t\t logs"
	@echo "build:\t\t logs"

.PHONY: up
up:
	@docker-compose up -d

.PHONY:
down: up
	@docker-compose down

.PHONY:
build: down
	@docker-compose build web

.PHONY:
stop: up
	@docker-compose stop

.PHONY:
test: up
	@docker-compose exec web python manage.py test

.PHONY:
makemigrations: up
	@docker-compose exec web python manage.py makemigrations

.PHONY:
migrate: up
	@docker-compose exec web python manage.py migrate

.PHONY:
shell: up
	@docker-compose exec web bash

.PHONY:
logs: up
	@docker-compose logs -f web
