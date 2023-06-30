import pandas as pd


def suitable_for_tournament(dataframe):
    """
    Function that cheks if a game is suitable for a tournament.
    :param dataframe: dataframe containing information on games
    It returns True if game is ok for a tournament and False if not.
    """
    if dataframe['duration'] <= 120 and dataframe['max_players'] <= 40:
        return True
    else:
        return False


def generate_game():
    """
    Function that takes an dataset downloaded from the Internet and add information
    about minimum and maximum number of players in a team. 
    It returns a DataFrame which later will be used to fill a game table in a database. 
    """
    games = pd.read_csv('game/games_dataset.csv', index_col = 0)
    games.columns.str.lower()   
    games = games.rename(columns={'age':'min_age'})
    games['tournaments'] = games.apply(suitable_for_tournament, axis=1)
    
    max_players_in_team = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1,
                           1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    min_players_in_team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1,
                           1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
     
    games['max_players_in_team'] = max_players_in_team
    games['min_players_in_team'] = min_players_in_team

    return pd.DataFrame(games)
