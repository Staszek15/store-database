import pandas as pd
import numpy as np
import random


def generate_tournament_results():
    tournaments = pd.read_csv('tournament/tournament.csv')
    customers = pd.read_csv('customer, rental/customer.csv')
    games = pd.read_csv('game/game.csv')
    
    participants_list = []
    score_list = []
    tour_id_list = []
    place_list = []
    
    for i in range(len(tournaments)):
        tour_row = tournaments.iloc[i]
        games_row = games[games['game_id'] == tour_row.game_id] 
        
        tour_id = [tour_row.tournament_id for i in range(tour_row.total_players_number)]
        customers_id = random.sample(sorted(customers.customer_id),tour_row.total_players_number)

        tour_id_list.extend(tour_id)
        participants_list.extend(customers_id)

        teams_number = int(np.floor(tour_row.total_players_number / tour_row.team_players_number))        

        if tour_row.team_players_number > 1:
            place = sorted(list(np.arange(1, teams_number + 1)) * int(games_row.max_players_in_team.iloc[0]))
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
    
    final_table = pd.DataFrame(tournaments_dictionary)
    final_table.to_csv('tournament_results/tournament_results.csv', index = False)
    return(final_table)    

if __name__ == "__main__":
    generate_tournament_results()