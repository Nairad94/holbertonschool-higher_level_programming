-- lists the number of records with the same score in the table second_table, returns a list of results with two columns: "score" and "number"
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY score DESC;
