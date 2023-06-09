import pandas as pd
import numpy as np
import random


def generate_tournament_results(tournaments, customers, games):
    """
    Function that choose customers who take part in a tournament, assigns points and ranks.
    :param tournaments: table with tournaments
    :customers: table with customers
    :games: table with games
    """
    participants_list = []
    score_list = []
    tour_id_list = []
    place_list = []
    #takes into consideration only this tournaments that have already taken place
    tournaments = tournaments[tournaments['staff_id'].notnull()]
    
    for i in range(len(tournaments)):
        tour_row = tournaments.iloc[i]
        games_row = games[games['game_id'] == tour_row.game_id]

        tour_id = [tour_row.tournament_id for i in range(int(tour_row.total_players_number))]
        customers_id = random.sample(sorted(customers.customer_id),tour_row.total_players_number)

        tour_id_list.extend(tour_id)
        participants_list.extend(customers_id)

        teams_number = int(np.floor(tour_row.total_players_number / tour_row.team_players_number))        

        if tour_row.team_players_number > 1:
            # every member of a team takes the same place
            place = sorted(list(np.arange(1, teams_number + 1)) * int(games_row.max_players_in_team.iloc[0]))
            #score from 1 (last place) to number of teams (first place)
            score = place[::-1]
            score_list.extend(score)
            place_list.extend(place)
            pass
            
        else:
            place = np.arange(1,len(customers_id) + 1)
            score = place[::-1]
            
            score_list.extend(score)
            place_list.extend(place)
            
    tournaments_dictionary = {'tournament_id' : tour_id_list, 'customer_id' : participants_list,
                              'place' : place_list, 'score' : score_list}

    return pd.DataFrame(tournaments_dictionary)
