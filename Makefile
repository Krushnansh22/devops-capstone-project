.PHONY: help install test lint coverage run seed demo build push deploy delete tekton clean validate

PYTHON ?= python3
IMAGE ?= accounts:1
REGISTRY ?= localhost:32000
NAMESPACE ?= default

help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-\\.]+:.*?##/ { printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

install: ## Install Python dependencies
	$(PYTHON) -m pip install --upgrade pip wheel
	$(PYTHON) -m pip install -r requirements.txt

test: ## Run the unit tests
	$(PYTHON) -m pytest -q

coverage: ## Run the unit tests with coverage
	$(PYTHON) -m pytest --cov=service --cov-report=term-missing

lint: ## Run flake8 and pylint
	$(PYTHON) -m flake8 service tests --count --max-line-length=127 --statistics
	$(PYTHON) -m pylint service --score=no || true

run: ## Run the service locally on port 5000
	FLASK_APP=service:app $(PYTHON) -m flask run --host 0.0.0.0 --port 5000

seed: ## Create and seed the local database
	FLASK_APP=service:app $(PYTHON) -m flask db-create
	FLASK_APP=service:app $(PYTHON) -m flask seed-db

demo: ## Exercise the REST API and write evidence/rest-*.txt
	bash scripts/demo-api.sh

build: ## Build the Docker image
	docker build --rm --pull --tag $(IMAGE) .

push: ## Tag and push the image to the local registry
	docker tag $(IMAGE) $(REGISTRY)/$(IMAGE)
	docker push $(REGISTRY)/$(IMAGE)

deploy: ## Apply the Kubernetes manifests
	kubectl apply -f deploy/postgresql.yaml
	kubectl apply -f deploy/deployment.yaml
	kubectl apply -f deploy/service.yaml
	kubectl apply -f deploy/route.yaml

delete: ## Delete the Kubernetes resources
	kubectl delete -f deploy/route.yaml --ignore-not-found
	kubectl delete -f deploy/service.yaml --ignore-not-found
	kubectl delete -f deploy/deployment.yaml --ignore-not-found
	kubectl delete -f deploy/postgresql.yaml --ignore-not-found

tekton: ## Apply the Tekton tasks, pipeline, and PVC
	kubectl apply -f tekton/tasks.yaml
	kubectl apply -f tekton/pipeline.yaml
	kubectl apply -f tekton/pvc.yaml

pipelinerun: ## Start the Tekton pipeline run
	kubectl create -f tekton/pipelinerun.yaml

validate: ## Validate the whole project
	bash scripts/validate.sh

clean: ## Remove local artifacts
	rm -rf __pycache__ .pytest_cache .coverage htmlcov
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	rm -f accounts.db tests/test_accounts.db
