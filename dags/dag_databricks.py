from datetime import datetime
from airflow.decorators import dag
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

default_args = {
    'owner': 'owner_name',
    'start_date': datetime(2021, 10, 14),
    'email': ['email'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

@dag(
    dag_id='databricks',
    schedule_interval='0 7 * * 1-5',
    default_args=default_args, 
    description='<description>',
    catchup=False
)

def databricks_task():

    notebook_task_params = {
        'existing_cluster_id' : '<cluster_id>',
        'notebook_task' : {
            'notebook_path': '<notebook_path>',
        },
    }

    notebook_task = DatabricksSubmitRunOperator(
        task_id='<task_name>',
        databricks_conn_id='conexion_id',
        json=notebook_task_params)

    notebook_task

execute = databricks_task()
