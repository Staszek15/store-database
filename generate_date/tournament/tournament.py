import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta
import matplotlib.pyplot as plt



def generate_dates():
    
    number = np.random.randint(1,125)
    if number%3 == 2:
        period = number * 7
    elif number%3 == 1:
        period = number * 7 + 3
    else:
        period = number * 7 + 6
        
    start = datetime.strptime('2021-04-07', "%Y-%m-%d")
    tournament_date = start + timedelta(days=period)
    
    free_days = ['2023-01-01', '2023-01-06', '2023-04-09', '2023-04-10', '2023-05-01', '2023-05-03', '2023-05-28', '2023-06-08',
            '2022-01-01', '2022-01-06', '2022-04-17', '2022-04-18', '2022-05-01', '2022-05-03', '2022-06-05', '2022-06-16',
            '2022-08-15', '2022-11-01', '2022-11-11', '2022-12-25', '2022-12-26', '2021-01-06', '2021-04-04', '2021-04-05',
            '2021-05-01', '2021-05-03', '2021-05-23', '2021-06-03', '2021-08-15', '2021-11-01', '2021-11-11', '2021-12-25',
            '2021-12-26']

    if tournament_date in free_days:
        tournament_date = start + timedelta(days=4)

    return(tournament_date.strftime("%Y-%m-%d"))
    
    
    
def generate_tournament_staff(tournament_date, staff_table):
    
    staff_list = []
    staff_table.start = pd.to_datetime(staff_table.start)
    tournament_date = pd.to_datetime(tournament_date)
    
    for d in tournament_date:
        available_staff = staff_table.staff_id[staff_table.start < d].values
        if d.weekday() == 6:
            staff_list.extend([1])
        else:
            staff_list.extend([np.random.choice(available_staff)])
            
    return staff_list



def generate_total_players(table_game,game_id):
    
    inventory_table = pd.read_csv('inventory_rent/inventory_rent.csv')
    
    games_number = inventory_table.game_id.value_counts()
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



def generate_tournament():
    
    games_csv = pd.read_csv('game/game.csv')
    staff_csv = pd.read_csv('staff/staff.csv')

    name = ['Cosmic Entertainment', 'Battlefields of Bonaparte', 'The Kobolds', 'Gaming Evening', 'Hamst&Furious', 'Indian Camp', 'Vietgame',
             'Thematic Contest', 'Spring Tournament', 'Star Trek Day']
    n = len(name)
    tournament_id = np.arange(1,n+1)
    game_id = [9,27,33,33,7,5,36,6,1,19]
    date = np.sort([generate_dates() for _ in range(n)])
    
    team_players_number = [games_csv.max_players_in_team[games_csv.game_id == i].values[0] for i in game_id]
    total_players_number = generate_total_players(games_csv, game_id)
    
    max_staff = staff_csv.staff_id.max()
    #staff_id = [np.random.randint(1,max_staff+1) for _ in range(n)]
    staff_id = generate_tournament_staff(date,staff_csv) 
    
    tournaments_dict = {'tournament_id' : tournament_id,
                    'name' : name,
                    'date' : date,
                    'game_id' : game_id,
                    'team_players_number' : team_players_number,
                    'staff_id' : staff_id,
                    'total_players_number' : total_players_number
}
    tournaments_df = pd.DataFrame(tournaments_dict)
    tournaments_df.to_csv('tournament/tournament.csv', index = False)
    return(tournaments_df)

if __name__ == '__main__':
    generate_tournament()