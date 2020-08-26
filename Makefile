name := neosapience/appname-api
tag := v0.0.1
pwd := $(shell pwd)

up:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

test:
	@docker-compose -f docker-compose.yml -f docker-compose.test.yml up -d

logs:
	@docker-compose logs -f api

down:
	@docker-compose down

stop:
	@docker-compose stop ${service}

ps:
	@docker-compose ps

build-base:
	@docker build . -t ${name}:base -f docker/Dockerfile.base

build:
	@docker build . -t ${name}:dev -f docker/Dockerfile --build-arg MYAPP_API_VERSION=${name}:dev

build-dist:
	@docker build . -t ${name}:${tag} --build-arg MYAPP_API_VERSION=${name}:${tag}

ls:
	@docker images ${name}

h:
	@docker history ${name}:dev

push:
	@docker push ${name}:${tag}

sh:
	@docker run --rm -it ${name}:dev sh