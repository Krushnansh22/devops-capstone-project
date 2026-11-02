# Kanban Board — capstone-project

This is a text rendering of the ZenHub/GitHub Projects board used for the
capstone. It mirrors the board states required by the labs and can be
reproduced in ZenHub in a few minutes.

Board columns: **New Issues → Icebox → Product Backlog → Sprint Backlog →
In Progress → Done → Closed**

---

## Sprint 0 — Product backlog refinement

| New Issues | Icebox | Product Backlog |
| ---------- | ------ | --------------- |
| — | Containerize the microservice using Docker (8) | Set up the development environment (3) — `technical debt` |
| — | Deploy the Docker image to Kubernetes (8) | Read an account (3) — `enhancement` |
| — | — | Update an account (5) — `enhancement` |
| — | — | Delete an account (3) — `enhancement` |
| — | — | List all accounts (3) — `enhancement` |

Ranking (top = highest priority):

1. Set up the development environment
2. Read an account
3. Update an account
4. Delete an account
5. List all accounts

Labels: `enhancement` (customer value) and `technical debt` (yellow).

---

## Sprint 1 — Account CRUD

Sprint length: 1 week

| Sprint Backlog | Estimate | Status |
| -------------- | -------- | ------ |
| Set up the development environment | 3 | Closed |
| Read an account | 3 | Closed |
| Update an account | 5 | Closed |
| Delete an account | 3 | Closed |
| List all accounts | 3 | Closed |

Velocity: **17 points**.

---

## Sprint 2 — CI and security

| Sprint Backlog | Estimate | Status |
| -------------- | -------- | ------ |
| Add continuous integration with GitHub Actions | 5 | Closed |
| Secure the RESTful service | 5 | Closed |

Velocity: **10 points**.

---

## Sprint 3 — Docker, Kubernetes, CD

| Sprint Backlog | Estimate | Status |
| -------------- | -------- | ------ |
| Containerize the microservice using Docker | 5 | Closed |
| Deploy the Docker image to Kubernetes | 8 | Closed |
| Build an automated CD pipeline | 8 | Closed |

Velocity: **21 points**.

---

## Final board state

| New Issues | Icebox | Product Backlog | Sprint Backlog | In Progress | Done | Closed |
| ---------- | ------ | --------------- | -------------- | ----------- | ---- | ------ |
| — | — | — | — | — | — | All 9 stories |

All stories are in **Closed** after the sprint reviews.

---

## Reproducing this board in ZenHub

1. Create the repository `devops-capstone-project` from the IBM template.
2. Connect the repository to ZenHub and create the workspace `capstone-project`.
3. Create the nine issues from `docs/user-stories.md` using
   `.github/ISSUE_TEMPLATE/story_template.md`.
4. Add the `enhancement` and `technical debt` labels.
5. Create three one-week sprints named **Sprint 1**, **Sprint 2**, **Sprint 3**.
6. Assign estimates and sprints as shown above.
7. Move each story through `In Progress → Done → Closed` as you complete it.
