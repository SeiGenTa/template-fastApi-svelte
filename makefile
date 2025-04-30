# Makefile finalizado, leyendo .env

# Variables de entorno
ifneq (,$(wildcard .env))
	include .env
	export $(shell sed 's/=.*//' .env)
endif

# Variables del proyecto
VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
UVICORN := $(VENV_DIR)/bin/uvicorn

init:
	@echo "Creating virtual environment if not exists..."
	@if [ ! -d $(VENV_DIR) ]; then \
		python3 -m venv $(VENV_DIR); \
	fi
	@echo "Installing Python dependencies..."
	@if [ -f requirements.txt ]; then \
		$(PIP) install -r requirements.txt; \
	else \
		echo "No requirements.txt found. Please create it manually."; \
	fi
	@echo "Installing frontend dependencies..."
	@cd front && npm install
	@echo "Frontend dependencies installed."
	@$(MAKE) build

clean:
	@echo "Cleaning up build files and virtual environment..."
	@rm -rf ./dist
	@rm -rf $(VENV_DIR)
	@echo "Cleanup complete."

install:
	@echo "Installing dependencies..."
	@if [ -z "$(lib)" ]; then \
		$(PIP) install -r requirements.txt; \
	else \
		$(PIP) install "$(lib)"; \
	fi
	@echo "Updating requirements.txt..."
	@$(PIP) freeze > requirements.txt
	@echo "Dependencies installed."

run-server:
	@echo "Running backend server at port $(PORT_BACK)..."
	@$(UVICORN) src.app:app --host 0.0.0.0 --port $(PORT_BACK)

run-prod-server:
	@echo "Running production backend server at port $(PORT_BACK)..."
	@$(UVICORN) src.app:app --host 0.0.0.0 --port $(PORT_BACK)

NGINX_CONF := $(shell pwd)/nginx.conf

run: generate-nginx
	@echo "Starting nginx with configuration: $(NGINX_CONF) on port $(PORT)..."
	@sudo nginx -c $(NGINX_CONF)
	@echo "nginx started successfully."
	@bash -c ' \
		trap "echo Stopping nginx...; sudo nginx -s stop; kill 0" SIGINT; \
		$(UVICORN) src.app:app --host 0.0.0.0 --port $(PORT_BACK) --reload & \
		cd front && npm run dev -- --port $(PORT_FRONT) & \
		echo "You can access the application at http://localhost:$(PORT)"; \
		echo "Press Ctrl+C to stop the servers..."; \
		wait \
	'

build:
	@echo "Building the frontend..."
	@rm -rf ./dist
	@cd front && npm install && npm run build
	@mkdir -p dist
	@cp -r front/dist/* dist/
	@echo "Frontend build completed."

run-production:
	@echo "Starting production backend server..."
	@$(UVICORN) src.app:app --host 0.0.0.0 --port $(PORT)

stop-nginx:
	@echo "Stopping nginx..."
	@sudo nginx -s stop
	@echo "nginx stopped successfully."

generate-nginx:
	@echo "Generating nginx.conf from template using Python inside venv..."
	@$(VENV_DIR)/bin/python generate_nginx.py


