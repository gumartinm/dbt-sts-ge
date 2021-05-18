#!/bin/bash

# Build docker Airflow
docker build -t airflow-dbt-ge AIRFLOW/

# Build docker STS
docker build -t spark-thrift-server-dbt-ge  STS/

