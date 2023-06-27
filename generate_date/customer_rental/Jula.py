import pandas as pd
import numpy as np
from datetime import date, timedelta
import random
from dateutil.relativedelta import relativedelta
import faker
from ast import literal_eval

free_days = ['2023-01-01', '2023-01-06', '2023-04-09', '2023-04-10', '2023-05-01', '2023-05-03', '2023-05-28', '2023-06-08',
            '2022-01-01', '2022-01-06', '2022-04-17', '2022-04-18', '2022-05-01', '2022-05-03', '2022-06-05', '2022-06-16',
            '2022-08-15', '2022-11-01', '2022-11-11', '2022-12-25', '2022-12-26', '2021-01-06', '2021-04-04', '2021-04-05',
            '2021-05-01', '2021-05-03', '2021-05-23', '2021-06-03', '2021-08-15', '2021-11-01', '2021-11-11', '2021-12-25',
            '2021-12-26']




def get_dates_between(start_date, days_number):
    return [start_date + timedelta(days = i) for i in range(days_number)]


def prawdopodobienstwa_rejestracja(days_number):
    n = days_number

    series = []
    for _ in range(n - 1):
        xi = random.uniform(0, 1)
        series.append(xi)

    series.sort(reverse=True)  # Sortowanie malejące
    scaling_factor = 1 / sum(series)
    series = [x * scaling_factor for x in series]

    remaining_sum = abs(1 - sum(series))  # tu teoretycznie przekrocze 1 w wektorze prawd ale na dalekim miejscu po przecinku
    series.append(remaining_sum)

    return series


def generate_customer():
    fake = faker.Faker('pl_PL')

    country_probabilities = [0.78, 0.08, 0.04, 0.1]
    email_endings_pl = ["@gmail.com", "@wp.pl", "@o2.pl", "@live.com"]
    email_endings_de = ["@gmail.com", "@web.de", "@gmx.net", "@live.com"]
    email_endings_cs = ["@gmail.com", "@szn.cz", "live.com"]
    email_endings_uk = ["@gmail.com", "@mail.ru", "@live.com"]

    countries = ["Poland", "Germany", "Czech Republic", "Ukraine"]
    country = random.choices(countries, weights=country_probabilities)[0]

    if country == "Poland":
        fake = faker.Faker('pl_PL')
        if random.random() < 0.5:
            x = fake.first_name_female()
            y = fake.last_name_female()
            email = generate_email(x, y) + random.choice(email_endings_pl)
            return x, y, email
        else:
            x = fake.first_name_male()
            y = fake.last_name_male()
            email = generate_email(x, y) + random.choice(email_endings_pl)
            return x, y, email

    elif country == "Germany":
        fake = faker.Faker('de_DE')
        if random.random() < 0.5:
            x = fake.first_name_female()
            y = fake.last_name_female()
            email = generate_email(x, y) + random.choice(email_endings_de)
            return x, y, email
        else:
            x = fake.first_name_male()
            y = fake.last_name_male()
            email = generate_email(x, y) + random.choice(email_endings_de)
            return x, y, email

    elif country == "Czech Republic":
        fake = faker.Faker('cs_CZ')
        if random.random() < 0.5:
            x = fake.first_name_female()
            y = fake.last_name_female()
            email = generate_email(x, y) + random.choice(email_endings_cs)
            return x, y, email
        else:
            x = fake.first_name_male()
            y = fake.last_name_male()
            email = generate_email(x, y) + random.choice(email_endings_cs)
            return x, y, email

    elif country == "Ukraine":
        fake = faker.Faker('uk_UA')
        if random.random() < 0.5:
            x = fake.first_name_female()
            y = fake.last_name_female()
            email = generate_email(x, y) + random.choice(email_endings_uk)
            return x, y, email
        else:
            x = fake.first_name_male()
            y = fake.last_name_male()
            email = generate_email(x, y) + random.choice(email_endings_uk)
            return x, y, email

def generate_email(first_name, last_name):
    if " " in first_name:
        first_name = first_name.split(" ")[0]
    email = first_name[0: random.randint(2, len(first_name) - 1)] + last_name[0: random.randint(2, len(last_name) - 1)]
    email += str(random.choices(['', random.randint(0, 100)], weights=[0.4, 0.6])[0])
    return email


def days_from_last_rent(return_date, start_date):
    diff_date = (return_date - start_date).days
    x = 0.6 / (1 + np.e ** (-0.01005 * (diff_date - 300)))
    possible_days = [0, np.random.randint(1, 9), np.random.randint(10, 21), np.random.randint(22, 41),
                     np.random.randint(42, 120)]
    prob = [0.02, x, 0.75 - 3 * x / 4, 0.22 - x / 4, 0.01]

    return int(np.random.choice(possible_days, p=prob))

# 0 bo moga przyjsc pograc na miejscu i od razu oddac
def rent_days():
    possible_days = [0, np.random.randint(1,8), np.random.randint(8,14), np.random.randint(15,31),
                     np.random.randint(31, 61), np.random.randint(61, 121), np.random.randint(121, 672)]
    prob = [0.2, 0.5, 0.2, 0.05, 0.03, 0.017, 0.003]
    return int(np.random.choice(possible_days, p = prob))


def generate_rentals(n, start_date, end_date, days_number, games_buy_prices):
    fake = faker.Faker('pl_PL')

    registration_dates = [start_date] * 15 + [start_date + timedelta(days=1)] * 10 + [
        start_date + timedelta(days=2)] * 5 + [
                             random.choices(get_dates_between(start_date,days_number), weights=prawdopodobienstwa_rejestracja(days_number))[0] for _ in
                             range(n - 30)]
    random.shuffle(registration_dates)

    customers = {

        'first_name': ["s" for _ in range(n)],
        'last_name': ["a" for _ in range(n)],
        'birthdate': [fake.date_of_birth(minimum_age=13, maximum_age=80) for _ in range(n)],
        'email': ["s" for _ in range(n)],
        'phone': [random.randint(100000000, 999999999) for _ in range(n)],
        'address_id': random.sample([i for i in range(n)], n),
        'registration_date': registration_dates
    }

    df_customers = pd.DataFrame(customers)

    for i in range(n):
        df_customers.at[i, "first_name"], df_customers.at[i, "last_name"], df_customers.at[
            i, "email"] = generate_customer()

    df_customers = df_customers.sort_values(by="registration_date")
    df_customers['customer_id'] = [_ + 1 for _ in range(n)]

    ###################################################3
    ###############################################3

    inventory_rent = pd.read_csv("inventory_rent/inventory_rent.csv")
    games = pd.read_csv('game/game.csv')

    customers = df_customers
    inventory_id = inventory_rent['inventory_id']

    rental = pd.DataFrame(columns=['inventory_id', 'rental_date', 'return_date', 'game_id'])
    for i in inventory_id:
        return_date = start_date

        while return_date < end_date:
            rental_date = return_date + timedelta(days=days_from_last_rent(return_date, start_date))
            return_date = rental_date + timedelta(days=rent_days())
            if rental_date <= end_date:
                if return_date > end_date:
                    new_return_date = None
                    new_row = {'inventory_id': i, 'rental_date': rental_date, 'return_date': new_return_date,
                               'game_id': int(
                                   inventory_rent.loc[inventory_rent['inventory_id'] == i, 'game_id'].values)}
                    rental.loc[len(rental)] = new_row
                else:
                    new_row = {'inventory_id': i, 'rental_date': rental_date, 'return_date': return_date,
                               'game_id': int(
                                   inventory_rent.loc[inventory_rent['inventory_id'] == i, 'game_id'].values)}
                    rental.loc[len(rental)] = new_row

    rental['rental_date'] = pd.to_datetime(rental['rental_date'])
    rental['return_date'] = pd.to_datetime(rental['return_date'])
    rental = rental.sort_values(by='rental_date')
    rental['rental_id'] = np.arange(1, len(rental) + 1)
    rental = rental.iloc[:, [4, 0, 1, 2, 3]]

    cst_id = []
    for i in range(0, len(rental)):
        cont = True
        while cont:
            customer_id = random.choice(np.arange(1, len(customers) + 1))
            wiek = relativedelta(rental.iloc[i]['rental_date'], customers['birthdate'][customer_id - 1], '%Y-%m-%d').years
            if (wiek > games.loc[games['game_id'] == rental.iloc[i]['game_id'], 'min_age'].values and
                    customers['registration_date'][customer_id - 1] <= rental.iloc[i]['rental_date'].date()):
                cst_id.append(customer_id)
                break
            else:
                continue

    rental['customer_id'] = cst_id

    staff_id = pd.read_csv('create_staff_schedule\staff_schedule.csv', index_col=[0])
    staff_id['staff_ids'].iloc[staff_id[(staff_id['date'] == "2023-06-11")].index[0]]
    staff_id.loc[:, 'staff_ids'] = staff_id.loc[:, 'staff_ids'].apply(lambda x: literal_eval(x))

    staff_id_ = []
    # choosing randomly who will sell the item
    for date in rental['rental_date']:
        staff_id_.append(random.choice(
            (staff_id['staff_ids'].iloc[staff_id[(staff_id['date'] == date.strftime('%Y-%m-%d'))].index[0]])))
    rental["staff_id"] = staff_id_
    ##############
    ##############
    temp = {
        'customer_id': [i + 1 for i in range(n)],
        'count': [0] * n
    }

    df_temp = pd.DataFrame(temp)

    df_temp

    for i in range(len(rental)):
        client_id = rental["customer_id"][i]

        df_temp.at[client_id - 1, "count"] = df_temp["count"][client_id - 1] + 1

        if df_temp["count"][client_id - 1] == 10:
            df_temp.at[client_id - 1, "date"] = rental["return_date"][i]
    df_customers['VIP'] = df_temp['date']

    ####################
    #######################

    games_rent_prices_dict = {game_id: round(buy_price/15, 2) for game_id, buy_price in games_buy_prices.items()}
    games_rent_prices = pd.DataFrame(games_rent_prices_dict.items(), columns=['game_id', 'rent_price'])

    main_price = []
    for i in range(0, len(rental)):
        if pd.isnull(df_customers.loc[df_customers['customer_id'] == rental.iloc[i]['customer_id'], 'VIP'].values[0]):
            main_price.append(games_rent_prices.loc[
                                  games_rent_prices['game_id'] == str(rental.iloc[i]['game_id']), 'rent_price'].values[
                                  0])
        elif df_customers.loc[df_customers['customer_id'] == rental.iloc[i]['customer_id'], 'VIP'].values[
            0] > np.datetime64(rental.iloc[i]['rental_date']):
            main_price.append(games_rent_prices.loc[
                                  games_rent_prices['game_id'] == str(rental.iloc[i]['game_id']), 'rent_price'].values[
                                  0])
        else:
            main_price.append(games_rent_prices.loc[
                                  games_rent_prices['game_id'] == str(rental.iloc[i]['game_id']), 'rent_price'].values[
                                  0] * 0.9)

    rental['price'] = main_price

    fine = []
    for i in range(0, len(rental)):
        if pd.isnull(rental.iloc[i]['return_date']):
            fine.append(None)
        elif relativedelta(rental.iloc[i]['return_date'], rental.iloc[i]['rental_date'], '%Y-%m-%d').days <= 7:
            fine.append(0)
        else:
            delay_days = relativedelta(rental.iloc[i]['return_date'], rental.iloc[i]['rental_date'],
                                       '%Y-%m-%d').days - 7
            fine.append(round(delay_days * 0.1 * rental.iloc[i]['price'], 2))

    rental['fine'] = fine

    rental.to_csv('rental.csv')
    df_customers.to_csv("customer.csv", index=False)

    return rental, df_customers

