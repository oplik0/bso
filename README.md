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

2. Konfiguracja
  ```sh
  cp values.example.yaml values.yaml
  ```
  I edytować:
  ```yaml
  grafana:
  email:
    address: your@email.com
    from_address: sending@address.com
    host: smtp.example.com:25
    user: username
    password: secretPassword
  discord:
    url: https://discord.com/api/webhooks/123456789/abcdefg
  ingress:
    hosts:
      - grafana.example.com
  ```
3. Instalacja charta helm:
  ```bash
  helm package bso-helm
  helm install bso ./bso-helm-0.1.0.tgz -f values.yaml
  ```