# airflow-demo

Requirements:
- Docker
- Docker Compose v2.14.0+

Setup:
```
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker compose up airflow-init
docker compose up -d
```