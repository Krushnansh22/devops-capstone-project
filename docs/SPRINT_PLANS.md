# Sprint Plans

## Sprint 0 — Agile planning (60 min)

Goal: create the repository, the user story template, and the product backlog.

- Create `devops-capstone-project` from the IBM template (public).
- Create `.github/ISSUE_TEMPLATE/story_template.md`.
- Create 9 user stories.
- Move 5 CRUD stories to the Product Backlog and 2 container stories to the Icebox.
- Add `enhancement` and `technical debt` labels.
- Rank the backlog.
- Create three one-week sprints.

Evidence: `planning-repository-done`, `planning-storytemplate-done`,
`planning-userstories-done`, `planning-productbacklog-done`,
`planning-labels-done`, `planning-kanban-done`.

---

## Sprint 1 — Account CRUD with TDD (1 week)

Goal: implement read, update, delete, and list with tests written first.

| Story | Points |
| ----- | ------ |
| Set up the development environment | 3 |
| Read an account | 3 |
| Update an account | 5 |
| Delete an account | 3 |
| List all accounts | 3 |

Definition of done:

- Unit tests written before the route
- `pytest` green
- `flake8` clean
- Pull request merged
- Story moved to Done, then Closed

Evidence: `rest-setupcfg-done`, `rest-techdebt-done`, `list-accounts`,
`read-accounts`, `update-accounts`, `delete-accounts`, `rest-create-done`,
`rest-list-done`, `rest-read-done`, `rest-update-done`, `rest-delete-done`.

---

## Sprint 2 — CI and security (1 week)

| Story | Points |
| ----- | ------ |
| Add continuous integration with GitHub Actions | 5 |
| Secure the RESTful service | 5 |

Definition of done:

- `.github/workflows/ci-build.yaml` runs lint and tests on every push and PR
- Build status badge in `README.md`
- Flask-Talisman secure headers and Flask-CORS policy enabled
- `curl -I` shows `X-Content-Type-Options`, `X-Frame-Options`,
  `Content-Security-Policy`, and `Access-Control-Allow-Origin`

Evidence: `sprint2-plan`, `ci-workflow-done`, `ci-badge-done`,
`ci-kanban-done`, `security-code-done`, `security-headers-done`,
`security-kanban-done`.

---

## Sprint 3 — Docker, Kubernetes, CD (1 week)

| Story | Points |
| ----- | ------ |
| Containerize the microservice using Docker | 5 |
| Deploy the Docker image to Kubernetes | 8 |
| Build an automated CD pipeline | 8 |

Definition of done:

- `Dockerfile` builds and runs as a non-root user
- Image pushed to the IBM Cloud Container Registry
- `deploy/` manifests applied and the route serves `/accounts`
- Tekton tasks, pipeline, PVC, and a successful pipeline run
- `tkn pipelinerun logs -L > pipelinerun.txt`

Evidence: `sprint3-plan`, `kube-app-output`, `kube-docker-done`,
`kube-kubernetes-done`, `kube-images`, `kube-deploy-accounts`,
`pipelinerun.txt`, `cd-pipeline-done`.

---

## Velocity summary

| Sprint | Points | Cumulative |
| ------ | ------ | ---------- |
| Sprint 1 | 17 | 17 |
| Sprint 2 | 10 | 27 |
| Sprint 3 | 21 | 48 |
