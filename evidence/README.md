# Evidence

This folder contains the evidence that can be produced **locally**. The
capstone also requires screenshots from GitHub, ZenHub, and the OpenShift
cluster; those cannot be generated from a terminal and are listed in
`docs/EVIDENCE_CHECKLIST.md`.

## Real, reproducible files

| File | Produced by | Shows |
| ---- | ----------- | ----- |
| `test-results.txt` | `bash scripts/test.sh` | 32 passing unit tests |
| `flake8.txt` | `bash scripts/capture-evidence.sh` | lint results |
| `rest-create.txt` | `bash scripts/demo-api.sh` | `POST /accounts` → `201 CREATED` |
| `rest-list.txt` | `bash scripts/demo-api.sh` | `GET /accounts` → `200 OK` |
| `rest-read.txt` | `bash scripts/demo-api.sh` | `GET /accounts/1` → `200 OK` |
| `rest-update.txt` | `bash scripts/demo-api.sh` | `PUT /accounts/1` → `200 OK` |
| `rest-delete.txt` | `bash scripts/demo-api.sh` | `DELETE /accounts/1` → `204 NO CONTENT` |
| `security-headers.txt` | `bash scripts/demo-api.sh` | Talisman headers + CORS |
| `docker-run.txt` | `docker run ... accounts:1` | the container starts healthy and serves the API |
| `kube-images.txt` | `bash scripts/build-image.sh` | the built `accounts:1` image |

## Files that must come from your cluster or GitHub

| File | Where it comes from |
| ---- | ------------------- |
| `pipelinerun.txt` | `tkn pipelinerun logs -L` in the lab cluster |
| `kube-deploy-accounts.txt` | `oc get all -l app=accounts` |
| every `*.jpg` / `*.png` | GitHub, ZenHub, and the OpenShift console |

`pipelinerun.txt` in this folder is a placeholder that describes the expected
content. Replace it with the real log before submitting.

## Regenerate everything local

```bash
bash scripts/capture-evidence.sh
```
