# DROP TABLES

drop_table_queries = []
# songplays table
drop_table_queries.append("DROP TABLE IF EXISTS songplays")
# users table
drop_table_queries.append("DROP TABLE IF EXISTS users")
# songs table
drop_table_queries.append("DROP TABLE IF EXISTS songs")
# artists table
drop_table_queries.append("DROP TABLE IF EXISTS artists")
# time table
drop_table_queries.append("DROP TABLE IF EXISTS time")

# CREATE TABLES

create_table_queries = []
# songplays  table
create_table_queries.append("CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time bigint NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)")
# users table
create_table_queries.append("CREATE TABLE IF NOT EXISTS users (user_id int NOT NULL PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar)")
# songs table
create_table_queries.append("CREATE TABLE IF NOT EXISTS songs (song_id text NOT NULL PRIMARY KEY, title varchar, artist_id varchar, year int, duration numeric)")
# artists table
create_table_queries.append("CREATE TABLE IF NOT EXISTS artists (artist_id varchar NOT NULL PRIMARY KEY, name varchar, location varchar, latitude numeric, longitude numeric)")
#time table
create_table_queries.append("CREATE TABLE IF NOT EXISTS time (start_time bigint NOT NULL PRIMARY KEY, hour int, day int, week int, month text, year int, weekday text)")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users (gender,user_id,first_name, last_name, level) VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
 INSERT INTO time ("start_time", "year", "month", "week", "day", "weekday") VALUES(%s,%s,%s,%s,%s,%s)
 ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, artists.artist_id from songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")
