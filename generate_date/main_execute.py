from generate_date.staff.staff import *
from generate_date.inventory_rent.inventory_rent import *

if __name__ == "__main__":
    #address
    generate_staff().to_csv('staff/staff.csv')
    #create_staff_schedule
    #game
    generate_inventory_rent().to_csv('inventory_rent/inventory_rent.csv')
    #customer, rental
    #inventory_buy, purchase
    #tournament
    #tournament_results
