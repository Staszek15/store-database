ALTER TABLE inventory_rent
  ADD CONSTRAINT FK_games_TO_inventory_rent
    FOREIGN KEY (game_id)
    REFERENCES games (game_id);

ALTER TABLE tournament
  ADD CONSTRAINT FK_games_TO_tournament
    FOREIGN KEY (game_id)
    REFERENCES games (game_id);

ALTER TABLE tournament
  ADD CONSTRAINT FK_staff_TO_tournament
    FOREIGN KEY (staff_id)
    REFERENCES staff (staff_id);

ALTER TABLE inventory_buy
  ADD CONSTRAINT FK_games_TO_inventory_buy
    FOREIGN KEY (game_id)
    REFERENCES games (game_id);

ALTER TABLE rentals
  ADD CONSTRAINT FK_staff_TO_rentals
    FOREIGN KEY (staff_id)
    REFERENCES staff (staff_id);

ALTER TABLE rentals
  ADD CONSTRAINT FK_inventory_rent_TO_rentals
    FOREIGN KEY (inventory_id)
    REFERENCES inventory_rent (inventory_id);

ALTER TABLE rentals
  ADD CONSTRAINT FK_customers_TO_rentals
    FOREIGN KEY (customer_id)
    REFERENCES customers (customer_id);

ALTER TABLE staff
  ADD CONSTRAINT FK_addresses_TO_staff
    FOREIGN KEY (address_id)
    REFERENCES addresses (address_id);

ALTER TABLE customers
  ADD CONSTRAINT FK_addresses_TO_customers
    FOREIGN KEY (address_id)
    REFERENCES addresses (address_id);

ALTER TABLE tournament_results
  ADD CONSTRAINT FK_tournament_TO_tournament_results
    FOREIGN KEY (tournament_id)
    REFERENCES tournament (tournament_id);

ALTER TABLE tournament_results
  ADD CONSTRAINT FK_customers_TO_tournament_results
    FOREIGN KEY (customer_id)
    REFERENCES customers (customer_id);

ALTER TABLE purchases
  ADD CONSTRAINT FK_inventory_buy_TO_purchases
    FOREIGN KEY (inventory_id)
    REFERENCES inventory_buy (inventory_id);

ALTER TABLE purchases
  ADD CONSTRAINT FK_customers_TO_purchases
    FOREIGN KEY (customer_id)
    REFERENCES customers (customer_id);

ALTER TABLE purchases
  ADD CONSTRAINT FK_staff_TO_purchases
    FOREIGN KEY (staff_id)
    REFERENCES staff (staff_id);
