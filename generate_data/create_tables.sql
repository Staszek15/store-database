
        
CREATE OD REPLACE TABLE addresses
(
  address_id  INT         NOT NULL,
  address     VARCHAR(50) NOT NULL,
  country     VARCHAR(50) NOT NULL,
  city        VARCHAR(50) NOT NULL,
  postal_code VARCHAR(10) NOT NULL,
  PRIMARY KEY (address_id)
);

CREATE OD REPLACE TABLE customers
(
  customer_id       INT         NOT NULL AUTO_INCREMENT,
  first_name        VARCHAR(50) NOT NULL,
  last_name         VARCHAR(50) NOT NULL,
  birthdate         DATE        NOT NULL,
  email             VARCHAR(50) NULL    ,
  phone             VARCHAR(15) NOT NULL,
  address_id        INT         NOT NULL,
  registration_date DATE        NOT NULL,
  VIP               DATE        NULL    ,
  PRIMARY KEY (customer_id)
);

ALTER TABLE customers
  ADD CONSTRAINT UQ_customer_id UNIQUE (customer_id);

CREATE OD REPLACE TABLE games
(
  game_id             INT          NOT NULL AUTO_INCREMENT,
  name                VARCHAR(100) NOT NULL,
  min_age             INT          NULL    ,
  min_players         INT          NOT NULL DEFAULT 1,
  max_players         INT          NULL    ,
  category            VARCHAR(50)  NOT NULL,
  duration            INT          NOT NULL,
  rating              FLOAT        NOT NULL,
  tournaments         BOOLEAN      NOT NULL DEFAULT FALSE,
  max_players_in_team INT          NOT NULL,
  min_players_in_team INT          NOT NULL,
  PRIMARY KEY (game_id)
);

ALTER TABLE games
  ADD CONSTRAINT UQ_game_id UNIQUE (game_id);

ALTER TABLE games
  ADD CONSTRAINT UQ_name UNIQUE (name);

CREATE OD REPLACE TABLE inventory_buy
(
  inventory_id INT     NOT NULL AUTO_INCREMENT,
  game_id      INT     NOT NULL,
  price        FLOAT   NOT NULL,
  available    BOOLEAN NOT NULL,
  PRIMARY KEY (inventory_id)
);

ALTER TABLE inventory_buy
  ADD CONSTRAINT UQ_inventory_id UNIQUE (inventory_id);

CREATE OD REPLACE TABLE inventory_rent
(
  inventory_id INT     NOT NULL AUTO_INCREMENT,
  game_id      INT     NOT NULL,
  price        FLOAT   NOT NULL,
  available    BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (inventory_id)
);

ALTER TABLE inventory_rent
  ADD CONSTRAINT UQ_inventory_id UNIQUE (inventory_id);

CREATE OD REPLACE TABLE purchases
(
  purchase_id  INT  NOT NULL AUTO_INCREMENT,
  inventory_id INT  NOT NULL,
  customer_id  INT  NOT NULL,
  date         DATE NOT NULL,
  staff_id     INT  NOT NULL,
  PRIMARY KEY (purchase_id)
);

ALTER TABLE purchases
  ADD CONSTRAINT UQ_purchase_id UNIQUE (purchase_id);

CREATE OD REPLACE TABLE rentals
(
  rental_id    INT   NOT NULL AUTO_INCREMENT,
  inventory_id INT   NOT NULL,
  rental_date  DATE  NOT NULL,
  return_date  DATE  NULL    ,
  game_id      INT   NOT NULL,
  customer_id  INT   NOT NULL,
  staff_id     INT   NOT NULL,
  fine         FLOAT NULL    ,
  price        FLOAT NOT NULL,
  PRIMARY KEY (rental_id)
);

ALTER TABLE rentals
  ADD CONSTRAINT UQ_rental_id UNIQUE (rental_id);

CREATE OD REPLACE TABLE staff
(
  staff_id   INT         NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name  VARCHAR(50) NOT NULL,
  salary     FLOAT       NOT NULL,
  birthdate  DATE        NOT NULL,
  start      DATE        NOT NULL,
  phone      VARCHAR(15) NOT NULL,
  address_id INT         NOT NULL,
  email      VARCHAR(50) NOT NULL,
  PRIMARY KEY (staff_id)
);

ALTER TABLE staff
  ADD CONSTRAINT UQ_staff_id UNIQUE (staff_id);

CREATE OD REPLACE TABLE tournament
(
  tournament_id        INT          NOT NULL AUTO_INCREMENT,
  name                 VARCHAR(100) NOT NULL,
  date                 DATE         NOT NULL,
  game_id              INT          NOT NULL,
  team_players_number  INT          NOT NULL,
  staff_id             INT          NOT NULL,
  total_players_number INT          NOT NULL,
  PRIMARY KEY (tournament_id)
);

ALTER TABLE tournament
  ADD CONSTRAINT UQ_tournament_id UNIQUE (tournament_id);

ALTER TABLE tournament
  ADD CONSTRAINT UQ_name UNIQUE (name);

CREATE OD REPLACE TABLE tournament_results
(
  tournament_id INT NOT NULL,
  customer_id   INT NOT NULL,
  place         INT NOT NULL,
  score         INT NOT NULL
);

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

        
      