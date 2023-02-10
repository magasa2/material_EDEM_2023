from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    dag_id="sample_dag",
    start_date=datetime(2022, 5, 28),
    schedule_interval=None,
    tags=["sample_dag"],
    default_args={'retries': 1},
) as dag:

    # Here the corresponding tasks
    start= EmptyOperator(task_id="start")
    end= EmptyOperator(task_id="end")

    #print_task= BashOperator(task_id="print_task", bash_command= 'echo "\n\n\nHELLO MDA!!!\n\n\n"',)
    true_task = EmptyOperator(task_id="true_task")
    false_task = EmptyOperator(task_id="false_task")

    @task.branch (task_id="is_Saturday")
    def is_Saturday():
        if datetime.today().isoweekday()== 5:
            return "true_task"
        return "false_task"


      # Here the DAG dependencies

    start>>is_Saturday()>>[true_task, false_task]>>end
    # Here the DAG dependencies
  
