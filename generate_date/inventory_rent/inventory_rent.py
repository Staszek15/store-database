import pandas as pd
import random
import numpy as np
from scipy.special import softmax

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


def generate_inventory_rent(prices):
    game_ids = exchange_players_to_game_id()
    random.shuffle(game_ids)
    prices = [prices[str(game_id)] for game_id in game_ids]
    data = {'inventory_id': np.arange(1, 501),
                      'game_id': game_ids,
                      'price': prices,
            }
    return pd.DataFrame(data)
