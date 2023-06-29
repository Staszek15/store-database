import pandas as pd
import random
import numpy as np
from scipy.special import softmax


def generate_game_ids(games):
    """
    Generate random games ids with probability based on their maximum players number and rating.
    """
    game_id = []
    probs = [0.2, 0.4, 0, 0.3, 0.1]  # probability of drawing games for max 1, 2, 3, 4 and 5 or more players
    # we do not have games for max 3 players in our shop
    n_players = np.random.choice([1, 2, 3, 4, 5], size=500, p=probs)  # draw a random number of 1, 2, 3 etc

    for i in range(1, 6):
        n = (n_players == i).sum()  # number of all games for consecutive max players number
        if i == 5:
            # games for max 5 or more players
            prob_r = softmax(games.loc[games['max_players'] >= i, 'rating'].values)
            # probability of drawing games in certain group of max players based on their ratings
            simulated_id = list(np.random.choice(games.loc[games['max_players'] >= i, 'game_id'].values, p=prob_r,
                                                 size=n))
            game_id += simulated_id
        else:
            if len(games.loc[games['max_players'] == i, 'rating'].values) != 0:
                # because we do not have games for max 3 players
                prob_r = softmax(games.loc[games['max_players'] == i, 'rating'].values)
                simulated_id = list(np.random.choice(games.loc[games['max_players'] == i, 'game_id'].values, p=prob_r,
                                                     size=n))
                game_id += simulated_id
    return game_id


def generate_inventory_rent(prices, games):
    """
    Generate data frame for inventory_rent table.
    :param prices: prices of renting each game
    :param games: table with information about owned games
    """
    game_ids = generate_game_ids(games)
    random.shuffle(game_ids)
    prices = [prices[str(game_id)] for game_id in game_ids]
    data = {'inventory_id': np.arange(1, 501),
            'game_id': game_ids,
            'price': prices,
            }
    return pd.DataFrame(data)


def check_if_rent_available(inv_rent, rental):
    """
    Add new column to inventory_rent data frame with information about particular game availability.
    """
    available = []
    for i in range(len(inv_rent)):
        if pd.isna(rental.loc[rental['inventory_id'] == inv_rent.iloc[i]['inventory_id'], 'return_date'].values[-1]):
            # check if latest rented game of particular inventory_id has been returned
            available.append(False)
        else:
            available.append(True)
    inv_rent['available'] = available
    return pd.DataFrame(inv_rent)
