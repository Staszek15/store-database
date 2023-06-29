import pandas as pd

def remove_rentals(tournament_df, rental):
    
    tournament_df['tuple'] = tournament_df.apply(lambda row: (row['game_id'], row['date']), axis=1)
    
    for element in tournament_df.tuple:
        id = element[0]
        date = element[1]
        rental['rental_date'] = pd.to_datetime(rental['rental_date'])
        rental['return_date'] = pd.to_datetime(rental['return_date'])
        mask = (rental['game_id'] == id) & (rental['rental_date'] < date) & (rental['return_date'] > date)
        rental.loc[mask, 'return_date'] = date
        
    return(rental)