# Python GitOps

![Build, Scan & Deploy](https://github.com/ydvsailendar/python-gitops/actions/workflows/build-and-bump.yaml/badge.svg)
![CodeQL](https://github.com/ydvsailendar/python-gitops/actions/workflows/codeql.yaml/badge.svg)


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

## ARGOCD

- create app namespace
```bash
kubectl create namespace argocd
```

- deploy argocd stack
```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

- expose app service
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

- get argocd admin creds
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

## App

- create argocd project for python-gitops
```bash
kubectl apply -f k8s/argocd/project.yaml
```

- deploy python-gitops application
```bash
kubectl apply -f k8s/argocd/application.yaml
```

- create app namespace
```bash
kubectl create namespace python-gitops
```

- expose app service
```bash
kubectl port-forward svc/python-gitops -n python-gitops 9090:80
```

## Monitoring

- add all in one monitoring stack
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

- create namespace for monitoring
```bash
kubectl create namespace monitoring
```

- deploy the stack
```bash
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
```

- expose grafana service
```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```

- get grafana admin creds
```bash
kubectl get secret monitoring-grafana -n monitoring  -o jsonpath="{.data.admin-password}" | base64 --decode
```

- expose alertmanager service
```bash
kubectl port-forward svc/monitoring-kube-prometheus-alertmanager -n monitoring 9093:9093
```