/*Rozkład - liczba rejestracji w kazdym kolejnym miesiacu*/

SELECT 
  DATE_FORMAT(registration_date,'%Y-%m') AS registration_month, 
  COUNT(*) AS num_of_registrations
FROM customers
GROUP BY registration_month;

/*Liczba wypożyczeb w kazdym koeljnym miesiacu*/
SELECT *
FROM rentals;

SELECT 
  DATE_FORMAT(rental_date, '%Y-%m') AS rental_month,
  COUNT(*) AS num_of_rentals
FROM rentals
GROUP BY rental_month;


/*Wyznacz ranking na pracownika miesiąca dla każdego miesiąca,
 w którym sklep prowadził sprzedaż.*/

-- jeśli rozważamy tylko sprzedaż

SELECT date, CONCAT(s.first_name, ' ', s.last_name) AS employee, sales_number
FROM (
  SELECT DATE_FORMAT(date,'%Y-%m') AS date, staff_id, COUNT(purchase_id) AS sales_number,
         ROW_NUMBER() OVER (PARTITION BY DATE_FORMAT(date,'%Y-%m') ORDER BY COUNT(purchase_id) DESC) AS row_num
  FROM purchases
  GROUP BY DATE_FORMAT(date,'%Y-%m'), staff_id
) AS subquery
LEFT JOIN staff AS s USING(staff_id)
WHERE row_num = 1
ORDER BY date, sales_number DESC;


SELECT employee, COUNT(*) AS how_often
FROM (SELECT date, CONCAT(s.first_name, ' ', s.last_name) AS employee, sales_number
FROM (
  SELECT DATE_FORMAT(date,'%Y-%m') AS date, staff_id, COUNT(purchase_id) AS sales_number,
         ROW_NUMBER() OVER (PARTITION BY DATE_FORMAT(date,'%Y-%m') ORDER BY COUNT(purchase_id) DESC) AS row_num
  FROM purchases
  GROUP BY DATE_FORMAT(date,'%Y-%m'), staff_id
) AS subquery
LEFT JOIN staff AS s USING(staff_id)
WHERE row_num = 1
ORDER BY date, sales_number DESC) AS tab
GROUP BY employee
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT *
FROM games;

SELECT (date), employee, MAX(sales_number) AS max_sales
FROM (SELECT date, CONCAT(s.first_name, ' ', s.last_name) AS employee, sales_number
FROM (
  SELECT DATE_FORMAT(date,'%Y-%m') AS date, staff_id, COUNT(purchase_id) AS sales_number,
         ROW_NUMBER() OVER (PARTITION BY DATE_FORMAT(date,'%Y-%m') ORDER BY COUNT(purchase_id) DESC) AS row_num
  FROM purchases
  GROUP BY DATE_FORMAT(date,'%Y-%m'), staff_id
) AS subquery
LEFT JOIN staff AS s USING(staff_id)
WHERE row_num = 1
ORDER BY date, sales_number DESC) AS subquery;



/*Sporządź analizę top 10 zawodników turniejowych w zależności
 od gry. */

SELECT g.name AS game, CONCAT(c.first_name, ' ', c.last_name) AS player, score
FROM (
  SELECT t.game_id, customer_id, SUM(score) AS score,
        ROW_NUMBER() OVER (PARTITION BY game_id ORDER BY SUM(score) DESC) AS row_num
        FROM tournament_results AS results
        LEFT JOIN tournament AS t USING(tournament_id)
        GROUP BY game_id, customer_id
) AS subquery
LEFT JOIN customers AS c USING(customer_id)
LEFT JOIN games AS g USING(game_id)
WHERE row_num IN (1,2,3,4,5,6,7,8,9,10) 
AND game_id IN (
    SELECT game_id FROM (
      SELECT DISTINCT game_id FROM tournament ORDER BY RAND() LIMIT 3
    ) AS random_games
  )
ORDER BY game_id, score DESC;

SELECT g.name AS game, CONCAT(c.first_name, ' ', c.last_name) AS player, score
FROM (
  SELECT t.game_id, customer_id, SUM(score) AS score
  FROM tournament_results AS results
  LEFT JOIN tournament AS t USING(tournament_id)
  WHERE t.game_id IN (
    SELECT DISTINCT game_id
    FROM tournament
    ORDER BY RAND()
    LIMIT 3
  )
  GROUP BY game_id, customer_id
) AS subquery
LEFT JOIN customers AS c USING(customer_id)
LEFT JOIN games AS g USING(game_id)
ORDER BY game_id, score DESC;

SELECT game_id FROM (
      SELECT game_id FROM tournament ORDER BY RAND() LIMIT 3
    ) AS random_games


/*Gracz z największa liczba punktow za wszystkie turnieje*/
SELECT CONCAT(c.first_name, ' ', c.last_name) AS player, SUM(r.score) AS total_score
FROM tournament_results AS r
LEFT JOIN customers AS c USING(customer_id)
GROUP BY player
ORDER BY total_score DESC
LIMIT 1;

/*Ustal, które gry przynoszą największy dochód ze sprzedaży, 
a które z wypożyczeń.*/

-- wypozyczenia
SELECT g.name AS game, ROUND(SUM(r.price + r.fine) - 0.7*r.price*15,2) AS rental_income, COUNT(r.rental_id)
FROM rentals AS r
LEFT JOIN inventory_rent AS i USING(inventory_id)
LEFT JOIN games AS g ON i.game_id = g.game_id
GROUP BY g.name
ORDER BY rental_income DESC
LIMIT 3;


-- kupna
SELECT g.name AS game, ROUND(SUM(i.price - 0.7*i.price) , 2) AS buy_income, COUNT(p.purchase_id)
FROM purchases AS p
LEFT JOIN inventory_buy AS i USING(inventory_id)
LEFT JOIN games AS g ON i.game_id = g.game_id
GROUP BY g.name
ORDER BY buy_income DESC
LIMIT 3;

 
/*Skąd są klienci? wrocław, dolnoslaskie, reszta polski */
SELECT *
FROM customers;

-- osoby z wrocławia
SELECT COUNT(c.customer_id) AS num_of_customers
FROM customers AS c
LEFT JOIN addresses AS a USING(address_id)
WHERE a.city = 'Wrocław'
GROUP BY a.city;

-- dolnośląskie
SELECT COUNT(c.customer_id) AS num_of_customers
FROM customers AS c
LEFT JOIN addresses AS a USING(address_id)
WHERE (a.city <> 'Wrocław') AND 
(a.postal_code REGEXP '^50|^51|^52|^53|^54|^55|^56|^57|^58|^59|^67-2');

-- reszta
SELECT COUNT(c.customer_id) AS num_of_customers
FROM customers AS c
LEFT JOIN addresses AS a USING(address_id)
WHERE (a.city <> 'Wrocław') AND
(a.postal_code NOT REGEXP '^50|^51|^52|^53|^54|^55|^56|^57|^58|^59|^67-2');
 63 164 372

WITH tab AS (
 SELECT c.customer_id, a.city, CASE WHEN a.city = 'Wrocław' THEN 'Wrocław'
 WHEN (a.city <> 'Wrocław') AND
  (a.postal_code REGEXP '^50|^51|^52|^53|^54|^55|^56|^57|^58|^59|^67-2') 
 THEN 'Dolnośląskie'
 WHEN (a.city <> 'Wrocław') AND
(a.postal_code NOT REGEXP '^50|^51|^52|^53|^54|^55|^56|^57|^58|^59|^67-2') 
THEN  'reszta'
END AS region
FROM customers as c
LEFT JOIN addresses AS a USING(address_id))
  /*
SELECT region, COUNT(*)
FROM tab
GROUP BY region;*/

SELECT *
FROM tab WHERE region IS NULL;

SELECT *
FROM customers
WHERE customer_id = 433;


/* Klienci, którzy wydali najmniej i najwięcej hajsu łącznie w sklepie
(i wypozyczenia i kupna)*/
--TRZEBA JESZCZE WZIAC PIERWSZY I OSTATNI WIERSZ
-- ALE DLUGO MULI WIEC JAK MACIE JAKIS INNY POMYSL NA TO TO PROSZE BARDZO
SELECT c.customer_id, ROUND(SUM(r.price + r.fine + i.price), 2) AS money_spend
FROM customers AS c
LEFT JOIN rentals AS r ON c.customer_id = r.customer_id
LEFT JOIN purchases AS p ON c.customer_id = p.customer_id
LEFT JOIN inventory_buy AS i ON p.inventory_id = i.inventory_id
GROUP BY c.customer_id
ORDER BY money_spend;

SELECT c.customer_id
FROM customers AS c
LEFT JOIN rentals AS r ON c.customer_id = r.customer_id
LEFT JOIN purchases AS p ON c.customer_id = p.customer_id
WHERE r.r
GROUP BY c.customer_id

/*5. Jak często wypożyczane są gry droższe niż średnia cena w sklepie
 a jak często tańsze. (np. liczba wypożyczen drozszych gier przez liczbe
  gier drozszych jakie posiada sklep)*/


WITH inv_ids AS (
  SELECT 
    CASE WHEN inventory_id IN (SELECT inventory_id 
    FROM inventory_rent
    WHERE price > (SELECT ROUND(AVG(price),2)
    FROM inventory_rent)) THEN 'droższe'
    CASE WHEN inventory_id IN (SELECT inventory_id 
  FROM inventory_rent
  WHERE price <= (SELECT ROUND(AVG(price),2)
  FROM inventory_rent)) THEN 'tańsze'
  END AS czy_drozsze
  FROM rentals
)

SELECT 
    CASE WHEN inventory_id IN (SELECT inventory_id 
    FROM inventory_rent
    WHERE price > (SELECT ROUND(AVG(price),2)
    FROM inventory_rent)) THEN 'droższe'
    CASE WHEN inventory_id IN (SELECT inventory_id 
  FROM inventory_rent
  WHERE price <= (SELECT ROUND(AVG(price),2)
  FROM inventory_rent)) THEN 'tańsze'
  END AS czy_drozsze
  FROM rentals;
SELECT COUNT(*)
FROM inv_ids
GROUP BY czy_drozsze;


-- gry drozsze niz srednia cena
SELECT inventory_id 
FROM inventory_rent
WHERE price > (SELECT ROUND(AVG(price),2)
FROM inventory_rent);

--gry tansze lub rowne sredniej cenie
SELECT inventory_id 
FROM inventory_rent
WHERE price <= (SELECT ROUND(AVG(price),2)
FROM inventory_rent);
