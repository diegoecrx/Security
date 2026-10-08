# Infrastructure

| Folder | Content | Phase |
|---|---|---|
| `docker/` | Dockerfiles / compose overrides | v0.1 |
| `terraform/` | IaC (deliberately misconfigured examples: IAM, storage) | v1.0 stretch |
| `kubernetes/` | Manifests (privileged containers, secrets-in-manifest examples) | v1.0 stretch |

Scan all of it: `trivy config`, Checkov, tfsec (see [`../docs/04-tooling.md`](../docs/04-tooling.md)).
Intentional IaC issues are catalogued as IAC-00x in
[`../docs/05-vulnerability-catalog.md`](../docs/05-vulnerability-catalog.md). Start IaC
scanning against the Dockerfiles and compose file immediately; add Terraform/K8s later.
