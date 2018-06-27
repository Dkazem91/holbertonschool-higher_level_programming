-- This list all tv show ratings
SELECT tg.name, SUM(tr.rate) AS rating FROM tv_show_genres tgs
JOIN tv_genres tg
ON tg.id = tgs.genre_id
JOIN tv_show_ratings tr
ON tr.show_id = tgs.show_id
GROUP BY  tg.name DESC ORDER BY RATING DESC;
