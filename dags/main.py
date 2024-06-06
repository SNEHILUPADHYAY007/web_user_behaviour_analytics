import datetime as dt
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
import polars as pl

# Initializing the DAG
dag = DAG(
    dag_id = "web_user_behaviour_analytics",
    start_date = dt.datetime(2024,6,6),
    schedule_interval = None,
)

final_csv_file_loc = "/opt/airflow/assets/agg_data.csv"


# Function to read the CSV and rename the defaults cols using Polars
def read_csv_file():
    # read the csv file
    df = pl.read_csv("/opt/airflow/assets/user_behavior_large.csv")
    # col to rename to
    req_col_name = ["date", "ip_address", "page_accessed", "access_time", "time_spent_in_sec"]
    col_names_df = df.columns
    # Making a dict to rename the cols
    # zip(old_col_name, new_col_name)
    new_col_names = dict(zip(col_names_df, req_col_name))
    print(new_col_names)
    # renaming the cols 
    df = df.rename(new_col_names)
    return df

# Function to add agg operations on the Dataframe
def perform_agg(df):
    df_new = df.select(pl.col(["ip_address","page_accessed","time_spent_in_sec"])).group_by(["ip_address","page_accessed"]).agg(
    pl.col("time_spent_in_sec").sum().alias("total_time_spent_in_sec"),
    pl.col("time_spent_in_sec").mean().alias("avg_time_spent_in_sec"),
    pl.col("time_spent_in_sec").max().alias("max_time_spent_in_sec"),
    pl.col("time_spent_in_sec").min().alias("min_time_spent_in_sec")
).sort("ip_address", descending = False)
    print(df_new.head(20))

    return df_new

   

# main method to call all the functions sequentially
def main():
    # Read CSV FILE
    df = read_csv_file()

    # Perform aggregations
    df_final = perform_agg(df) 

    df_final.write_csv(final_csv_file_loc)

    
    

# Python operator to perform basic operations on the File data
perform_file_operations = PythonOperator(
    task_id = "perform_file_operations",
    python_callable = main,
    dag = dag,
)



perform_file_operations 