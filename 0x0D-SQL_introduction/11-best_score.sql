/*shows all rows greater than 10*/
SELECT score, name from second_table
WHERE score >= 10
GROUP BY score DESC, name;
