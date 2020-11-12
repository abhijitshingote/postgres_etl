# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays (songplay_id serial primary key, start_time bigint not null, user_id int not null references users(user_id), level text, 
song_id text references songs(song_id), artist_id text references artists(artist_id), session_id int, location text, user_agent text,
CONSTRAINT uniq_usersongstarttime UNIQUE (user_id, song_id, start_time))
""")

user_table_create = ("""create table if not exists users (user_id int primary key, first_name text, last_name text, gender text, level text)
""")

song_table_create = ("""create table if not exists songs (song_id text primary key, title text, artist_id text, year int, duration float)
""")

artist_table_create = ("""create table if not exists artists (artist_id text primary key, name text, location text, latitude float, longitude float)
""")

time_table_create = ("""create table if not exists time (start_time numeric primary key, hour int, day int, week int, month int, year int, weekday int)
""")



# INSERT RECORDS

songplay_table_insert = ("""insert into songplays ( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values ( %s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (user_id, song_id, start_time) DO NOTHING
""")

user_table_insert = ("""insert into users (user_id, first_name, last_name, gender, level) values(%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""insert into songs (song_id, title, artist_id, year, duration) values (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""insert into artists (artist_id, name, location, latitude, longitude) values (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")


time_table_insert = ("""insert into time (start_time, hour, day, week, month, year, weekday) values (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""select s.song_id,a.artist_id
from songs s
inner join artists a on (a.artist_id=s.artist_id)
where s.title = %s 
and a.name = %s
and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [ user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]