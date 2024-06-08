# Web User Behaviour Analytics
An Airflow DAG project to track and analyze user behavior on a website by monitoring page accesses and time spent by users identified by IP addresses, with daily statistics calculation for marketing analysis.

# Description
This project aims to analyze user behavior on a website by tracking page accesses and the time spent by users, identified by IP addresses. The data processing pipeline is built using Apache Airflow for orchestration, Polars for data manipulation.

# Features
* Data Extraction: Uses requests to fetch upcoming rocket launch data from the SpaceDevs API.
* Data Processing: Implements Airflow DAGs (Directed Acyclic Graphs) to manage and automate workflows.
* Data Aggregation: Aggregates data using Polars to calculate metrics such as the number of page accesses and total time spent by each user.
* Containerization: Runs Airflow and its dependencies inside Docker containers for a consistent and reproducible setup.

# Technologies Used
* Apache Airflow: Orchestrates and schedules the data pipeline tasks.
* Docker: Provides containerization for the development and deployment environment.
* Python: The primary programming language used for scripting and data manipulation.
* Data Transformation and Aggregation: Read and Aggregates data using Polars to calculate metrics such as the number of page accesses and total time spent by each user.

# Setup Instructions
### 1. Clone the repository:
```
git clone https://github.com/your-username/rocket-launch-project.git
cd rocket-launch-project
```
### 2. Build the Docker image:
```
docker build -t airflow-rocket-launch .
```
### 3. Run the Docker container:
```
# Edit the Local path as per your need
docker run --rm -d -p 8080:8080 -v /d/Apache-airflow/Rocket_launch_project/tmp:/opt/airflow/tmp airflow-rocket-launch
```
### 4. Access the Airflow web interface:
Open your browser and navigate to http://localhost:8080 to access the Airflow UI.

### 5. Scopes
1) Aggregated data can be stored in DB(SQLALCHEMY). As of now I'm storing the data in CSV files.
2) For Visualization, Streamlit can be used.



