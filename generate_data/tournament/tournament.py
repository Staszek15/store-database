import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_date(start_date,weeks_n):
    """
    Function generating date of a tournament. It chooses randomly number of weeks that passed from a given 
    start moment. 0, 3 or 6 is added to change a day of the week.
    :param start: the earliest date for the first tournament
    :weeks_n: time horizon
    """
    number = np.random.randint(1,weeks_n)
    if number%3 == 2:
        period = number * 7 #wednesday
    elif number%3 == 1:
        period = number * 7 + 3 #saturday
    else:
        period = number * 7 + 6 #tuesday
        
    #convert string to datetime   
    start = datetime.strptime(start_date, "%Y-%m-%d") #wednesday
    tournament_date = start + timedelta(days=period)

    return(tournament_date)


def last_element(list_):
    """
    Function extracting a last element of a given list.
    :param list_: list of elements
    Returns the last element.
    """
    return(list_[-1])


def generate_tournament_staff(date,schedule):
    """Function that choose a staff member who is responsible for conducting
    a tournament. It selects the last person from the list of employees who
    are at work to provide diversity. Usually 1 or 2 people are there, manager
    works the most and he is represented by 1. Selecting the last let involve
    other workers more.
    : param date: date of a tournament
    : schedule: work timetable
    Returns a person who is at work at a given day.
    """
    date_str = [date_obj.strftime('%Y-%m-%d') for date_obj in date]
    date_str = pd.DataFrame(date_str)
    date_str.columns=['date']
    date_merge_staff = date_str.merge(schedule, on='date', how='left')
    # choose last element, because manager with id 1 is the first one and he is the most frequent at job
    date_merge_staff['staff_ids'] = date_merge_staff['staff_ids'].apply(last_element) 
    staff_id = date_merge_staff.staff_ids
    return(staff_id)



    
def generate_total_players(table_game,game_id, inventory_rent):
    """
    Function generating list of number of players who participated in tournamens.
    :param table_game: dataset of games
    :param game_id: id values of games that are selected 
    Returns a padnas Series with numbers that reresent complete amount of participants.
    """
    games_number = inventory_rent.game_id.value_counts()
    availability_df = pd.DataFrame(games_number)
    
    #creating a table of games and avilable pieces
    games_table = table_game[['game_id','min_players','max_players','duration', 'max_players_in_team','min_players_in_team']]
    game_id_df = pd.DataFrame(game_id, columns=['game_id'])
    merged = game_id_df.merge(games_table, on='game_id', how='left')
    merged_availability = merged.merge(availability_df, on='game_id', how='left')

    total_num = []
    for i in range(len(merged_availability)):
        row = merged_availability.iloc[i]
        #choosing the number of boards depending on accessible pieces
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
            #in case of games for individuals number of players per board is choosed randomly 
            players_per_board = [np.random.randint(row.min_players,row.max_players + 1) for i in range(boards_num)]
            total_num.extend([np.sum(players_per_board)])
            
    merged_availability['total_players_number'] = total_num
    
    return(merged_availability.total_players_number)


def generate_tournament(games, inv_rent, schedule):
    """Function generating tournamets dataframe taking limits on number of players into consideration.
    :param games: dataset of games
    :param inv_rent: dataset of games destined for rentals
    Returns a dataframe with dataframe containing complete information on tournaments"""
    n = 45
    name_base = ['Cosmic Entertainment', 'Battlefields of Bonaparte', 'The Kobolds', 'Gaming Evening', 'Hamst&Furious', 'Indian Camp', 'Vietgame',
             'Thematic Contest', 'Spring Tournament', 'Star Trek Day']
    game_id_base = [9, 27, 33, 33, 7, 5, 36, 6, 1, 19]

    pairs = list(zip(game_id_base,name_base))
    tournaments_pairs = random.choices(pairs,k=n)
    name = list(map(lambda x: x[1], tournaments_pairs))
    game_id = list(map(lambda x: x[0], tournaments_pairs))
    tournament_id = np.arange(1, n+1)
    
    team_players_number = [games.max_players_in_team[games.game_id == i].values[0] for i in game_id]
    
    tournaments_past = 30
    tournaments_future = n-tournaments_past
    
    total_players_number_past = generate_total_players(games, game_id[:tournaments_past], inv_rent)       
    date_past = np.sort([generate_date('2021-04-07',105) for _ in range(tournaments_past)])
    staff_id_past = generate_tournament_staff(date_past,schedule)
    
    total_players_number_future = [None for i in range(tournaments_future)]
    date_future = np.sort([generate_date('2023-07-01',30) for _ in range(tournaments_future)])
    staff_id_future =[None for i in range(tournaments_future)]
    
    
    name_dictionary = {}
    new_names = []
    
    for tour_name in name:
        if tour_name in name_dictionary:
            name_dictionary[tour_name] += 1
            new_names.append(f'{tour_name} {name_dictionary[tour_name]}')
        else:
            name_dictionary[tour_name] = 1
            new_names.append(f'{tour_name} {name_dictionary[tour_name]}')

    tournaments_dict_past = {'tournament_id' : tournament_id[:tournaments_past],
                    'name' : new_names[:tournaments_past],
                    'date' : date_past,
                    'game_id' : game_id[:tournaments_past],
                    'team_players_number' : team_players_number[:tournaments_past],
                    'staff_id' : staff_id_past,
                    'total_players_number' : total_players_number_past
                    }
    
    tournaments_dict_future = {'tournament_id' : tournament_id[tournaments_past:],
                    'name' : new_names[tournaments_past:],
                    'date' : date_future,
                    'game_id' : game_id[tournaments_past:],
                    'team_players_number' : team_players_number[tournaments_past:],
                    'staff_id' : staff_id_future,
                    'total_players_number' : total_players_number_future
                    }
    
    past_df = pd.DataFrame(tournaments_dict_past)
    future_df = pd.DataFrame(tournaments_dict_future)
    total_df = pd.concat([past_df,future_df])
    return total_df
