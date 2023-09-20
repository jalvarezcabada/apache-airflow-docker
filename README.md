# Apache Airflow 🚀

### Deploy 📦

1) _Create Docker Image_

```
docker build . -f Dockerfile -t airflow-dev:2.7.1
```

2) _Deploy docker-compose with all services_

```
docker-compose up -d
```

## Container verification ⚙️

_Status_

```
docker ps
```

_Logs_

```
docker logs <<container_id>>
```

## Built by 🛠️

Python, Apache Airflow y Docker

* [Apache Airflow](https://airflow.apache.org/)
* [Docker](https://www.docker.com//)

## Author ✒️

* **Joaquin Alvarez** - [jalvarezcabada](https://github.com/jalvarezcabada)
