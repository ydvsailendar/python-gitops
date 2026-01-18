# Python GitOps

![Build, Scan & Deploy](https://github.com/ydvsailendar/python-gitops/actions/workflows/build-and-bump.yaml/badge.svg)
![CodeQL](https://github.com/ydvsailendar/python-gitops/actions/workflows/codeql.yaml/badge.svg)
![SBOM](https://github.com/ydvsailendar/python-gitops/actions/workflows/build-and-bump.yaml/badge.svg)

## Security & Quality

- **Static code analysis** is performed using GitHub CodeQL for Python.
- **Container images** are scanned for known vulnerabilities using Trivy.
- Scan results are visible in GitHub Actions and the Security tab.
- High and Critical vulnerabilities are surfaced early without blocking development.

## Supply Chain Security

- A **Software Bill of Materials (SBOM)** is generated for every container image.
- SBOMs are produced using **Syft** in **CycloneDX** format.
- The SBOM is built from the final image and published as a CI artifact.
- This enables vulnerability impact analysis and dependency traceability.

## Dependency Management

- Dependencies are monitored and updated using **GitHub Dependabot**.
- Updates are proposed via pull requests and validated through CI.
- Security alerts are visible in the GitHub Security dashboard.
