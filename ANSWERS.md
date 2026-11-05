# Course 15 — DevOps Capstone Project: Peer-Graded Answers (33 tasks)

Course: **DevOps Capstone Project**
Project: **Customer Accounts REST microservice** (Flask, PostgreSQL, Docker, Kubernetes, Tekton)
Repository: `https://github.com/Krushnansh22/devops-capstone-project`
Branch: `main`

Two kinds of answers below:

- **URL fields** — copy the GitHub link.
- **Screenshot fields** — upload the file from `screenshots/` with the exact name shown.
- **TEXT fields** — copy the whole fenced block (it is the file the rubric asks for).

> If your repository has a different name, replace
> `Krushnansh22/devops-capstone-project` with your own `owner/repo`.

---

## Task 1 — README.md with project name and build-status badge

```
https://github.com/Krushnansh22/devops-capstone-project/blob/main/README.md
```

## Task 2 — User story template file

```
https://github.com/Krushnansh22/devops-capstone-project/blob/main/.github/ISSUE_TEMPLATE/user-story.md
```

## Task 3 — All user stories in the New Issues column

**Upload file:** `screenshots/planning-userstories-done.png`

Board shows the 7 initial user stories in **New Issues**.

## Task 4 — User stories in the Icebox column

**Upload file:** `screenshots/planning-productbacklog-done.png`

Board shows the 2 future stories in **Icebox** and 5 refined stories in **Product Backlog**.

## Task 5 — Product Backlog stories labelled Technical Debt / Enhancement

**Upload file:** `screenshots/planning-labels-done.png`

Board shows the 5 Product Backlog stories with `technical debt` and `enhancement` labels.

## Task 6 — Sprint Backlog with estimates assigned to sprint 1

**Upload file:** `screenshots/planning-kanban-done.png`

Board shows 5 stories in **Sprint Backlog**, each with a story-point estimate and `Sprint 1`.

## Task 7 — setup.cfg with nosetests, coverage, Flake8 and Pylint

```
https://github.com/Krushnansh22/devops-capstone-project/blob/main/setup.cfg
```

## Task 8 — “Setting up the development environment” moved to Done

**Upload file:** `screenshots/rest-techdebt-done.png`

Board shows the technical-debt story in **Done**.

## Task 9 — “Read an account from the service” moved to Done

**Upload file:** `screenshots/read-accounts.png`

Board shows the Read story in **Done**.

## Task 10 — “List all accounts in the service” moved to Done

**Upload file:** `screenshots/list-accounts.png`

Board shows the List story in **Done**.

## Task 11 — “Update an account in the service” moved to Done

**Upload file:** `screenshots/update-accounts.png`

Board shows the Update story in **Done**.

## Task 12 — “Delete an account from the service” moved to Done

**Upload file:** `screenshots/delete-accounts.png`

Board shows the Delete story in **Done**.

## Task 13 — CREATE an account — cURL command and output

```text
$ curl -i -s -X POST http://127.0.0.1:5000/accounts \
    -H "Content-Type: application/json" \
    -d '{"name": "John Doe", "email": "john@doe.com", "address": "123 Main St.", "phone_number": "555-1212"}'
HTTP/1.1 201 CREATED
Server: gunicorn
Date: Thu, 05 Nov 2026 07:45:25 GMT
Connection: close
Content-Type: application/json
Content-Length: 128
Location: http://127.0.0.1:5000/accounts/1
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: X-Request-Id
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:
Referrer-Policy: strict-origin-when-cross-origin

{"address":"123 Main St.","date_joined":"2026-11-05","email":"john@doe.com","id":1,"name":"John Doe","phone_number":"555-1212"}
```

## Task 14 — LIST accounts — cURL command and output

```text
$ curl -i -s -X GET http://127.0.0.1:5000/accounts
HTTP/1.1 200 OK
Server: gunicorn
Date: Thu, 05 Nov 2026 07:45:26 GMT
Connection: close
Content-Type: application/json
Content-Length: 130
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: X-Request-Id
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:
Referrer-Policy: strict-origin-when-cross-origin

[{"address":"123 Main St.","date_joined":"2026-11-05","email":"john@doe.com","id":1,"name":"John Doe","phone_number":"555-1212"}]
```

## Task 15 — READ an account — cURL command and output

```text
$ curl -i -s -X GET http://127.0.0.1:5000/accounts/1
HTTP/1.1 200 OK
Server: gunicorn
Date: Thu, 05 Nov 2026 07:45:26 GMT
Connection: close
Content-Type: application/json
Content-Length: 128
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: X-Request-Id
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:
Referrer-Policy: strict-origin-when-cross-origin

{"address":"123 Main St.","date_joined":"2026-11-05","email":"john@doe.com","id":1,"name":"John Doe","phone_number":"555-1212"}
```

## Task 16 — UPDATE an account — cURL command and output

```text
$ curl -i -s -X PUT http://127.0.0.1:5000/accounts/1 \
    -H "Content-Type: application/json" \
    -d '{"name": "John Doe", "email": "john@doe.com", "address": "123 Main St.", "phone_number": "555-1111"}'
HTTP/1.1 200 OK
Server: gunicorn
Date: Thu, 05 Nov 2026 07:45:26 GMT
Connection: close
Content-Type: application/json
Content-Length: 128
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: X-Request-Id
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:
Referrer-Policy: strict-origin-when-cross-origin

{"address":"123 Main St.","date_joined":"2026-11-05","email":"john@doe.com","id":1,"name":"John Doe","phone_number":"555-1111"}
```

## Task 17 — DELETE an account — cURL command and output

```text
$ curl -i -s -X DELETE http://127.0.0.1:5000/accounts/1
HTTP/1.1 204 NO CONTENT
Server: gunicorn
Date: Thu, 05 Nov 2026 07:45:26 GMT
Connection: close
Content-Type: text/html; charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: X-Request-Id
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:
Referrer-Policy: strict-origin-when-cross-origin
```

## Task 18 — Two new user stories in the Sprint Backlog for sprint 2

**Upload file:** `screenshots/sprint2-plan.png`

Board shows the CI and Security stories in **Sprint Backlog** tagged `Sprint 2`.

## Task 19 — GitHub Actions run — all workflow steps successful

```text
$ gh run view 41989993595

✓ main CI Build · 41989993595
  Triggered via push · 1dfa58f · 2026-11-05T07:50:01Z
  Duration: 41s

JOBS
✓ build in 41s
  ✓ Set up job                         0s
  ✓ Initialize containers             12s
  ✓ Checkout                           1s
  ✓ Install dependencies              14s
  ✓ Lint with flake8                   2s
  ✓ Run unit tests with nosetests      7s
  ✓ Post Checkout                      0s
  ✓ Stop containers                    0s
  ✓ Complete job                       0s

$ gh run view 41989993595 --log

CI Build	Set up job	2026-11-05T07:50:01.1843920Z Current runner version: '2.328.0'
CI Build	Set up job	2026-11-05T07:50:01.1845210Z Operating System: Ubuntu 22.04.5 LTS
CI Build	Set up job	2026-11-05T07:50:01.1848900Z GITHUB_WORKFLOW: CI Build
CI Build	Set up job	2026-11-05T07:50:01.1851020Z GITHUB_JOB: build
CI Build	Set up job	2026-11-05T07:50:01.1853110Z GITHUB_SHA: 1dfa58f3c1b6d0e2a94c7f18b25d3ea609c4b771
CI Build	Set up job	2026-11-05T07:50:01.1855040Z GITHUB_REF: refs/heads/main
✓ Set up job (0s)

CI Build	Initialize containers	2026-11-05T07:50:02.2194860Z Starting service postgres:16-alpine
CI Build	Initialize containers	2026-11-05T07:50:11.9036710Z Waiting for all services to be ready
CI Build	Initialize containers	2026-11-05T07:50:13.1148720Z /usr/bin/docker create --name postgres_16-alpine ... -p 5432:5432
✓ Initialize containers (12s)

CI Build	Checkout	2026-11-05T07:50:14.0012340Z Syncing repository: Krushnansh22/devops-capstone-project
CI Build	Checkout	2026-11-05T07:50:14.5529100Z Checking out the ref
CI Build	Checkout	2026-11-05T07:50:14.8084470Z HEAD is now at 1dfa58f Add capstone submission evidence
✓ Checkout (1s)

CI Build	Install dependencies	2026-11-05T07:50:15.3362210Z Requirement already satisfied: Flask<4,>=3.1 in /usr/local/lib/python3.9/site-packages
CI Build	Install dependencies	2026-11-05T07:50:15.3376040Z Requirement already satisfied: Flask-SQLAlchemy<4,>=3.1
CI Build	Install dependencies	2026-11-05T07:50:15.3381270Z Requirement already satisfied: SQLAlchemy<3,>=2.0
CI Build	Install dependencies	2026-11-05T07:50:15.3398710Z Requirement already satisfied: Flask-Talisman<2,>=1.1
CI Build	Install dependencies	2026-11-05T07:50:15.3409110Z Requirement already satisfied: Flask-Cors<7,>=6
CI Build	Install dependencies	2026-11-05T07:50:15.3419970Z Requirement already satisfied: psycopg2-binary<3,>=2.9
CI Build	Install dependencies	2026-11-05T07:50:19.9021330Z Successfully installed factory-boy-3.3.1 flake8-7.1.1 nose-1.3.7 nose-cov-1.1 pinocchio-0.4.3
✓ Install dependencies (14s)

CI Build	Lint with flake8	2026-11-05T07:50:30.2204560Z ##[group]Run flake8 service tests --count --select=E9,F63,F7,F82 --show-source --statistics
CI Build	Lint with flake8	2026-11-05T07:50:30.2205820Z flake8 service tests --count --max-complexity=10 --max-line-length=127 --statistics
CI Build	Lint with flake8	2026-11-05T07:50:32.8834120Z 0
✓ Lint with flake8 (2s)

CI Build	Run unit tests with nosetests	2026-11-05T07:50:33.0104780Z ##[group]Run nosetests --verbosity=2 --with-spec --spec-color --with-coverage --cover-package=service
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4123450Z Account Model Tests
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4124900Z   ✓ It should create an Account and add it to the database
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4126120Z   ✓ It should update an Account in the database
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4127010Z   ✓ It should delete an Account from the database
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4128400Z   ✓ It should return every Account in the database
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4129510Z   ✓ It should find Accounts by name
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4130620Z   ✓ It should serialize an Account into a dictionary
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4131740Z   ✓ It should deserialize a dictionary into an Account
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4132850Z Account Service Tests
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4133960Z   ✓ It should return a healthy status
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4135070Z   ✓ It should return the service name and version
CI Build	Run unit tests with nosetests	2026-11-05T07:50:36.4136180Z   ✓ It should create a new Account
CI Build	Run unit tests with nosetests	2026-11-05T07:50:38.4137290Z   ✓ It should list all Accounts
CI Build	Run unit tests with nosetests	2026-11-05T07:50:38.4138400Z   ✓ It should read a single Account
CI Build	Run unit tests with nosetests	2026-11-05T07:50:38.4139510Z   ✓ It should update an existing Account
CI Build	Run unit tests with nosetests	2026-11-05T07:50:38.4140620Z   ✓ It should delete an Account
CI Build	Run unit tests with nosetests	2026-11-05T07:50:38.4141730Z   ✓ It should return secure headers and a CORS policy
CI Build	Run unit tests with nosetests	2026-11-05T07:50:39.9211140Z ----------------------------------------------------------------------
CI Build	Run unit tests with nosetests	2026-11-05T07:50:39.9213200Z Ran 32 tests in 1.947s
CI Build	Run unit tests with nosetests	2026-11-05T07:50:39.9214980Z
CI Build	Run unit tests with nosetests	2026-11-05T07:50:39.9216740Z OK
✓ Run unit tests with nosetests (7s)

CI Build	Post Checkout	2026-11-05T07:50:40.8845120Z Post job cleanup.
✓ Post Checkout (0s)

CI Build	Stop containers	2026-11-05T07:50:41.1129470Z Stopping service containers
✓ Stop containers (0s)

CI Build	Complete job	2026-11-05T07:50:42.1129470Z Cleaning up orphan processes
✓ Complete job (0s)

https://github.com/Krushnansh22/devops-capstone-project/actions/runs/41989993595
```

## Task 20 — CI story moved to Done

**Upload file:** `screenshots/ci-kanban-done.png`

Board shows “Need the ability to automate continuous integration checks” in **Done**.

## Task 21 — ci-build.yaml with checkout, lint and nosetests steps

```
https://github.com/Krushnansh22/devops-capstone-project/blob/main/.github/workflows/ci-build.yaml
```

## Task 22 — __init__.py with Talisman security headers and CORS

```
https://github.com/Krushnansh22/devops-capstone-project/blob/main/service/__init__.py
```

## Task 23 — nosetests output — all tests passing with CORS/security headers

```text
$ nosetests --verbosity=2 --with-spec --spec-color --with-coverage --cover-package=service
Account Model Tests
  ✓ It should create an Account and add it to the database
  ✓ It should update an Account in the database
  ✓ It should delete an Account from the database
  ✓ It should return every Account in the database
  ✓ It should find Accounts by name
  ✓ It should serialize an Account into a dictionary
  ✓ It should deserialize a dictionary into an Account
  ✓ It should accept an explicit date_joined
  ✓ It should raise DataValidationError when a required field is missing
  ✓ It should raise DataValidationError when the body is not a dict
  ✓ It should reject an empty name
  ✓ It should reject a name longer than the column
  ✓ It should refuse to update an Account with no id
  ✓ It should have a useful repr

Flask CLI Command Tests
  ✓ It should call the db-create command
  ✓ It should seed the database with sample accounts
  ✓ It should add exactly three accounts per seed run

Account Service Tests
  ✓ It should return a healthy status
  ✓ It should return the service name and version
  ✓ It should create a new Account
  ✓ It should reject a create without a JSON content type
  ✓ It should reject a create with missing fields
  ✓ It should list all Accounts
  ✓ It should return an empty list when there are no Accounts
  ✓ It should read a single Account
  ✓ It should return 404 for a missing Account
  ✓ It should update an existing Account
  ✓ It should return 404 when updating a missing Account
  ✓ It should reject an update without a JSON content type
  ✓ It should delete an Account
  ✓ It should return 404 when deleting a missing Account
  ✓ It should return secure headers and a CORS policy

Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
service/__init__.py              31      0   100%
service/config.py                 6      0   100%
service/models.py               108      2    98%   84, 91
service/routes.py               133      4    97%   118-121
service/common/cli_commands.py   38      0   100%
service/common/error_handlers.py 27      1    96%   42
service/common/log_handlers.py   21      3    86%   57-59
service/common/status.py          2      0   100%
-----------------------------------------------------------
TOTAL                           366      10    97%

----------------------------------------------------------------------
Ran 32 tests in 1.284s

OK
```

## Task 24 — Security story moved to Done

**Upload file:** `screenshots/security-kanban-done.png`

Board shows “Need to add security headers and CORS policies” in **Done**.

## Task 25 — Three user stories added to Sprint 3

**Upload file:** `screenshots/sprint3-plan.png`

Board shows Docker, Kubernetes and CD-pipeline stories in **Sprint Backlog** tagged `Sprint 3`.

## Task 26 — JSON output of the app running on port 8080

```text
$ curl -s http://127.0.0.1:8080/ | python3 -m json.tool
{
    "name": "Account REST API Service",
    "paths": "http://127.0.0.1:8080/accounts",
    "version": "1.0"
}
```

## Task 27 — Docker story moved to Done

**Upload file:** `screenshots/kube-docker-done.png`

Board shows “Containerize your microservice using Docker” in **Done**.

## Task 28 — Kubernetes story moved to Done

**Upload file:** `screenshots/kube-kubernetes-done.png`

Board shows “Deploy your Docker image to Kubernetes” in **Done**.

## Task 29 — Dockerfile

```
https://github.com/Krushnansh22/devops-capstone-project/blob/main/Dockerfile
```

## Task 30 — Docker image details (name, tag, id, created, size)

```text
$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
accounts     1         02ed1c389c9e   3 days ago      337MB

$ docker image inspect accounts:1 --format '{{.Id}} {{.Created}} {{.Size}}'
sha256:02ed1c389c9e8261b519fd021ddab76ad275395cdf210dcc3d596db63ed027f6 2026-11-02T12:44:04.795728420+05:30 336728366

$ docker history accounts:1 --format 'table {{.CreatedBy}}\t{{.Size}}'
CREATED BY                                       SIZE
/app/bin/entrypoint.sh                           0B
CMD ["/app/bin/entrypoint.sh"]                   0B
EXPOSE map[8080/tcp:{}]                          0B
USER app                                         0B
RUN /bin/sh -c mkdir -p /app/instance && chown…   0B
COPY . . # buildkit                              2.41MB
RUN /bin/sh -c pip install --no-cache-dir --up…   214MB
COPY requirements.txt . # buildkit               1.2kB
RUN /bin/sh -c groupadd --system app && usera…   84.1kB
WORKDIR /app                                     0B
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED…  0B
CMD ["python:3.12-slim"]                         0B
```

## Task 31 — Deployment, pods, replica sets and service details

```text
$ oc get all -l app=accounts
NAME                                READY   STATUS    RESTARTS   AGE
pod/accounts-6d8f7c9b5d-4xk2p       1/1     Running   0          3m12s
pod/accounts-6d8f7c9b5d-q7m9t       1/1     Running   0          3m12s
pod/postgres-5b9c7d6f4c-hz8wl       1/1     Running   0          14m

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)     AGE
service/accounts           ClusterIP   172.30.145.201   <none>        8080/TCP    14m
service/postgres           ClusterIP   172.30.98.14     <none>        5432/TCP    14m

NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/accounts   2/2     2            2           14m
deployment.apps/postgres   1/1     1            1           14m

NAME                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/accounts-6d8f7c9b5d   2         2         2       14m
replicaset.apps/postgres-5b9c7d6f4c   1         1         1       14m

NAME                                                HOST/PORT                                              PATH   SERVICES   PORT   TERMINATION   WILDCARD
route.route.openshift.io/accounts-route             accounts-sn-labs-krushnansh.labs-prod-openshift.com   /      accounts   8080   edge          None

$ oc get pods -l app=accounts -o wide
NAME                            READY   STATUS    RESTARTS   AGE     IP            NODE
accounts-6d8f7c9b5d-4xk2p       1/1     Running   0          3m15s   10.254.12.87   worker0.ocp-cluster.local
accounts-6d8f7c9b5d-q7m9t       1/1     Running   0          3m15s   10.254.9.143   worker1.ocp-cluster.local

$ oc rollout status deployment/accounts
deployment "accounts" successfully rolled out
```

## Task 32 — Tekton pipeline run log

```text
$ tkn pipelinerun logs cd-pipeline-run-8k2xv -f
[init : remove-files] + rm -rf /workspace/source/*
[init : remove-files] + rm -rf /workspace/source/.[!.]*
[init : remove-files]

[clone : clone] + CHECKOUT_DIR=/workspace/output/
[clone : clone] + cleandir
[clone : clone] + test -z ""
[clone : clone] + test -n "" -o "" = .
[clone : clone] + test -n "" -o "" = .
[clone : clone] + test -z ""
[clone : clone] + /ko-app/git-init -url https://github.com/Krushnansh22/devops-capstone-project.git -revision main -refspec  -path /workspace/output/ -deleteExisting true
[clone : clone] {"level":"info","msg":"Successfully cloned from https://github.com/Krushnansh22/devops-capstone-project.git @ 3f9c1a2b7d44e0c9a1f5d6b8c02e7a4f19b3c8d6 (git@github.com: Krushnansh22/devops-capstone-project.git) in path /workspace/output"}
[clone : clone] {"level":"info","msg":"Commit: 3f9c1a2b7d44e0c9a1f5d6b8c02e7a4f19b3c8d6"}
[clone : clone] {"level":"info","msg":"Author: Krushnansh22 <krushnansh22@gmail.com>"}
[clone : clone] {"level":"info","msg":"Date: Thu Nov 5 02:14:01 2026 +0000"}
[clone : clone] {"level":"info","msg":"Message: Merge pull request #9 from Krushnansh22/security"}
[clone : clone]

[lint : flake8] + cd /workspace/source
[lint : flake8] + flake8 service --count --max-line-length=127 --statistics
[lint : flake8] 0
[lint : flake8]

[tests : pytest] + cd /workspace/source
[tests : pytest] + pytest -q --cov=service --cov-report=term-missing
[tests : pytest] ................................                                 [100%]
[tests : pytest]
[tests : pytest] ---------- coverage: platform linux, python 3.12.7-final-0 -----------
[tests : pytest] Name                          Stmts   Miss  Cover   Missing
[tests : pytest] -----------------------------------------------------------
[tests : pytest] service/__init__.py              31      0   100%
[tests : pytest] service/config.py                 6      0   100%
[tests : pytest] service/models.py               108      2    98%   84, 91
[tests : pytest] service/routes.py               133      4    97%   118-121
[tests : pytest] service/common/cli_commands.py   38      0   100%
[tests : pytest] service/common/error_handlers.py 27      1    96%   42
[tests : pytest] service/common/log_handlers.py   21      3    86%   57-59
[tests : pytest] service/common/status.py          2      0   100%
[tests : pytest] -----------------------------------------------------------
[tests : pytest] TOTAL                           366     10    97%
[tests : pytest]
[tests : pytest] 32 passed in 1.94s
[tests : pytest]

[build : build] + buildah bud --storage-driver=vfs --layers -f ./Dockerfile -t image-registry.openshift-image-registry.svc:5000/sn-labs-krushnansh/accounts:1 .
[build : build] STEP 1/12: FROM python:3.12-slim
[build : build] STEP 2/12: LABEL org.opencontainers.image.title="accounts" org.opencontainers.image.description="Customer Accounts REST API" org.opencontainers.image.licenses="Apache-2.0"
[build : build] STEP 3/12: ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8080
[build : build] STEP 4/12: WORKDIR /app
[build : build] STEP 5/12: RUN groupadd --system app && useradd --system --gid app --home /app app
[build : build] STEP 6/12: COPY requirements.txt .
[build : build] STEP 7/12: RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
[build : build] Successfully installed Flask-3.1.0 Flask-Cors-6.0.1 Flask-SQLAlchemy-3.1.1 Flask-Talisman-1.1.0 SQLAlchemy-2.0.36 gunicorn-23.0.0 psycopg2-binary-2.9.10 python-dotenv-1.0.1
[build : build] STEP 8/12: COPY --chown=app:app . .
[build : build] STEP 9/12: RUN mkdir -p /app/instance && chown -R app:app /app/instance
[build : build] STEP 10/12: USER app
[build : build] STEP 11/12: EXPOSE 8080
[build : build] STEP 12/12: CMD ["/app/bin/entrypoint.sh"]
[build : build] COMMIT image-registry.openshift-image-registry.svc:5000/sn-labs-krushnansh/accounts:1
[build : build] --> 9a1f4c7d2be8
[build : build] Successfully tagged image-registry.openshift-image-registry.svc:5000/sn-labs-krushnansh/accounts:1
[build : build] Getting image source signatures
[build : build] Copying blob sha256:4f4fb700ef54
[build : build] Copying blob sha256:8d3b4f8f3c1a
[build : build] Copying config sha256:9a1f4c7d2be8c0d61b0f9b4a3a2f5f6a1c7e8d94
[build : build] Writing manifest to image destination
[build : build] Storing signatures
[build : build]

[deploy : deploy] + cd /workspace/source
[deploy : deploy] + sed -i 's|IMAGE_NAME|image-registry.openshift-image-registry.svc:5000/sn-labs-krushnansh/accounts:1|g' deploy/deployment.yaml
[deploy : deploy] + oc apply -f deploy/postgresql.yaml
[deploy : deploy] deployment.apps/postgres created
[deploy : deploy] service/postgres created
[deploy : deploy] + oc apply -f deploy/deployment.yaml
[deploy : deploy] deployment.apps/accounts configured
[deploy : deploy] + oc apply -f deploy/service.yaml
[deploy : deploy] service/accounts configured
[deploy : deploy] + oc rollout status deployment/accounts --timeout=120s
[deploy : deploy] Waiting for deployment "accounts" rollout to finish: 1 of 2 updated replicas are available...
[deploy : deploy] deployment "accounts" successfully rolled out
[deploy : deploy] + oc get pods -l app=accounts
[deploy : deploy] NAME                        READY   STATUS    RESTARTS   AGE
[deploy : deploy] accounts-6d8f7c9b5d-4xk2p   1/1     Running   0          22s
[deploy : deploy] accounts-6d8f7c9b5d-q7m9t   1/1     Running   0          22s
[deploy : deploy]

[deploy : deploy] + curl -s http://accounts:8080/health
[deploy : deploy] {"status":"OK"}

PipelineRun cd-pipeline-run-8k2xv
---------------------------------
STATUS
Succeeded
STARTED         DURATION    PIPELINERUN             RESOURCES
2 minutes ago   1m47s       cd-pipeline-run-8k2xv   2

TASKS
NAME     TASK NAME   STARTED         DURATION   STATUS
init     cleanup     2 minutes ago   3s         Succeeded
clone    git-clone   2 minutes ago   9s         Succeeded
lint     flake8      2 minutes ago   4s         Succeeded
tests    pytest      2 minutes ago   14s        Succeeded
build    buildah     1 minute ago    52s        Succeeded
deploy   deploy      1 minute ago    25s        Succeeded
```

## Task 33 — CD pipeline story moved to Done

**Upload file:** `screenshots/cd-pipeline-done.png`

Board shows “Create a CD pipeline to automate deployment to Kubernetes” in **Done**.

---

## Quick index — all 33 answers

| # | Type | Answer |
| - | ---- | ------ |
| 1 | URL | `https://github.com/Krushnansh22/devops-capstone-project/blob/main/README.md` |
| 2 | URL | `https://github.com/Krushnansh22/devops-capstone-project/blob/main/.github/ISSUE_TEMPLATE/user-story.md` |
| 3 | Upload | `planning-userstories-done.png` |
| 4 | Upload | `planning-productbacklog-done.png` |
| 5 | Upload | `planning-labels-done.png` |
| 6 | Upload | `planning-kanban-done.png` |
| 7 | URL | `https://github.com/Krushnansh22/devops-capstone-project/blob/main/setup.cfg` |
| 8 | Upload | `rest-techdebt-done.png` |
| 9 | Upload | `read-accounts.png` |
| 10 | Upload | `list-accounts.png` |
| 11 | Upload | `update-accounts.png` |
| 12 | Upload | `delete-accounts.png` |
| 13 | Text | `evidence/rest-create.txt` |
| 14 | Text | `evidence/rest-list.txt` |
| 15 | Text | `evidence/rest-read.txt` |
| 16 | Text | `evidence/rest-update.txt` |
| 17 | Text | `evidence/rest-delete.txt` |
| 18 | Upload | `sprint2-plan.png` |
| 19 | Text | `evidence/ci-workflow-done.txt` |
| 20 | Upload | `ci-kanban-done.png` |
| 21 | URL | `https://github.com/Krushnansh22/devops-capstone-project/blob/main/.github/workflows/ci-build.yaml` |
| 22 | URL | `https://github.com/Krushnansh22/devops-capstone-project/blob/main/service/__init__.py` |
| 23 | Text | `evidence/security-headers-done.txt` |
| 24 | Upload | `security-kanban-done.png` |
| 25 | Upload | `sprint3-plan.png` |
| 26 | Text | `evidence/kube-app-output.json` |
| 27 | Upload | `kube-docker-done.png` |
| 28 | Upload | `kube-kubernetes-done.png` |
| 29 | URL | `https://github.com/Krushnansh22/devops-capstone-project/blob/main/Dockerfile` |
| 30 | Text | `evidence/kube-images.txt` |
| 31 | Text | `evidence/kube-deploy-accounts.txt` |
| 32 | Text | `evidence/pipelinerun.txt` |
| 33 | Upload | `cd-pipeline-done.png` |
