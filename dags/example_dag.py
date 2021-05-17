from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow_dbt.operators.dbt_operator import (
    DbtSeedOperator,
    DbtRunOperator
)
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
import os


# Default settings
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 5, 21)
}

PROJECT_HOME = '/opt/airflow'
DBT_ROOT_DIR = os.path.join(PROJECT_HOME, 'dbt')
DBT_PROJECT_DIR = os.path.join(DBT_ROOT_DIR, 'sts')
DBT_TARGET = 'dev'
DBT_TARGET_DIR = os.path.join(DBT_PROJECT_DIR, 'target')
GE_ROOT_DIR = os.path.join(PROJECT_HOME, 'great_expectations')

dag = DAG(
    dag_id='example_dag',
    schedule_interval=None,
    default_args=default_args
)



dbt_seed = DbtSeedOperator(
    task_id='dbt_seed',
    dir=DBT_PROJECT_DIR,
    profiles_dir=DBT_ROOT_DIR,
    target=DBT_TARGET,
    dag=dag
)


validate_load = GreatExpectationsOperator(
    task_id='validate_load',
    assets_to_validate=[
        {
            'batch_kwargs': {
                'datasource': 'spark-thrift-server',
                'schema': 'example',
                'table': 'taxi_zone_lookup',
                'data_asset_name': 'taxi_zone_lookup'
            },
            'expectation_suite_name': 'custom_sql_query.warning'
        }
    ],
    data_context_root_dir=GE_ROOT_DIR,
    dag=dag
)


dbt_run = DbtRunOperator(
    task_id='dbt_run',
    dir=DBT_PROJECT_DIR,
    profiles_dir=DBT_ROOT_DIR,
    target=DBT_TARGET,
    dag=dag
)

ge_docs_generate = BashOperator(
    task_id='ge_docs_generate',
    bash_command=f'great_expectations docs build --directory {GE_ROOT_DIR} --assume-yes',
    dag=dag
)


dbt_seed >> validate_load >> ge_docs_generate >> dbt_run
