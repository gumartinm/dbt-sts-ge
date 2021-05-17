FROM apache/airflow:2.0.2

#
# Custom dependencies as environment variables
#
ARG CUSTOM_BUILD_APT_DEPS=" \
    build-essential \
    libsasl2-dev \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    unixodbc-dev \
    "
ENV CUSTOM_BUILD_APT_DEPS=${CUSTOM_BUILD_APT_DEPS}

ARG CUSTOM_RUN_APT_DEPS=" \
    curl \
    libsasl2-2 \
    libsasl2-modules \
    "
ENV CUSTOM_RUN_APT_DEPS=${CUSTOM_RUN_APT_DEPS}

ARG CUSTOM_PYTHON_DEPS=" \
    pyhive[hive]==0.6.3 \
    databricks-dbapi[sqlalchemy]==0.5.0 \
    great-expectations==0.13.19 \
    airflow-provider-great-expectations==0.0.6 \
    airflow-dbt==0.3.0 \
    dbt-spark[PyHive]==0.19.1 \
    "
ENV CUSTOM_PYTHON_DEPS=${CUSTOM_PYTHON_DEPS}


#
# Install packages
#
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends ${CUSTOM_BUILD_APT_DEPS} ${CUSTOM_RUN_APT_DEPS} && \
    su -l airflow -c "pip install --no-cache-dir --user ${CUSTOM_PYTHON_DEPS} apache-airflow-providers-apache-hive --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.6.txt""


#
# Patch databricks-dbapi[sqlalchemy] for Spark Thrift Server
#
USER root
COPY hive.py.patch /root/
RUN patch -d/ -p0 < /root/hive.py.patch


#
# Switch to airflow user
#
USER airflow


EXPOSE 8080
