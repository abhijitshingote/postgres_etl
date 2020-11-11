## Use Case for Database Sparkify
Database provides the data infrastructure to consume Sparkify app logs in the form of songs and user actions. Data is consumed and then housed in a relational DB that makes analysis of this data much easier to further allow improvement of Sparkify product.

## Database Schema Design
Database follows conventional design principles so we have dimension tables for artists, songs, users and a fact table that logs users interaction with the songs. ETL pipeline consumes songs/artists data and app log data. Both are in the form of json documents.

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