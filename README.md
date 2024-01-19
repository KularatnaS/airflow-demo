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

To install additional python packages:
```
docker build . --tag extending_airflow:latest
```

Launching a MINIO docker container:
```
docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   --name minio2 \
   -v ~/minio/data:/data \
   -e "MINIO_ROOT_USER=ROOTNAME" \
   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
   quay.io/minio/minio server /data --console-address ":9001"
```