include .env
export $(shell sed 's/=.*//' .env)

.PHONY: help up start stop restart status ps clean

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up: ## Start all or c=<name> containers in foreground
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) up $(c)

start: ## Start all or c=<name> containers in background
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) up -d $(c)

build: ## Build all or c=<name> containers in foreground
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) up --build $(c)

build-d: ## Build all or c=<name> containers in background
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) up --build -d $(c)

stop: ## Stop all or c=<name> containers
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) stop $(c)

restart: ## Restart all or c=<name> containers
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) stop $(c)
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) up -d $(c)

rebuild: ## Rebuild all or c=<name> containers
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) down $(c)
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) up --build -d $(c)

logs: ## Show logs for all or c=<name> containers
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) logs --tail=$(or $(n), 100) -f $(c)

status: ## Show status of containers
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) ps

ps: status ## Alias of status

clean: ## Clean all data
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) down

down: clean ## Alias of clean

images: ## Show all images
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) images

exec: ## Exec container
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec $(or $(c), app) bash

shell: ## Exec shell
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec app ipython

run-command: ## Run command in shell
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec app python -c="$(c)"

lint: ## Show images
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) exec app sh -c "flake8 $(key) api"