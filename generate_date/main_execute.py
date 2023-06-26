from staff.staff import *
from inventory_rent.inventory_rent import *
from address.address import *
from const import *


if __name__ == "__main__":
    generate_address().to_csv('address/address.csv')
    generate_staff().to_csv('staff/staff.csv')
    #create_staff_schedule
    #game
    generate_inventory_rent(games_rent_prices).to_csv('inventory_rent/inventory_rent.csv')
    #customer, rental
    #inventory_buy, purchase
    #tournament
    #tournament_results
