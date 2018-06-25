-- counts and shows
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score DESC;
