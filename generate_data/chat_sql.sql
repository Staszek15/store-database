CREATE TABLE addresses
(
  address_id  INT         NOT NULL,
  address     VARCHAR(50) NOT NULL,
  country     VARCHAR(50) NOT NULL,
  city        VARCHAR(50) NOT NULL,
  postal_code VARCHAR(10) NOT NULL,
  PRIMARY KEY (address_id)
);

CREATE TABLE customers
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
  PRIMARY KEY (customer_id),
  FOREIGN KEY (address_id) REFERENCES addresses (address_id)
);

CREATE TABLE games
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

CREATE TABLE inventory_buy
(
  inventory_id INT     NOT NULL AUTO_INCREMENT,
  game_id      INT     NOT NULL,
  price        FLOAT   NOT NULL,
  available    BOOLEAN NOT NULL,
  PRIMARY KEY (inventory_id),
  FOREIGN KEY (game_id) REFERENCES games (game_id)
);

CREATE TABLE inventory_rent
(
  inventory_id INT     NOT NULL AUTO_INCREMENT,
  game_id      INT     NOT NULL,
  price        FLOAT   NOT NULL,
  available    BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (inventory_id),
  FOREIGN KEY (game_id) REFERENCES games (game_id)
);

CREATE TABLE staff
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
  PRIMARY KEY (staff_id),
  FOREIGN KEY (address_id) REFERENCES addresses (address_id)
);

CREATE TABLE purchases
(
  purchase_id  INT  NOT NULL AUTO_INCREMENT,
  inventory_id INT  NOT NULL,
  customer_id  INT  NOT NULL,
  date         DATE NOT NULL,
  staff_id     INT  NOT NULL,
  PRIMARY KEY (purchase_id),
  FOREIGN KEY (inventory_id) REFERENCES inventory_buy (inventory_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
);

CREATE TABLE rentals
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
  PRIMARY KEY (rental_id),
  FOREIGN KEY (inventory_id) REFERENCES inventory_rent (inventory_id),
  FOREIGN KEY (game_id) REFERENCES games (game_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
);



CREATE TABLE tournament
(
  tournament_id        INT          NOT NULL AUTO_INCREMENT,
  name                 VARCHAR(100) NOT NULL,
  date                 DATE         NOT NULL,
  game_id              INT          NOT NULL,
  team_players_number  INT          NOT NULL,
  staff_id             INT          NOT NULL,
  total_players_number INT          NOT NULL,
  PRIMARY KEY (tournament_id),
  FOREIGN KEY (game_id) REFERENCES games (game_id),
  FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
);

CREATE TABLE tournament_results
(
  tournament_id INT NOT NULL,
  customer_id   INT NOT NULL,
  place         INT NOT NULL,
  score         INT NOT NULL,
  FOREIGN KEY (tournament_id) REFERENCES tournament (tournament_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);
