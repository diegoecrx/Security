# One command vocabulary, identical on any machine.
# Uses '>' as the recipe prefix so it is robust to editors that strip tabs.
.RECIPEPREFIX = >
.PHONY: help up down logs build scan sast sca secrets dast iac sbom test clean

help:
> @echo "Targets: up down logs build | scan sast sca secrets dast iac sbom | test clean"

up:            ## start app + db + redis
> docker compose up -d --build

down:          ## stop and remove containers
> docker compose down

logs:
> docker compose logs -f

build:         ## build the application image
> docker compose build

scan: secrets sast sca iac   ## run all static local scans

sast:          ## Semgrep (static analysis)
> semgrep --config auto --sarif --output reports/sast/semgrep.sarif application/ || true

sca:           ## pip-audit + Trivy (dependencies)
> pip-audit -r application/backend/requirements.txt -f json -o reports/sca/pip-audit.json || true
> trivy fs --scanners vuln --format json -o reports/sca/trivy-fs.json application/ || true

secrets:       ## Gitleaks (secret scanning, incl. history)
> gitleaks detect --report-format sarif --report-path reports/secrets/gitleaks.sarif || true

iac:           ## Checkov / Trivy (IaC + Dockerfiles + compose)
> trivy config --format json -o reports/sca/trivy-config.json . || true

sbom:          ## generate CycloneDX SBOM (Syft)
> syft dir:application -o cyclonedx-json=reports/sbom/sbom.cdx.json || true

dast:          ## OWASP ZAP baseline against the running app (requires 'make up')
> docker run --rm -t --network host -v $(PWD)/reports/dast:/zap/wrk ghcr.io/zaproxy/zaproxy:stable \
>   zap-baseline.py -t http://localhost:8000 -J zap-baseline.json || true

test:          ## run application tests
> docker compose run --rm api pytest -q || true

clean:
> docker compose down -v
