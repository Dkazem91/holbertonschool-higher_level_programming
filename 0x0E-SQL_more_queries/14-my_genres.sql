-- genre id by show
SELECT tgg.name FROM tv_genres AS tgg
LEFT JOIN tv_show_genres AS tgs
ON tgs.genre_id = tgg.id
WHERE tgs.show_id = 8
GROUP BY tgg.name ASC;
