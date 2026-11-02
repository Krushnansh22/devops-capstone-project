# Customer Accounts — User Stories

Project: `devops-capstone-project`
Service: Customer Accounts REST API (Flask)
Database: PostgreSQL (SQLite for local development)

Story points use the Fibonacci scale **3, 5, 8, 13** (S, M, L, XL).

---

## Story 1 — Set up the development environment

**As a** developer  
**I need** a repeatable local development environment  
**So that** I can develop and test the Accounts service consistently

**Details and Assumptions**

- Python 3.12, a virtual environment, and `requirements.txt`
- `pytest` and `flake8` available locally
- A `setup.cfg` that configures the test runner and linter

**Acceptance Criteria**

```gherkin
Given a clean checkout of the repository
When I create a virtual environment and install requirements.txt
Then I can run the test suite with pytest
And flake8 reports no errors
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| technical debt | 3 | Sprint 1 |

---

## Story 2 — Read an account

**As a** customer service agent  
**I need** to read a single account by its id  
**So that** I can answer questions about a customer

**Details and Assumptions**

- `GET /accounts/<id>`
- Returns `404` when the account does not exist

**Acceptance Criteria**

```gherkin
Given an account exists with id 1
When I request GET /accounts/1
Then I receive 200 OK
And the response body contains the account details

Given no account exists with id 9999
When I request GET /accounts/9999
Then I receive 404 Not Found
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| enhancement | 3 | Sprint 1 |

---

## Story 3 — Update an account

**As a** customer service agent  
**I need** to update an existing account  
**So that** customer details stay accurate

**Details and Assumptions**

- `PUT /accounts/<id>` with a JSON body
- Only `application/json` is accepted

**Acceptance Criteria**

```gherkin
Given an account exists with id 1
When I send PUT /accounts/1 with a new address
Then I receive 200 OK
And the returned account has the new address

Given the request has no JSON content type
When I send PUT /accounts/1
Then I receive 415 Unsupported Media Type
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| enhancement | 5 | Sprint 1 |

---

## Story 4 — Delete an account

**As a** customer service agent  
**I need** to delete an account  
**So that** closed accounts are removed from the system

**Details and Assumptions**

- `DELETE /accounts/<id>`
- Returns `204 No Content` on success, `404` when missing

**Acceptance Criteria**

```gherkin
Given an account exists with id 1
When I send DELETE /accounts/1
Then I receive 204 No Content
And a subsequent GET /accounts/1 returns 404

Given no account exists with id 9999
When I send DELETE /accounts/9999
Then I receive 404 Not Found
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| enhancement | 3 | Sprint 1 |

---

## Story 5 — List all accounts

**As a** customer service agent  
**I need** to list every account  
**So that** I can browse the customer base

**Details and Assumptions**

- `GET /accounts`
- Returns `[]` with `200 OK` when there are no accounts

**Acceptance Criteria**

```gherkin
Given five accounts exist
When I request GET /accounts
Then I receive 200 OK
And the response contains five accounts

Given no accounts exist
When I request GET /accounts
Then I receive 200 OK
And the response is an empty list
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| enhancement | 3 | Sprint 1 |

---

## Story 6 — Containerize the microservice using Docker

**As a** DevOps engineer  
**I need** a Docker image of the Accounts service  
**So that** it can run identically in every environment

**Details and Assumptions**

- Multi-stage-free `python:3.12-slim` image
- Runs as a non-root user
- Exposes port `8080` and has a `HEALTHCHECK`

**Acceptance Criteria**

```gherkin
Given the Dockerfile and application source
When I run docker build -t accounts:1 .
Then the image builds successfully
And docker run -p 8080:8080 accounts:1 serves GET /health
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| technical debt | 5 | Sprint 3 |

---

## Story 7 — Deploy the Docker image to Kubernetes

**As a** DevOps engineer  
**I need** to deploy the Accounts image to Kubernetes/OpenShift  
**So that** the service is available to other microservices

**Details and Assumptions**

- `deploy/deployment.yaml`, `deploy/service.yaml`, `deploy/route.yaml`
- PostgreSQL deployed alongside the service
- Readiness and liveness probes on `/health`

**Acceptance Criteria**

```gherkin
Given a Kubernetes cluster and the accounts image
When I apply the manifests in deploy/
Then the accounts deployment reaches Ready
And GET /accounts through the route returns 200 OK
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| technical debt | 8 | Sprint 3 |

---

## Story 8 — Secure the RESTful service

**As a** security-conscious developer  
**I need** secure headers and a CORS policy  
**So that** the API is protected against common browser attacks

**Details and Assumptions**

- Flask-Talisman for security headers
- Flask-CORS for cross-origin access
- HTTPS enforced in production

**Acceptance Criteria**

```gherkin
Given the site is secured
When a REST API request is made
Then secure headers and a CORS policy should be returned
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| enhancement | 5 | Sprint 2 |

---

## Story 9 — Build an automated CD pipeline

**As a** DevOps engineer  
**I need** a Tekton CD pipeline  
**So that** every merge can be built, tested, and deployed automatically

**Details and Assumptions**

- Tasks: cleanup, git-clone, flake8, pytest, buildah, deploy
- Pipeline: `cd-pipeline`
- Workspace backed by `pipelinerun-pvc`

**Acceptance Criteria**

```gherkin
Given the CD pipeline has been created
When I trigger the pipeline run
Then I should see the accounts service deployed to OpenShift
```

| Label | Estimate | Sprint |
| ----- | -------- | ------ |
| technical debt | 8 | Sprint 3 |
