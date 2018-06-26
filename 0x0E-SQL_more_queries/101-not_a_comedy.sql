-- only comedy
SELECT title FROM tv_shows
WHERE title NOT IN (SELECT ts.title FROM tv_shows AS ts
JOIN tv_show_genres AS tgs
ON ts.id = tgs.show_id
JOIN tv_genres AS tgg
ON tgs.genre_id = tgg.id
WHERE tgg.name = 'Comedy'
)ORDER BY title;
