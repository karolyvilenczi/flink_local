# flink_local
A local flink setup using docker compose.
The purpose is to create a simple python csv generator to demonstrate the steps in this video from confluent:

https://developer.confluent.io/courses/apache-flink/stream-processing/


# Start & stop
### Start
make up

### Stop
make stop_down

## Example 1

1. Start up
2. make flink_sql
3. paste: 

CREATE TABLE my_table (
    id INT,
    name STRING,
    age INT
) WITH (
    'connector' = 'filesystem',
    'path' = '/opt/flink/jobs/01_data.csv',
    'format' = 'csv'
);


## Example 2

1. Start up
2. In a separate window (tab or tmux) go into 
3. in project root: poetry install
4. enter shell: poetry shell
5. cd scripts/02_fake_colored_generator 
6. make sure you have the correnct python version: 'python3 --version' or 'which python3'
7. python3 data_generator.py (let it run)
8. enter flink sql: 'make flink_sql'
9. enter:

### Event tables

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
