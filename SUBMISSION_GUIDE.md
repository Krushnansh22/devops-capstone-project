# Course 15 — DevOps Capstone Project Submission Guide

**Course:** DevOps Capstone Project (IBM DevOps and Software Engineering
Professional Certificate, course 15)
**Final module:** Final Submission and Evaluation
**Two submission routes:** *Option 1 — AI-Graded* (app item) or
*Option 2 — Peer-Graded* (one peer review, one required review)

Both routes use the same evidence: screenshots and repository URLs collected
during five hands-on labs plus two sprint-planning labs.

This folder is a complete, runnable capstone repository. It contains the
Customer Accounts microservice, 32 passing tests, the GitHub Actions workflow,
the security configuration, the Dockerfile, the Kubernetes/OpenShift manifests,
and the Tekton CD pipeline.

---

## 1. What is graded

The grader checks that you completed these labs and can show proof:

| Module | Lab | Evidence |
| ------ | --- | -------- |
| 1 | Agile Planning using GitHub/ZenHub | 6 planning screenshots + repository URL |
| 2 | Develop a RESTful Service using TDD | `setup.cfg`, kanban, 5 story screenshots, 5 `curl` screenshots |
| 3 | Add Continuous Integration | CI run screenshot, badge screenshot, kanban |
| 3 | Add Security to Your RESTful Service | `service/__init__.py`, `curl -I` headers, kanban |
| 4 | Deploy Your Application to Kubernetes | app output, Docker image list, `oc get all`, Dockerfile URL |
| 5 | Build an Automated CD Pipeline | `pipelinerun.txt`, kanban |

The complete file-by-file list is in `docs/EVIDENCE_CHECKLIST.md`.

---

## 2. What is already done in this folder

| Requirement | Where |
| ----------- | ----- |
| Agile user stories with acceptance criteria | `docs/user-stories.md` |
| Kanban board states for every sprint | `docs/kanban-board.md` |
| Sprint plans and velocity | `docs/SPRINT_PLANS.md` |
| Issue template | `.github/ISSUE_TEMPLATE/story_template.md` |
| Flask REST service with full CRUD | `service/` |
| 32 unit tests | `tests/` |
| CI workflow (flake8 + pytest + PostgreSQL) | `.github/workflows/ci-build.yaml` |
| Security headers + CORS | `service/__init__.py` |
| Container image | `Dockerfile` |
| Kubernetes/OpenShift manifests | `deploy/` |
| Tekton tasks, pipeline, PVC, pipelinerun | `tekton/` |
| Captured API and test output | `evidence/` |

Run the local validator at any time:

```bash
bash scripts/validate.sh
```

Expected: `95 passed, 0 failed`.

---

## 3. Prerequisites

- A GitHub account (`Krushnansh22`)
- SSH access to GitHub — `ssh -T git@github.com`
- A ZenHub account connected to GitHub (free for public repositories)
- Access to the IBM Cloud IDE with OpenShift for the Kubernetes and Tekton labs
- Docker for the container lab

---

## 4. Step 1 — Create the repository from the template

The lab requires **Use this template**, *not* a fork.

1. Open <https://github.com/ibm-developer-skills-network/aolwx-devops-capstone-template/generate>
2. Owner: `Krushnansh22`
3. Repository name: **`devops-capstone-project`** (the grader looks for this name)
4. Visibility: **Public**
5. Click **Create repository from template**

Screenshot: `planning-repository-done.jpg`.

---

## 5. Step 2 — Push this project

```bash
cd "DevOps Capstone Project"

# one-time identity check
git config user.name  "Krushnansh22"
git config user.email "krushnansh22@gmail.com"

bash scripts/publish.sh Krushnansh22
```

`publish.sh` adds `origin`, verifies the repository exists, and pushes `main`.
Because the repository was just created from the template, the first push
replaces the template commit:

```bash
git push -u --force origin main
```

If `GITHUB_TOKEN` is exported, the script can also create the repository through
the template-generate API.

Verify the Actions workflow starts:

<https://github.com/Krushnansh22/devops-capstone-project/actions>

---

## 6. Step 3 — Agile planning (Module 1)

Create these in ZenHub for the repository:

1. Workspace `capstone-project`, connected to the repository.
2. The `enhancement` and `technical debt` labels.
3. Nine issues from `docs/user-stories.md` using the story template.
4. Three one-week sprints: **Sprint 1**, **Sprint 2**, **Sprint 3**.

Then reproduce the board states in `docs/kanban-board.md` and take the six
screenshots:

| Screenshot | Board state to show |
| ---------- | ------------------- |
| `planning-repository-done.jpg` | Repository home page |
| `planning-storytemplate-done.jpg` | `story_template.md` |
| `planning-userstories-done.jpg` | 7 stories in **New Issues** |
| `planning-productbacklog-done.jpg` | 5 in **Product Backlog**, 2 in **Icebox** |
| `planning-labels-done.jpg` | Labels visible on the cards |
| `planning-kanban-done.jpg` | 5 stories in **Sprint Backlog** with estimates |

Checklist for "sprint ready": every story has a label, an estimate (3/5/8/13),
and a sprint assignment.

---

## 7. Step 4 — Sprint 1: REST service with TDD (Module 2)

### Run the tests

```bash
bash scripts/test.sh
```

Output is saved to `evidence/test-results.txt`:

```
................................
32 passed
```

### Confirm the TDD layout

- Tests: `tests/test_models.py`, `tests/test_routes.py`
- Code: `service/models.py`, `service/routes.py`
- Runner configuration: `setup.cfg`

Screenshot: `rest-setupcfg-done.jpg`.

### Demo every endpoint

```bash
bash scripts/demo-api.sh
```

This starts the service on port 5000, runs the five `curl` commands from the
lab, and writes:

- `evidence/rest-create.txt` → `201 CREATED`
- `evidence/rest-list.txt` → `200 OK` with a list
- `evidence/rest-read.txt` → `200 OK`
- `evidence/rest-update.txt` → `200 OK` with phone number `555-1111`
- `evidence/rest-delete.txt` → `204 NO CONTENT`

Take the five screenshots from those terminal sessions:

`rest-create-done`, `rest-list-done`, `rest-read-done`, `rest-update-done`,
`rest-delete-done`.

### Kanban evidence

Move each story to **Done** as you finish it and capture
`list-accounts.jpg`, `read-accounts.jpg`, `update-accounts.jpg`,
`delete-accounts.jpg`, plus `rest-techdebt-done.jpg` for the environment story.

At the end of the sprint, move all stories to **Closed**.

---

## 8. Step 5 — Sprint 2: CI and security (Module 3)

### Continuous integration

Push to `main` or open a pull request. The workflow
`.github/workflows/ci-build.yaml` runs:

1. checkout
2. install dependencies
3. `flake8`
4. `pytest` against a PostgreSQL service container

Open the green run and capture `ci-workflow-done.jpg`.

Open `README.md` and capture the badge as `ci-badge-done.jpg`.

Capture the CI story in **Done** as `ci-kanban-done.jpg`.

### Security

`service/__init__.py` enables Flask-Talisman and Flask-CORS. Verify the headers:

```bash
bash scripts/demo-api.sh
cat evidence/security-headers.txt
```

You should see:

```
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: default-src 'self'; ...
Access-Control-Allow-Origin: *
```

Capture:

- `security-code-done.jpg` — `service/__init__.py` on GitHub
- `security-headers-done.jpg` — the `curl -I` output
- `security-kanban-done.jpg` — the story in **Done**

---

## 9. Step 6 — Sprint 3: Docker and Kubernetes (Module 4)

### Build the image

```bash
bash scripts/build-image.sh
```

Expected output (also saved to `evidence/kube-images.txt`):

```
accounts   1   ...   ~150MB
```

Capture `kube-images.jpg` from `docker image ls`.

### Push to the IBM Cloud registry

In the lab environment:

```bash
docker tag accounts:1 us.icr.io/$SN_ICR_NAMESPACE/accounts:1
docker push us.icr.io/$SN_ICR_NAMESPACE/accounts:1
```

### Deploy

```bash
bash scripts/deploy-k8s.sh
```

or manually:

```bash
oc apply -f deploy/postgresql.yaml
oc apply -f deploy/deployment.yaml
oc apply -f deploy/service.yaml
oc apply -f deploy/route.yaml
oc get all -l app=accounts
```

Open the route in the internal browser and capture `kube-app-output.jpg`.

Capture `kube-deploy-accounts.jpg` from `oc get all -l app=accounts`.

Capture the two story screenshots: `kube-docker-done.jpg` and
`kube-kubernetes-done.jpg`.

Save the Dockerfile URL:

```
https://github.com/Krushnansh22/devops-capstone-project/blob/main/Dockerfile
```

---

## 10. Step 7 — CD pipeline (Module 5)

Install Tekton and the sample tasks in the cluster, then:

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

When the run succeeds, capture the graded evidence:

```bash
tkn pipelinerun logs -L > pipelinerun.txt
```

`evidence/pipelinerun.txt` in this folder is a placeholder describing exactly
what the real file must contain. Replace it with the output from your cluster.

Capture `cd-pipeline-done.jpg` from the board.

---

## 11. Step 8 — Final submission pack

Replace `<user>` with `Krushnansh22`.

### Repository URLs

```
https://github.com/<user>/devops-capstone-project
https://github.com/<user>/devops-capstone-project/blob/main/README.md
https://github.com/<user>/devops-capstone-project/blob/main/Dockerfile
https://github.com/<user>/devops-capstone-project/blob/main/.github/workflows/ci-build.yaml
https://github.com/<user>/devops-capstone-project/blob/main/service/routes.py
https://github.com/<user>/devops-capstone-project/blob/main/tests/test_routes.py
https://github.com/<user>/devops-capstone-project/tree/main/deploy
https://github.com/<user>/devops-capstone-project/tree/main/tekton
https://github.com/<user>/devops-capstone-project/actions
```

### Screenshot checklist

Upload these in the order the labs present them:

```
planning-repository-done
planning-storytemplate-done
planning-userstories-done
planning-productbacklog-done
planning-labels-done
planning-kanban-done
rest-setupcfg-done
rest-techdebt-done
list-accounts
read-accounts
update-accounts
delete-accounts
rest-create-done
rest-list-done
rest-read-done
rest-update-done
rest-delete-done
sprint2-plan
ci-workflow-done
ci-badge-done
ci-kanban-done
security-code-done
security-headers-done
security-kanban-done
sprint3-plan
kube-app-output
kube-docker-done
kube-kubernetes-done
kube-images
kube-deploy-accounts
cd-pipeline-done
pipelinerun.txt
```

### Answering the AI-graded prompts

- **Repository / file URL questions** — paste the matching URL above.
- **Screenshot questions** — upload the file with the exact name from the table.
- **Pipeline log question** — paste the contents of `pipelinerun.txt`.
- **Kanban questions** — upload the board screenshot that shows the requested
  column and story state.
- **Docker question** — provide the Dockerfile URL and the `kube-images`
  screenshot.

---

## 12. Local validation

```bash
bash scripts/validate.sh
```

The validator checks 95 items: repository layout, every REST endpoint, the
model methods, Talisman and CORS, the CI workflow, the Dockerfile, the
Kubernetes probes and resources, the Tekton tasks and pipeline, the docs, the
seven evidence files, YAML syntax, flake8, and all 32 unit tests.

---

## 13. Troubleshooting

**`publish.sh` says the repository was not found**
Create it from the template URL in Step 1 with the exact name
`devops-capstone-project` and choose Public.

**`git push` is rejected as non-fast-forward**
The template repo already has a commit. Use `git push -u --force origin main`
(the repository was just created and contains nothing of value).

**GitHub Actions fails on the PostgreSQL service**
Check that `DATABASE_URI` in the workflow points at host `postgres` and database
`testdb`, and that the service health check is `pg_isready`.

**`oc apply` cannot find `route.yaml` on plain Kubernetes**
Routes are OpenShift-only. Skip the route on vanilla Kubernetes and use a
`NodePort`/`LoadBalancer` service instead.

**Tekton pod fails with `permission denied` on the workspace**
The PVC storage class must support `ReadWriteMany`. In the IBM lab use
`skills-network-learner`; otherwise switch to `ReadWriteOnce` and a single task
at a time.

**`tkn: command not found`**
Install the Tekton CLI in the lab environment, or run
`kubectl logs -l tekton.dev/pipelineRun=<run-name>` instead.

**The lab environment expired**
The IBM Cloud IDE is ephemeral. Your code and evidence are in GitHub; recreate
the cluster and re-run `scripts/deploy-k8s.sh` and the pipeline.
