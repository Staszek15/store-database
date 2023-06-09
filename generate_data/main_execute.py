from staff.staff import *
from inventory_rent.inventory_rent import *
from address.address import *
from inventory_buy_purchase.inventory_buy_purchase import *
from customer_rental.customer_rental import *
from game.game import *
from create_staff_schedule.create_staff_schedule import *
from const import *
from customer_rental.customer_rental import *
from tournament.tournament import *
from tournament_results.tournament_results import *
from tournament_rental_consistency.tournament_rental_consistency import *
from connection import *


def main():

    generate_address(pd.read_csv('address/postal_codes.csv', encoding='UTF-8',
                                 delimiter=';')).to_csv('address/address.csv', index=False)
    generate_staff().to_csv('staff/staff.csv', index=False)
    create_staff_schedule(free_days).to_csv('create_staff_schedule/staff_schedule.csv', index=False)
    staff_schedule = pd.read_csv('create_staff_schedule/staff_schedule.csv')
    generate_game().to_csv('game/game.csv', index=False)
    games = pd.read_csv('game/game.csv')
    generate_inventory_rent(games_rent_prices_dict, games).to_csv('inventory_rent/inventory_rent.csv', index=False)
    rentals, customers = generate_customers_rentals(n, start_date, end_date, days_number, games_rent_prices,
                                                    pd.read_csv('inventory_rent/inventory_rent.csv'),
                                                    games, staff_schedule)
    rentals.to_csv('customer_rental/rentals.csv', index=False)
    customers.to_csv('customer_rental/customers.csv', index=False)

    generate_tournament(games, pd.read_csv('inventory_rent/inventory_rent.csv'),
                        staff_schedule).to_csv('tournament/tournaments.csv', index=False)
    generate_tournament_results(pd.read_csv('tournament/tournaments.csv'),
                                pd.read_csv('customer_rental/customers.csv'),
                                games).to_csv('tournament_results/tournament_results.csv', index=False)
    
    remove_rentals(pd.read_csv('tournament/tournaments.csv'), 
                   pd.read_csv('customer_rental/rentals.csv')).to_csv('customer_rental/rentals.csv', index=False)

    rental = pd.read_csv('customer_rental/rentals.csv')
    
    check_if_rent_available(pd.read_csv('inventory_rent/inventory_rent.csv'),
                            rental).to_csv('inventory_rent/inventory_rent.csv', index=False)
    inventory_buy, purchases = generate_inventory_buy_purchase(games, pd.read_csv('customer_rental/customers.csv'),
                                                               staff_schedule, games_buy_prices, start_date, end_date)
    inventory_buy.to_csv('inventory_buy_purchase/inventory_buy.csv', index=False)
    purchases.to_csv('inventory_buy_purchase/purchases.csv', index=False)


    connect()





if __name__ == "__main__":
    main()

    
