# DevOps Capstone Project — Customer Accounts Microservice

[![CI Build](https://github.com/Krushnansh22/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Krushnansh22/devops-capstone-project/actions/workflows/ci-build.yaml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)](https://www.python.org/)

Final project for the **IBM DevOps and Software Engineering Professional
Certificate** — course 15, **DevOps Capstone Project**.

The project is a **Customer Accounts REST microservice** built with Flask and
PostgreSQL, developed with TDD over three sprints, secured with Flask-Talisman
and Flask-CORS, containerized with Docker, deployed to Kubernetes/OpenShift,
and delivered through a Tekton CD pipeline.

---

## Architecture

```
                        +-----------------------------+
   HTTPS  /accounts     |        OpenShift Route      |
  --------------------> |            accounts         |
                        +--------------+--------------+
                                       |
                        +--------------v--------------+
                        |   accounts Deployment       |
                        |   gunicorn + Flask :8080    |
                        |   Talisman + CORS           |
                        +--------------+--------------+
                                       |
                        +--------------v--------------+
                        |   postgres Service :5432    |
                        |   postgres Deployment       |
                        |   postgres-pvc              |
                        +-----------------------------+
```

Development flow:

```
GitHub  ->  GitHub Actions (lint + pytest)  ->  Tekton cd-pipeline
                                              cleanup -> clone -> lint
                                              -> test -> buildah -> deploy
```

---

## REST API

| Method | Path | Description | Success | Errors |
| ------ | ---- | ----------- | ------- | ------ |
| GET | `/health` | Health probe | 200 | — |
| GET | `/` | Service name and version | 200 | — |
| POST | `/accounts` | Create an account | 201 + `Location` | 400, 415 |
| GET | `/accounts` | List all accounts | 200 | — |
| GET | `/accounts/<id>` | Read one account | 200 | 404 |
| PUT | `/accounts/<id>` | Update an account | 200 | 400, 404, 415 |
| DELETE | `/accounts/<id>` | Delete an account | 204 | 404 |

Account fields: `id`, `name`, `email`, `address`, `phone_number` (optional),
`date_joined`.

### Example

```bash
curl -i -X POST http://127.0.0.1:5000/accounts \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1212"}'
```

```
HTTP/1.1 201 CREATED
Location: http://127.0.0.1:5000/accounts/1
...
```

---

## Tech stack

| Area | Tool |
| ---- | ---- |
| Language | Python 3.12 |
| Web | Flask 3, gunicorn |
| Data | Flask-SQLAlchemy, SQLAlchemy 2, PostgreSQL 16 (SQLite for local tests) |
| Tests | pytest, factory-boy |
| Lint | flake8, pylint, black |
| CI | GitHub Actions |
| Security | Flask-Talisman, Flask-CORS |
| Container | Docker (`python:3.12-slim`, non-root, health check) |
| Orchestration | Kubernetes / OpenShift |
| CD | Tekton |

---

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# create and seed the SQLite database
FLASK_APP=service:app flask db-create
FLASK_APP=service:app flask seed-db

# start the service
FLASK_APP=service:app flask run --port 5000
```

Or use the helper scripts:

```bash
bash scripts/run.sh          # start on port 5000
bash scripts/test.sh         # run the tests
bash scripts/demo-api.sh     # exercise every endpoint and save evidence
```

The service also starts with gunicorn:

```bash
gunicorn --bind 0.0.0.0:8080 --workers=2 service:app
```

---

## Tests

```bash
pytest -q
```

```
................................
32 passed
```

Tests cover the model (create, read, update, delete, list, find by name,
serialization, validation) and every route, including `404`, `400`, `415`, and
the security headers.

---

## Continuous integration

`.github/workflows/ci-build.yaml` runs on every push and pull request to
`main`:

1. checkout
2. install dependencies
3. `flake8` static analysis
4. `pytest` against a PostgreSQL service container

The status badge at the top of this README reflects the latest run.

---

## Security

`service/__init__.py` enables:

- **Flask-Talisman** — `Content-Security-Policy`, `X-Frame-Options`,
  `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, and HSTS
  when `FORCE_HTTPS=true`
- **Flask-CORS** — `Access-Control-Allow-Origin` policy, configurable with
  `CORS_ORIGINS`

Verify with:

```bash
curl -i http://127.0.0.1:5000/health
```

---

## Docker

```bash
docker build -t accounts:1 .
docker run --rm -p 8080:8080 accounts:1
curl -i http://127.0.0.1:8080/health
```

The image runs as the unprivileged `app` user, exposes port `8080`, and has a
`HEALTHCHECK` that calls `/health`.

---

## Kubernetes / OpenShift

```bash
kubectl apply -f deploy/postgresql.yaml
kubectl apply -f deploy/deployment.yaml
kubectl apply -f deploy/service.yaml
kubectl apply -f deploy/route.yaml      # OpenShift only

kubectl get all -l app=accounts
```

Push the image to your registry first:

```bash
docker tag accounts:1 us.icr.io/$SN_ICR_NAMESPACE/accounts:1
docker push us.icr.io/$SN_ICR_NAMESPACE/accounts:1
```

---

## Tekton CD pipeline

```bash
kubectl apply -f tekton/tasks.yaml
kubectl apply -f tekton/pipeline.yaml
kubectl apply -f tekton/pvc.yaml

tkn pipeline start cd-pipeline \
  -p repo-url=https://github.com/Krushnansh22/devops-capstone-project.git \
  -p branch=main \
  -p build-image=image-registry.openshift-image-registry.svc:5000/$SN_ICR_NAMESPACE/accounts:1 \
  -w name=pipeline-workspace,claimName=pipelinerun-pvc \
  -s pipeline --showlog
```

Pipeline stages: `cleanup → git-clone → flake8 → pytest → buildah → deploy`.

Capture the run log for the final submission:

```bash
tkn pipelinerun logs -L > pipelinerun.txt
```

---

## Repository layout

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/story_template.md
│   └── workflows/ci-build.yaml
├── deploy/                 # Kubernetes and OpenShift manifests
├── docs/                   # user stories, kanban board, sprint plans, checklist
├── evidence/               # captured test, API, and security output
├── scripts/                # run, test, demo, build, deploy, publish, validate
├── service/
│   ├── __init__.py         # app factory, Talisman, CORS
│   ├── config.py
│   ├── models.py           # Account model
│   ├── routes.py           # REST endpoints
│   └── common/             # status codes, errors, logging, CLI commands
├── tekton/                 # tasks, pipeline, PVC, pipelinerun
├── tests/                  # model, route, and CLI tests
├── Dockerfile
├── Makefile
├── Procfile
├── requirements.txt
└── wsgi.py
```

---

## Documentation

- `docs/user-stories.md` — nine user stories with acceptance criteria
- `docs/kanban-board.md` — board states for every sprint
- `docs/SPRINT_PLANS.md` — sprint goals, velocity, definition of done
- `docs/EVIDENCE_CHECKLIST.md` — every screenshot the grader expects
- `SUBMISSION_GUIDE.md` — end-to-end submission walkthrough

---

## License

Licensed under the **Apache License 2.0**. See `LICENSE`.
