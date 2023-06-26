import pandas as pd
import numpy as np

def suitable_for_tournament(dataframe):
    if dataframe['duration'] <= 120 and dataframe['max_players'] <= 40:
        return True
    else:
        return False
    
def generate_game():
    games = pd.read_csv('game/games_dataset.csv', index_col = 0)
    games.columns.str.lower()   
    games = games.rename(columns={'age':'min_age'})
    games['tournaments'] = games.apply(suitable_for_tournament, axis = 1)
    
    max_players_in_team = [1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    min_players_in_team = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
     
    games['max_players_in_team'] = max_players_in_team
    games['min_players_in_team'] = min_players_in_team
    
    games.to_csv('game/game.csv', index = False)
    
if __name__ == "__main__":
    generate_game()