# Final Submission — Evidence Checklist

The capstone is graded on screenshots and URLs. Capture each item below and
keep the exact file name; the labs and the grader both refer to them by name.
Use `.jpg` or `.png`.

Legend:
- **local** — this folder can produce the content, but you must still take the
  screenshot in your own environment.
- **github** — take it on github.com.
- **zenhub** — take it on your ZenHub board.
- **cluster** — take it in the IBM Cloud IDE / OpenShift terminal.

---

## Module 1 — Agile planning

| # | File name | Where | What must be visible |
| - | --------- | ----- | -------------------- |
| 1 | `planning-repository-done.jpg` | github | The new public `devops-capstone-project` repository page |
| 2 | `planning-storytemplate-done.jpg` | github | `.github/ISSUE_TEMPLATE/story_template.md` contents |
| 3 | `planning-userstories-done.jpg` | zenhub | Board with 7 stories in **New Issues** |
| 4 | `planning-productbacklog-done.jpg` | zenhub | 5 stories in **Product Backlog**, 2 in **Icebox** |
| 5 | `planning-labels-done.jpg` | zenhub | `enhancement` and `technical debt` labels on stories |
| 6 | `planning-kanban-done.jpg` | zenhub | 5 stories in **Sprint Backlog** with estimates |

## Module 2 — RESTful service (TDD)

| # | File name | Where | What must be visible |
| - | --------- | ----- | -------------------- |
| 7 | `rest-setupcfg-done.jpg` | local/github | `setup.cfg` contents |
| 8 | `rest-techdebt-done.jpg` | zenhub | Environment story in **Done** |
| 9 | `list-accounts.jpg` | zenhub | List story in **Done** |
| 10 | `read-accounts.jpg` | zenhub | Read story in **Done** |
| 11 | `update-accounts.jpg` | zenhub | Update story in **Done** |
| 12 | `delete-accounts.jpg` | zenhub | Delete story in **Done** |
| 13 | `rest-create-done.jpg` | local | `curl -i -X POST .../accounts` returning `201 Created` |
| 14 | `rest-list-done.jpg` | local | `curl -i .../accounts` returning `200 OK` and a list |
| 15 | `rest-read-done.jpg` | local | `curl -i .../accounts/1` returning `200 OK` |
| 16 | `rest-update-done.jpg` | local | `curl -i -X PUT .../accounts/1` returning `200 OK` with the new phone number |
| 17 | `rest-delete-done.jpg` | local | `curl -i -X DELETE .../accounts/1` returning `204 No Content` |

## Module 3 — CI and security

| # | File name | Where | What must be visible |
| - | --------- | ----- | -------------------- |
| 18 | `sprint2-plan.jpg` | zenhub | Sprint 2 backlog with both stories |
| 19 | `ci-workflow-done.jpg` | github | A green GitHub Actions run with every step passed |
| 20 | `ci-badge-done.jpg` | github | `README.md` showing the build status badge |
| 21 | `ci-kanban-done.jpg` | zenhub | CI story in **Done** |
| 22 | `security-code-done.jpg` | github | `service/__init__.py` with Talisman and CORS |
| 23 | `security-headers-done.jpg` | local | `curl -I` output showing secure headers and CORS |
| 24 | `security-kanban-done.jpg` | zenhub | Security story in **Done** |

## Module 4 — Kubernetes

| # | File name | Where | What must be visible |
| - | --------- | ----- | -------------------- |
| 25 | `sprint3-plan.jpg` | zenhub | Sprint 3 backlog with three stories |
| 26 | `kube-app-output.jpg` | cluster | The app page served through the OpenShift route |
| 27 | `kube-docker-done.jpg` | zenhub | Docker story in **Done** |
| 28 | `kube-kubernetes-done.jpg` | zenhub | Kubernetes story in **Done** |
| 29 | `kube-images.jpg` | cluster | `docker image ls` showing the `accounts` image |
| 30 | `kube-deploy-accounts.jpg` | cluster | `oc get all -l app=accounts` showing the running deployment |
| — | Dockerfile URL | github | `https://github.com/<user>/devops-capstone-project/blob/main/Dockerfile` |

## Module 5 — CD pipeline

| # | File name | Where | What must be visible |
| - | --------- | ----- | -------------------- |
| 31 | `pipelinerun.txt` | cluster | `tkn pipelinerun logs -L` output for a successful run |
| 32 | `cd-pipeline-done.jpg` | zenhub | CD story in **Done** |

---

## Repository URLs to submit

Replace `<user>` with your GitHub username.

| Item | URL |
| ---- | --- |
| Repository | `https://github.com/<user>/devops-capstone-project` |
| README | `https://github.com/<user>/devops-capstone-project/blob/main/README.md` |
| Dockerfile | `https://github.com/<user>/devops-capstone-project/blob/main/Dockerfile` |
| CI workflow | `https://github.com/<user>/devops-capstone-project/blob/main/.github/workflows/ci-build.yaml` |
| Service code | `https://github.com/<user>/devops-capstone-project/blob/main/service/routes.py` |
| Tests | `https://github.com/<user>/devops-capstone-project/blob/main/tests/test_routes.py` |
| Kubernetes manifests | `https://github.com/<user>/devops-capstone-project/tree/main/deploy` |
| Tekton pipeline | `https://github.com/<user>/devops-capstone-project/tree/main/tekton` |
| Actions runs | `https://github.com/<user>/devops-capstone-project/actions` |
