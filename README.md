# Postgres_project 

A startup called Sparkify wants to analyze the data they've been collecting on songs and user
activity on their new music streaming app. The analytics team is particularly interested 
in understanding what songs users are listening to. Currently, they don't have an easy way to
query their data, which resides in a directory of JSON logs on user activity on the app,
as well as a directory with JSON metadata on the songs in their app.

They'd like to create a Postgres database with tables designed to optimize queries on song play
analysis and create a database schema and ETL pipeline for this analysis.

summary of the project : A star schema created with the songplays as a fact table from song_data
folder and the the rest of the tables are the dimension tables from log_data folder

the purpose of the project : Is to  analyze the data they've been collecting on songs and user
activity on their new music streaming app in an easy well designed postgres database

how to run the Python scripts : Python scripts are run in project.ipynb notebook after
finishing all sql_queries.py first. First create_tables.py is run in the notebook then etl.py is run .

explanation of the files in the repository: Using song_data in songplays and artists table,
and log_data for the rest of tables to be able to query and extract the artist name and song
from a simple query line  
