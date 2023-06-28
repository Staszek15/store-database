import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_dates():
    
    number = np.random.randint(1,105)
    number = np.random.randint(1,105)
    if number%3 == 2:
        period = number * 7
    elif number%3 == 1:
        period = number * 7 + 3
    else:
        period = number * 7 + 6
        
    start = datetime.strptime('2021-04-07', "%Y-%m-%d")
    tournament_date = start + timedelta(days=period)

    return(tournament_date)


def first_element_to_integer(list_):
    my_list = list_
    return(my_list[-2])


def generate_tournament_staff(date,schedule):
    date_str = [date_obj.strftime('%Y-%m-%d') for date_obj in date]
    date_str = pd.DataFrame(date_str)
    date_str.columns=['date']
    date_merge_staff = date_str.merge(schedule, on='date', how='left')
    date_merge_staff['staff_ids'] = date_merge_staff['staff_ids'].apply(first_element_to_integer)
    staff_id = date_merge_staff.staff_ids
    return(staff_id)



    
def generate_total_players(table_game,game_id, inventory_rent):
    games_number = inventory_rent.game_id.value_counts()
    availability_df = pd.DataFrame(games_number)
    
    games_table = table_game[['game_id','min_players','max_players','duration', 'max_players_in_team','min_players_in_team']]
    game_id_df = pd.DataFrame(game_id, columns=['game_id'])
    merged = game_id_df.merge(games_table, on='game_id', how='inner')
    merged_availability = merged.merge(availability_df, on='game_id', how='inner')

    total_num = []
    for i in range(len(merged_availability)):
        row = merged_availability.iloc[i]
        
        if row['count'] > 20:
            boards_num = 16
        elif row['count'] > 10 and row['count'] <= 20: 
            boards_num = int(np.ceil(row['count'] / 2))
        else:
            boards_num = row['count'] - 1
        
        if row.max_players_in_team > 1: 
            teams_per_board =  int(np.floor(row['max_players'] / row['max_players_in_team']))
            players_all_board = [teams_per_board * row.max_players_in_team for i in range(boards_num)]
            total_num.extend([np.sum(players_all_board)])

        else:
            players_per_board = [np.random.randint(row.min_players,row.max_players + 1) for i in range(boards_num)]
            total_num.extend([np.sum(players_per_board)])
            
    merged_availability['total_players_number'] = total_num
    
    return(merged_availability.total_players_number)


def generate_tournament(games, inv_rent, schedule):
    name = ['Cosmic Entertainment', 'Battlefields of Bonaparte', 'The Kobolds', 'Gaming Evening', 'Hamst&Furious', 'Indian Camp', 'Vietgame',
             'Thematic Contest', 'Spring Tournament', 'Star Trek Day']
    n = len(name)
    tournament_id = np.arange(1, n+1)
    game_id = [9, 27, 33, 33, 7, 5, 36, 6, 1, 19]
    date = np.sort([generate_dates() for _ in range(n)])
    
    team_players_number = [games.max_players_in_team[games.game_id == i].values[0] for i in game_id]
    total_players_number = generate_total_players(games, game_id, inv_rent)

    staff_id = generate_tournament_staff(date, schedule)

    tournaments_dict = {'tournament_id' : tournament_id,
                        'name' : name,
                        'date' : date,
                        'game_id' : game_id,
                        'team_players_number' : team_players_number,
                        'staff_id' : staff_id,
                        'total_players_number' : total_players_number
                    }
    return pd.DataFrame(tournaments_dict)



