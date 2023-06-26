import pandas as pd
import random
import numpy as np
from scipy.special import softmax


games_buy_prices = {
    '1': 164.5,
    '2': 65.00,
    '3': 158.70,
    '4': 170.32,
    '5': 139.90,
    '6': 119.19,
    '7': 182.55,
    '8': 179.90,
    '9': 409.95,
    '10': 269.90,
    '11': 59.90,
    '12': 169.90,
    '13': 479.00,
    '14': 169.00,
    '15': 42.38,
    '16': 100.00,
    '17': 39.90,
    '18': 62.50,
    '19': 199.99,
    '20': 112.89,
    '21': 650.00,
    '22': 219.00,
    "23": 25.50,
    '24': 188.65,
    '25': 56.60,
    '26': 350.00,
    '27': 74.99,
    '28': 129.99,
    '29': 289.00,
    '30': 277.80,
    '31': 120.00,
    '32': 115.60,
    '33': 158.95,
    '34': 28.00,
    '35': 162.55,
    '36': 185.2,
    '37': 46.50,
    '38': 239.90,
    '39': 37.00,
    '40': 103.00,
    '41': 28.80,
    '42': 120.00,
    '43': 56.70,
    '44': 79.90,
    '45': 117.97,
    '46': 25.60,
    '47': 16.70,
    '48': 180.00,
    '49': 115.60,
    '50': 133.20
}
games_rent_prices = {game_id: round(buy_price/15, 2) for game_id, buy_price in games_buy_prices.items()}
games = pd.read_csv('game/game.csv')

def exchange_players_to_game_id():
    game_id = []
    probs = [0.2, 0.4, 0, 0.3, 0.1]  # we do not have games for max 3 players
    n_players = np.random.choice([1, 2, 3, 4, 5], size=500, p=probs)  #draw random number of 1, 2, 3 etc
    for i in range(1, 6):
        n = (n_players == i).sum()
        if i == 5:
            prob_r = softmax(games.loc[games['max_players'] >= i, 'rating'].values)
            simulated_id = list(np.random.choice(games.loc[games['max_players'] >= i, 'game_id'].values, p=prob_r, size=n))
            game_id += simulated_id
        else:
            if len(games.loc[games['max_players'] == i, 'rating'].values) != 0:
                prob_r = softmax(games.loc[games['max_players'] == i, 'rating'].values)
                simulated_id = list(np.random.choice(games.loc[games['max_players'] == i, 'game_id'].values, p=prob_r, size=n))
                game_id += simulated_id
    return game_id


def generate_inventory_rent():
    game_ids = exchange_players_to_game_id()
    random.shuffle(game_ids)
    prices = [games_rent_prices[str(game_id)] for game_id in game_ids]
    data = {'inventory_id': np.arange(1, 501),
                      'game_id': game_ids,
                      'price': prices,
                      }
    inventory_rent = pd.DataFrame(data)
    return inventory_rent


generate_inventory_rent()