# flink_local
A local flink setup using docker compose.
The purpose is to create a simple python csv generator to demonstrate the steps in this video from confluent:

https://developer.confluent.io/courses/apache-flink/stream-processing/


# Start & stop
### Start
~~~~sh
make up
~~~~

### Stop
~~~~sh
make stop_down
~~~~

## Example 1

1. Start up
2. Start up FlinkSQL by executing:
~~~~sh
make flink_sql
~~~~
2. Paste into FlinkSQL: 

~~~~sql
CREATE TABLE my_table (
    id INT,
    name STRING,
    age INT
) WITH (
    'connector' = 'filesystem',
    'path' = '/opt/flink/jobs/01_data.csv',
    'format' = 'csv'
);
~~~~

## Example 2

1. Start up
2. In a separate window (tab or tmux) go into 
3. In project root: 
~~~~sh
poetry install
~~~~
4. To enter shell: 
~~~~sh
poetry shell
~~~~
5. Enter:
~~~~sh
cd scripts/02_fake_colored_generator 
~~~~
6. make sure you have the correnct python version: 
~~~~sh
python3 --version 
~~~~

or 

~~~~sh
which python3
~~~~

7. Execute: 
~~~~sh
python3 data_generator.py
~~~~

8. Start flink sql: 
~~~~sh
make flink_sql
~~~~
9. Enter the following scripts:

### Event tables

Drop if exitsts.

~~~~sql
DROP TABLE IF EXISTS cs1;
DROP TABLE IF EXISTS cs2;
~~~~

Create the stream tables.

~~~~sql
CREATE TABLE cs1 (
    id INT,
    name STRING,
    age INT,
    color STRING
) WITH (
    'connector' = 'filesystem',
    'path' = '/opt/flink/jobs/data/02_colored_data_live/stream1.csv',
    'format' = 'csv'
);

CREATE TABLE cs2 (
    id INT,
    name STRING,
    age INT,
    color STRING
) WITH (
    'connector' = 'filesystem',
    'path' = '/opt/flink/jobs/data/02_colored_data_live/stream2.csv',
    'format' = 'csv'
);
~~~~


~~~~sql
SELECT * FROM cs1;
SELECT * FROM cs2;
~~~~

### Events combined 

~~~~sql

CREATE VIEW events AS
SELECT * FROM cs1
UNION ALL
SELECT * FROM cs2;
~~~~


~~~~sql
select * from events;
~~~~

Create results table (for this you need to ensure the docker engine has permissions to create)

~~~~sql
CREATE TABLE results (
    color STRING,
    event_count BIGINT
) WITH (
    'connector' = 'filesystem',
    'path' = '/opt/flink/jobs/data/02_colored_data_live/results.csv',
    'format' = 'csv'
);
~~~~

To see the combination this is enough:

~~~~sql
SELECT color, count(*) as event_count  FROM events GROUP BY color;
~~~~
