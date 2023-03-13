# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" create table if not exists songplay 
                        (
                        songplay_id serial Primary key,
                        start_time timestamp not null ,
                        user_id integer not null,
                        level text,
                        song_id text ,
                        artist_id text,
                        session_id text, 
                        location text, 
                        user_agent text )"""
                        )

user_table_create = ("""create table if not exists users 
                    (
                    user_id integer Primary Key,
                    first_name text,
                    last_name text,
                    gender text,
                    level text)"""
                    )

song_table_create = ("""create table if not exists song
                    (
                    song_id text Primary Key,
                    title text not null,
                    artist_id text ,
                    year int,
                    duration numeric not null)"""
                    )

artist_table_create = ("""create table if not exists artist
                      (
                      artist_id text Primary Key, 
                      artist_name text not null,
                      artist_location varchar,
                      artist_latitude float,
                      artist_longitude float)"""
                      )

time_table_create = ("""create table if not exists time
                    (
                    start_time timestamp primary key,
                    hour int, 
                    day int,
                    week int,
                    month int,
                    year int , 
                    weekday int)"""
                    )

# INSERT RECORDS

songplay_table_insert = ("""insert into songplay (
          start_time, user_id, level, song_id, 
          artist_id, session_id, location, 
          user_agent
                                                 ) 
          values 
          (%s,%s,%s,%s,%s,%s,%s,%s) on conflict(songplay_id) do nothing; """)
                         

user_table_insert = ("""insert into users (
          user_id , first_name , last_name ,
          gender , level 
                                          )
          values
          (%s,%s,%s,%s,%s)ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level; """)
                        

song_table_insert = ("""insert into song (
          song_id , title , artist_id , 
          year ,duration 
                                         )
          values
          (%s,%s,%s,%s,%s)on conflict(song_id) do nothing; """)
                        

artist_table_insert = ("""insert into  artist(
          artist_id, artist_name, artist_location,
          artist_latitude,artist_longitude
                                             )
          values(%s,%s,%s,%s,%s)on conflict(artist_id) do ;""")
                        


time_table_insert = ("""insert into time(
          start_time, hour, day, week,
          month, year,weekday
                                        )
          values(%s,%s,%s,%s,%s,%s,%s)on conflict(start_time) do nothing;""")
                    

# FIND SONGS

song_select = ("""select 
                        song.song_id, 
                        artist.artist_id 
                  from 
                        song 
                  join artist 
                  on song.artist_id = artist.artist_id
""")

# QUERY LISTS

create_table_queries = [ user_table_create,song_table_create,artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [ user_table_drop, song_table_drop, artist_table_drop, time_table_drop,songplay_table_drop]