from airflow import DAG
from datetime import datetime
from airflow_dbt.operators.dbt_operator import (
    DbtSeedOperator,
    DbtRunOperator
)
import os


# Default settings
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 5, 21)
}

PROJECT_HOME = '/opt/airflow/dbt'
DBT_PROJECT_DIR = os.path.join(PROJECT_HOME, 'sts')
DBT_TARGET = 'dev'
DBT_TARGET_DIR = os.path.join(DBT_PROJECT_DIR, 'target')

dag = DAG(
    dag_id='example_dag',
    schedule_interval=None,
    default_args=default_args
)



dbt_seed = DbtSeedOperator(
    task_id='dbt_seed',
    dir=DBT_PROJECT_DIR,
    profiles_dir=PROJECT_HOME,
    target=DBT_TARGET,
    dag=dag
)


dbt_run = DbtRunOperator(
    task_id='dbt_run',
    dir=DBT_PROJECT_DIR,
    profiles_dir=PROJECT_HOME,
    target=DBT_TARGET,
    dag=dag
)


dbt_seed >> dbt_run
