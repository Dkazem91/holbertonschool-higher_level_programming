-- no name order
SELECT score, name FROM second_table
WHERE name <> ''
GROUP BY score DESC, name DESC;
