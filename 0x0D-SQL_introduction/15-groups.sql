-- when score
-- is more than twice
SELECT score, COUNT(score) FROM second_table GROUP BY score HAVING COUNT(score) > 1;
