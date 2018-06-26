-- only comedy
SELECT ts.title, tgg.name FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tgs
ON ts.id = tgs.show_id
LEFT JOIN tv_genres AS tgg
ON tgs.genre_id = tgg.id
ORDER BY ts.title, tgg.name;
