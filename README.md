# dbt-sts-ge

Playground pipeline with Airflow 2, Spark Thrift Server, dbt and Great Expectations

## How to run

* First of all you need to build the required Airflow and Spark Thrift Server containers.
  * Go to the folder `dockers` and run the script called `build_dockers.sh`.
  * Back to the main folder.
* Run docker compose with the command: `docker-compose -f docker-compose.yaml up`
  * Airflow should be listening in the http address: `http://localhost:8080/`
  * Sparkt Thrift Server should be listening in the thrift address: `jdbc:hive2://localhost:10000`

### Airflow 2

Airflow is running with the default username and password whose value is `airflow`.


