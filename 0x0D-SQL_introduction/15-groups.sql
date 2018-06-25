-- counts and shows
SELECT score, COUNT(score) AS number from second_table
GROUP BY score DESC;
