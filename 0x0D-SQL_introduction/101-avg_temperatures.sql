-- average by city
SELECT city, AVG(value) AS avg_tmp FROM temperatures GROUP BY city ORDER BY avg_tmp DESC;
