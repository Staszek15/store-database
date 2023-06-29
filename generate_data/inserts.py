from sqlalchemy import create_engine, text, URL
from unidecode import unidecode
import pandas as pd

def insert(df_games, df_addresses, df_customers, df_inventory_buy, df_inventory_rent, df_purchases, df_rentals, df_staff, df_tournament, df_tournament_results):

    url_object = URL.create(
        "mysql+pymysql",
        username="team21",
        password="te@mzi", 
        host="giniewicz.it",
        database="team21",
    )

    engine = create_engine(url_object)
    conn = engine.connect()

    conn.execute(text('TRUNCATE TABLE games'))
    df_games.to_sql("games", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE addresses'))
    df_addresses.to_sql("addresses", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE customers'))
    df_customers.to_sql("customers", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE inventory_buy'))
    df_inventory_buy.to_sql("inventory_buy", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE inventory_rent'))
    df_inventory_rent.to_sql("inventory_rent", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE purchases'))
    df_purchases.to_sql("purchases", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE rentals'))
    df_rentals.to_sql("rentals", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE staff'))
    df_staff.to_sql("staff", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE tournament'))
    df_tournament.to_sql("tournament", con=engine, if_exists="replace", index=False)

    conn.execute(text('TRUNCATE TABLE tournament_results'))
    df_tournament_results.to_sql("tournament_results", con=engine, if_exists="replace", index=False)

    



    conn.close()

if __name__ == "__main__":
        insert(pd.read_csv('game/game.csv'),
           pd.read_csv('inventory_rent/inventory_rent.csv'),
           pd.read_csv('inventory_buy_purchase/inventory_buy.csv'),

           pd.read_csv('address/address.csv'),
           pd.read_csv('customer_rental/customers.csv'),
           
           pd.read_csv('inventory_buy_purchase/purchases.csv'),
           pd.read_csv('customer_rental/rentals.csv'),
           pd.read_csv('staff/staff.csv'),
           pd.read_csv('tournament/tournament.csv'),
           pd.read_csv('tournament_results/tournament_results.csv'))
