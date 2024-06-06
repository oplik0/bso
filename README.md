# Projekt BSO - Obserwowalność K8S

## Budowanie i instalacja

Wymagane:
- Klaster K8S (np. Minikube)
- Skonfigurowany kubectl
- [Helm](https://helm.sh/)

1. Zbudowanie usługi w pythonie (potrzebne ponieważ nie jest opublikowana w DockerHub)
  ```bash
  cd trace-analyzer
  docker build -t trace-analyzer:latest
  ```

2. Instalacja charta helm:
  ```bash
  helm package bso-helm
  helm install bso ./bso-helm-0.1.0.tgz
  ```