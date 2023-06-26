import pandas as pd
import random
import numpy as np
import openpyxl
from scipy.special import softmax
import random
from datetime import datetime, timedelta
import pandas as pd
from ast import literal_eval

free_days = ['2023-01-01', '2023-01-06', '2023-04-09', '2023-04-10', '2023-05-01', '2023-05-03', '2023-05-28', '2023-06-08',
            '2022-01-01', '2022-01-06', '2022-04-17', '2022-04-18', '2022-05-01', '2022-05-03', '2022-06-05', '2022-06-16',
            '2022-08-15', '2022-11-01', '2022-11-11', '2022-12-25', '2022-12-26', '2021-01-06', '2021-04-04', '2021-04-05',
            '2021-05-01', '2021-05-03', '2021-05-23', '2021-06-03', '2021-08-15', '2021-11-01', '2021-11-11', '2021-12-25',
            '2021-12-26']

games_buy_prices = {
    '1': 164.5,
    '2' : 65.00,
    '3' : 158.70,
    '4' : 170.32,
    '5' : 139.90,
    '6' : 119.19,
    '7' : 182.55,
    '8' : 179.90,
    '9': 409.95,
    '10' : 269.90,
    '11' : 59.90,
    '12' : 169.90,
    '13' : 479.00,
    '14' : 169.00,
    '15' : 42.38,
    '16' : 100.00,
    '17' : 39.90,
    '18' : 62.50,
    '19' : 199.99,
    '20' : 112.89,
    '21': 650.00,
    '22' : 219.00,
    "23" : 25.50,
    '24' : 188.65, 
    '25' : 56.60,
    '26' : 350.00,
    '27' : 74.99,
    '28' : 129.99,
    '29' : 289.00,
    '30' : 277.80,
    '31' : 120.00,
    '32' : 115.60,
    '33' : 158.95,
    '34' : 28.00,
    '35' : 162.55,
    '36' : 185.2,
    '37' : 46.50,
    '38' : 239.90,
    '39' : 37.00,
    '40' : 103.00,
    '41' : 28.80,
    '42' : 120.00,
    '43' : 56.70,
    '44' : 79.90,
    '45' : 117.97,
    '46' : 25.60,
    '47' : 16.70,
    '48' : 180.00,
    '49' : 115.60,
    '50' : 133.20
}


def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() not in free_days:  # Sprawdza, czy nie są to dni wolne od pracy
            yield current_date
        current_date += timedelta(days=1)
    
def generate_random_numbers_prob(prob, n=6):
    while True:
        yield random.choices(range(n), weights=prob)[0]
        
def generate_random_numbers(n=6):
    while True:
        yield random.choices(range(n))[0]

def generate_id(name, df_id, df, n=1):
    df_id[name] = [i for i in range(1, len(df)+n)]

def exchange_players_to_game_id(df, n_players):
    games = pd.read_csv('game\game.csv')
    game_id = []
    for i in range(1, 6):
        n = (n_players == i).sum()
        if i == 5:
            prob_r = softmax(games.loc[games['max_players'] >= i, 'rating'].values)
            simulated_id = list(np.random.choice(games.loc[games['max_players'] >= i, 'game_id'].values, p = prob_r, size = n))
            game_id += simulated_id
        else:
            if len(games.loc[games['max_players'] == i, 'rating'].values) != 0:
                prob_r = softmax(games.loc[games['max_players'] == i, 'rating'].values)
                simulated_id = list(np.random.choice(games.loc[games['max_players'] == i, 'game_id'].values, p = prob_r, size = n))
                game_id += simulated_id
    return game_id
 
def generate_inventory_buy_purchase():
    games = pd.read_csv('game\game.csv')


    start_date = datetime(2021, 1, 4)
    end_date = datetime(2023, 6, 15)


    probabilities = [0.05, 0.15, 0.15, 0.15, 0.2, 0.2]
    probabilities_2021 = [0.3, 0.3, 0.3, 0.05, 0.05, 0.05]
    first_days = [datetime(2021, 1, 4), datetime(2021, 1, 5), datetime(2021, 1, 7), datetime(2021, 1, 8)]

    date_generator = generate_dates(start_date, end_date)
    random_number_generator = generate_random_numbers()
    random_number_generator_prob = generate_random_numbers_prob(probabilities_2021)
    random_number_generator_first_days = generate_random_numbers_prob(probabilities)


    data = []
    for date in date_generator:
        if date in first_days:
            random_number = next(random_number_generator_first_days)
            data.append({'date': date, 'purchases': random_number})
        elif date.year == 2021:
            random_number = next(random_number_generator_prob)
            data.append({'date': date, 'purchases': random_number})
        else:
            random_number = next(random_number_generator)
            data.append({'date': date, 'purchases': random_number})


    df = pd.DataFrame(data)
    df = df.drop(df[df['purchases'] == 0].index)
    df = df.loc[df.index.repeat(df['purchases'])].reset_index(drop=True)
    df = df.drop('purchases', axis=1)
    generate_id('purchase_id', df, df)
    items = []
    for date in df['date']:
        random_number = random.randint(1, 3)
        items.append(random_number)
    df['items'] = items
    df = df.loc[df.index.repeat(df['items'])].reset_index(drop=True)
    df = df.drop('items', axis=1)

    df_inventory = pd.DataFrame()
    generate_id('inventory_id', df_inventory, df, 151)

    possible_players = [1, 2, 3, 4, 5]
    probs = [0.2, 0.4, 0, 0.3, 0.1] 
    np.random.seed(42)

    n_players = np.random.choice([1, 2, 3, 4, 5], size = len(df_inventory), p=probs) 
    game_ids = exchange_players_to_game_id(df_inventory, n_players)
    random.shuffle(game_ids)

    prices = [games_buy_prices.get(str(game_id)) for game_id in game_ids]

    df_inventory['game_id'] = game_ids
    df_inventory['price'] = prices

    lista = [True]*150 + [False]*250
    random.shuffle(lista)
    available = [False]*(len(df_inventory)-400) + lista

    # this is the table of inventory_buy
    df_inventory['available'] = available

    df_inventory_false = df_inventory[df_inventory['available']==False]

    big_lista = []
    for i in range(50):
        big_lista.append(list(df_inventory_false['inventory_id'][df_inventory_false['game_id']==i+1]))

    inventory_purchase = []
    big_lista = [lista[::-1] for lista in big_lista]
    while True:
        n = len(big_lista)
        i = random.randint(0, n-1)
        chunk = big_lista[i]
        if chunk:
            d=chunk.pop()
        if not chunk:
            big_lista.remove(big_lista[i])
        inventory_purchase.append(d)
        if not big_lista:
            break 

    df['inventory_id'] = inventory_purchase
    df['game_id'] = [int(df_inventory_false['game_id'][df_inventory_false['inventory_id'] == inv].values) for inv in df['inventory_id'].values]

    staff_id = pd.read_csv('constants\staff_schedule.csv', index_col=[0])
    staff_id['staff_ids'].iloc[staff_id[(staff_id['date'] == "2023-06-11")].index[0]]

    staff_id.loc[:,'staff_ids'] = staff_id.loc[:,'staff_ids'].apply(lambda x: literal_eval(x))
    staff_id_ = []
    for date in df['date']:
      staff_id_.append(random.choice((staff_id['staff_ids'].iloc[staff_id[(staff_id['date'] == date.strftime('%Y-%m-%d'))].index[0]])))

    df["staff_id"] = staff_id_

    customer = pd.read_csv('customer, rental\customer.csv')

    tmp = (df
    .merge(games[['game_id', 'age']], 'left', 'game_id')
    .groupby('purchase_id')['age']
    .max()
    .reset_index()
    ).copy()

    tmp['key'] = 1
    customer['key'] = 1

    tmp2 = (tmp
    .merge(df[['date', 'purchase_id']], 'left', 'purchase_id')
    .merge(customer[['key', 'birthdate', 'customer_id']], on='key')
    .assign(customer_age = lambda x: ((x['date']-x['birthdate'].astype('datetime64')).dt.days/365).astype(int))
    .assign(valid_customer = lambda x: x['customer_age'] > x['age'])
    .query('valid_customer')
    .groupby('purchase_id')['customer_id']
    .apply(list)
    .reset_index()
    )

    purchase_id_final = tmp2[['purchase_id']].copy()
    purchase_id_final['chosen_customer'] = tmp2['customer_id'].apply(lambda x: random.choice(x))

    purchase_id = (df
              .merge(purchase_id_final[['purchase_id', 'chosen_customer']], 'left', 'purchase_id'))
    purchase_id = purchase_id.drop('game_id', axis=1)
    purchase_id = purchase_id.rename(columns={'chosen_customer': 'customer_id'})
    
    return df_inventory, purchase_id

if __name__ == "__main__":
  print(generate_inventory_buy_purchase())