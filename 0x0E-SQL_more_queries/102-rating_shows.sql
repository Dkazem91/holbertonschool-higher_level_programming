-- 102 advanced
SELECT ts.title, SUM(tr.rate) AS rating FROM tv_shows ts, tv_show_ratings tr
WHERE ts.id = tr.show_id
GROUP BY ts.title ORDER BY rating DESC;
