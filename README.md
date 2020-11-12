## Use Case for Database Sparkify
Database provides the data infrastructure to consume Sparkify app logs in the form of songs and user actions. Data is consumed and then housed in a relational DB that makes analysis of this data much easier to further allow improvement of Sparkify product.

## Database Schema Design
Database follows conventional design principles so we have dimension tables for artists, songs, users and a fact table that logs users interaction with the songs. ETL pipeline consumes songs/artists data and app log data. Both are in the form of json documents.
#### artists table
![Alt text](images/artisttable.png?raw=true "Title")

#### users table
![Alt text](images/usertable.png?raw=true "Title")

#### song table
![Alt text](images/songtable.png?raw=true "Title")

#### time table
![Alt text](images/timetable.jpg?raw=true "Title")

#### songplay table
![Alt text](images/songplaytable.png?raw=true "Title")

## Files
create_tables.py  - Creates database and then the subsequent tables by reading sql_queries.py
sql_queries.py - Create and insert queries to be used in create_tables.py and etl.py
etl.py - After tables have been created after running create_tables.py, use this script to process files and insert records from data/.
test.ipynb - test if records are available in the tables
etl.ipynb - can be ignored. used to test functionality of etl.py
data/ - repo of files to be processed
images/ - ignore

## Instructions
```
1.  python3 create_tables.py'     - Creates database and then the subsequent tables by reading sql_queries.py
2.  python3 etl.py   - process files and insert records from data/
```

## Example Queries
#### Top 5 most popular artist
select a.name,count(*) as number_of_songs_played from songplays s 
inner join artists a using (artist_id) 
group by a.name  order by 2 desc limit 5

#### Top 5 most popular songs
select a.name,s.title,count(*) as number_of_times_song_played from songplays sp 
inner join songs s using (song_id) inner join artists a on (a.artist_id=s.artist_id) 
group by a.name,s.title order by 3 desc limit 5

#### Most active users
select first_name,last_name,count(*) as total_songs_played
from songplays sp inner join users using (user_id) 
group by first_name,last_name order by 3 desc limit 5