cd /opt/airflow/dbt/sts

dbt seed --profiles-dir /opt/airflow/dbt

dbt run --profiles-dir /opt/airflow/dbt
