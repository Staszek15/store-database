from staff.staff import *
from inventory_rent.inventory_rent import *
from address.address import *
from const import *


if __name__ == "__main__":
    generate_address().to_csv('address/address.csv')
    generate_staff().to_csv('staff/staff.csv')
    #create_staff_schedule
    #game
    generate_inventory_rent(games_rent_prices, pd.read_csv('game/game.csv')).to_csv('inventory_rent/inventory_rent.csv')
    #customer, rental
    inv_rent = pd.read_csv('inventory_rent/inventory_rent.csv')
    rental = pd.read_csv('customer_rental/rental.csv')
    check_if_rent_available(inv_rent, rental).to_csv('inventory_rent/inventory_rent.csv')
    #inventory_buy, purchase
    #tournament
    #tournament_results
