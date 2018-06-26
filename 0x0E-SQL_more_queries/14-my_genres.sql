-- genre id by show
SELECT tgg.name from tv_genres AS tgg
JOIN tv_show_genres AS tgs
ON tgs.genre_id = tgg.id
JOIN tv_shows AS ts
ON ts.id = tgs.show_id
WHERE ts.title='Dexter'
GROUP BY tgg.name ASC;
