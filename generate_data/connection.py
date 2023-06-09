from sqlalchemy import create_engine, text, URL
from unidecode import unidecode
import pandas as pd

def connect():

    print("Connecting to database...")

    url_object = URL.create(
        "mysql+pymysql",
        username="team21",
        password="te@mzi", 
        host="giniewicz.it",
        database="team21"
    )

    engine = create_engine(url_object)
    conn = engine.connect()
    print("Connected to database.")
    conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
    conn.execute(text("DROP TABLE IF EXISTS addresses, customers, games, inventory_buy, inventory_rent, purchases, rentals, staff, tournament, tournament_results"))
    
    print("Old tables dropped.")

    fd = open('create_tables.sql', 'r')
    sqlTablesFile = fd.read()
    fd.close()
    sqlTablesCode = sqlTablesFile.split(';')[:-1]   # without last one because last query also ends with ';' so last element is empty

    for command in sqlTablesCode:
        print(text(command))
        conn.execute(text(command))    


    insert_data(engine=engine, conn=conn)


    conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))
    conn.close()



def insert_data(engine, conn):

    print("Inserting data...")
     
    df_games = pd.read_csv('game/game.csv')
    df_inventory_rent = pd.read_csv('inventory_rent/inventory_rent.csv')
    df_inventory_buy = pd.read_csv('inventory_buy_purchase/inventory_buy.csv')
    df_addresses = pd.read_csv('address/address.csv')
    df_customers = pd.read_csv('customer_rental/customers.csv')
    df_purchases = pd.read_csv('inventory_buy_purchase/purchases.csv')
    df_rentals = pd.read_csv('customer_rental/rentals.csv')
    df_staff = pd.read_csv('staff/staff.csv')
    df_tournament = pd.read_csv('tournament/tournaments.csv')
    df_tournament_results = pd.read_csv('tournament_results/tournament_results.csv')


    #conn.execute(text('TRUNCATE TABLE games'))
    #conn.execute(text('ALTER TABLE game DROP CONSTRAINT '))
    conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
    df_games.to_sql("games", con=engine, if_exists="append", index=False)
    print("Table games inserted.")

    #conn.execute(text('TRUNCATE TABLE addresses'))
    df_addresses.to_sql("addresses", con=engine, if_exists="append", index=False)

    #conn.execute(text('TRUNCATE TABLE customers'))
    df_customers.to_sql("customers", con=engine, if_exists="append", index=False)
    print("Table customers inserted")

    #conn.execute(text('TRUNCATE TABLE inventory_buy'))
    df_inventory_buy.to_sql("inventory_buy", con=engine, if_exists="append", index=False)
    print("Table inventory_buy inserted")


    #conn.execute(text('TRUNCATE TABLE inventory_rent'))
    df_inventory_rent.to_sql("inventory_rent", con=engine, if_exists="append", index=False)
    print("Table inventory_rent inserted")

    #conn.execute(text('TRUNCATE TABLE staff'))
    df_staff.to_sql("staff", con=engine, if_exists="append", index=False)
    print("Table staff inserted")


    #conn.execute(text('TRUNCATE TABLE purchases'))
    df_purchases.to_sql("purchases", con=engine, if_exists="append", index=False)
    print("Table purchases inserted")

    #conn.execute(text('TRUNCATE TABLE rentals'))
    df_rentals.to_sql("rentals", con=engine, if_exists="append", index=False)
    print("Table rentals inserted")
    
    #conn.execute(text('TRUNCATE TABLE tournament'))
    df_tournament.to_sql("tournament", con=engine, if_exists="append", index=False)
    print("Table tournament inserted")

    #conn.execute(text('TRUNCATE TABLE tournament_results'))
    df_tournament_results.to_sql("tournament_results", con=engine, if_exists="append", index=False)
    print("Table tournament_results inserted")


if __name__ == "__main__":
        connect()
