# Sparkify ETL and Data Dashboard

## Project Structure

This project was built so that data stakeholder at Sparkify kan get insights about their app.
The Project was structured like below

```
- Data -> this was the folder that contains song plays log to be ingested
- create_tables.py -> used to initiate the project and make sure each iteration was started using a clean database
- Dashboard.ipynb -> The data dashboard for this project.
- etl.ipynb -> Jupyter notebook to test and develop etl function
- etl.py ->  used to init/do ETL process
- sql_queries -> collection of sql_queries
- test.ipynb -> Collections of sql test function to check database content
```

## How to Start ETL process

1. Run `python create_tables.py`
2. Run `python etl.py`
3. Then you can access the dashboard and get insights

## Insight Included in the Project
Here are some insight included in the project:
1. Gender distribution among user
2. Level distribution (paid vs free)
3. Top 10 artists listened
4. Top 10 songs listened
5. What device / user agent that user use
6. Number of Active User
7. 10 Most Active User

## Database Structure
The database schema was using a star schema with 1 Fact table that record songplays and several Dimension Table.

### Fact Table
- songplays - records in log data associated with song plays i.e. records with page NextSong songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
### Dimension Tables    
- users - users in the app
- - user_id, first_name, last_name, gender, level
- songs - songs in music database
- -song_id, title, artist_id, year, duration
- artists - artists in music database
- - artist_id, name, location, latitude, longitude
- time - timestamps of records in songplays broken down into specific units
- - start_time, hour, day, week, month, year, weekday