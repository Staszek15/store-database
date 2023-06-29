/*Wyznacz ranking na pracownika miesiąca dla każdego miesiąca,
 w którym sklep prowadził sprzedaż.*/

-- jeśli rozważamy tylko sprzedaż

SELECT date, staff_id, sales_number
FROM (
  SELECT DATE_FORMAT(date,'%Y-%m') AS date, staff_id, COUNT(purchase_id) AS sales_number,
         ROW_NUMBER() OVER (PARTITION BY DATE_FORMAT(date,'%Y-%m') ORDER BY COUNT(purchase_id) DESC) AS row_num
  FROM purchases
  GROUP BY DATE_FORMAT(date,'%Y-%m'), staff_id
) AS subquery
WHERE row_num = 1
ORDER BY date, sales_number DESC;

/*Sporządź analizę top 10 zawodników turniejowych w zależności
 od gry. */

SELECT t.game_id, customer_id, SUM(score)
FROM tournament_results AS results
LEFT JOIN tournament AS t USING(tournament_id)
GROUP BY game_id, customer_id
ORDER BY game_id, score DESC;

SELECT game_id, customer_id, score
FROM (
  SELECT t.game_id, customer_id, SUM(score) AS score,
        ROW_NUMBER() OVER (PARTITION BY game_id ORDER BY SUM(score) DESC) AS row_num
        FROM tournament_results AS results
        LEFT JOIN tournament AS t USING(tournament_id)
        GROUP BY game_id, customer_id
) AS subquery
WHERE row_num = 1;

SELECT t.game_id, customer_id, SUM(score) AS score,
        ROW_NUMBER() OVER (PARTITION BY game_id ORDER BY SUM(score) DESC) AS score
        FROM tournament_results AS results
        LEFT JOIN tournament AS t USING(tournament_id)
        GROUP BY game_id, customer_id;




