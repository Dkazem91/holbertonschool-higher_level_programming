-- genre id by show

SELECT tgs.name, COUNT(tg.genre_id) as number_shows
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
LEFT JOIN tv_genres as tgs
ON tg.genre_id = tgs.id
WHERE tg.genre_id IS NOT NULL
GROUP BY tgs.name ORDER BY number_shows DESC;
