import pandas as pd
import numpy as np
from datetime import date, timedelta
import random
from dateutil.relativedelta import relativedelta
import faker
from ast import literal_eval


def get_dates_between(start_date, days_number):
    """
    Generates random date between start_date and date wchich is days_number after the store opening.
    :param start_date: opening date of our store
    :param days_number: how many days have passed since the store opening
    """
    return [start_date + timedelta(days = i) for i in range(days_number)]


def registration_probability(days_number):
    """
    Generates vector of probabilities which simulates the real development of the store. The vector is a descending series converging to 1.
    :param days_number: how many days have passed since the store opening
    """
    n = days_number

    series = []
    for _ in range(n - 1):
        xi = random.uniform(0, 1)
        series.append(xi)

    series.sort(reverse=True)  # sort descending
    scaling_factor = 1 / sum(series)
    series = [x * scaling_factor for x in series]

    remaining_sum = abs(1 - sum(series))
    series.append(remaining_sum)

    return series


def create_customers():
    """
    Generates one customer in the following format: first name, last name, email. Customers can be Polish, German, Czech or Ukrainian with the respective probabilities.
    """
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
    """
    Generates a random email body (characters before @) for provided first and last name of the customer.
    :param first_name: customer first name 
    :param last_name: customer last name 
    """
    if " " in first_name:
        first_name = first_name.split(" ")[0]
    email = first_name[0: random.randint(2, len(first_name) - 1)] + last_name[0: random.randint(2, len(last_name) - 1)]
    email += str(random.choices(['', random.randint(0, 100)], weights=[0.4, 0.6])[0])
    return email


def days_from_last_rent(return_date, start_date):
    """
    Generates a random number that indicates how many days passed since the last return of rental. 
    Probabilities in random choice are based on given density function and depend on how many days passed since the opening of the store. The more days, the bigger chance for short break in rentals.
    :param start_date: opening date of our store
    :param start_date: opening date of our store
    """
    diff_date = (return_date - start_date).days
    x = 0.6 / (1 + np.e ** (-0.01005 * (diff_date - 300)))
    possible_days = [0, np.random.randint(1, 9), np.random.randint(10, 21), np.random.randint(22, 41),
                     np.random.randint(42, 120)]
    prob = [0.02, x, 0.75 - 3 * x / 4, 0.22 - x / 4, 0.01]

    return int(np.random.choice(possible_days, p=prob))


def rent_days():
    """
    Generates a random number that indicates how many days did the rental last. 
    Function can return 0 because customer can rent a game, play it in the store and return afterwards.
    """
    possible_days = [0, np.random.randint(1,8), np.random.randint(8,14), np.random.randint(15,31),
                     np.random.randint(31, 61), np.random.randint(61, 121), np.random.randint(121, 672)]
    prob = [0.2, 0.5, 0.2, 0.05, 0.03, 0.017, 0.003]
    return int(np.random.choice(possible_days, p = prob))


def generate_customers_rentals(n, start_date, end_date, days_number, games_rent_prices, inventory_rent, games, staff_id):
    """
    Generates and returns customers and rentals dataframes with all the information.
    :param n: number of clients
    :param start_date: opening date of our store
    :param end_date: last day to include while generating data
    :param days_number: how many days have passed since the store opening
    :param games_rent_prices: dictionary with rental prices for every game
    :param inventory_rent: inventory_rent dataframe
    :param games: games dataframe
    :param staff_id: id of a staff member in our store
    """
    fake = faker.Faker('pl_PL')

    registration_dates = [start_date] * 15 + [start_date + timedelta(days=1)] * 10 + [
        start_date + timedelta(days=2)] * 5 + [
                             random.choices(get_dates_between(start_date,days_number),
                                            weights=registration_probability(days_number))[0] for _ in
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
            i, "email"] = create_customers()

    df_customers = df_customers.sort_values(by="registration_date")
    df_customers['customer_id'] = [_ + 1 for _ in range(n)]

    ###################################################

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
            customer_id = random.choice(np.arange(1, len(df_customers) + 1))
            wiek = relativedelta(rental.iloc[i]['rental_date'], df_customers['birthdate'][customer_id - 1],
                                 '%Y-%m-%d').years
            if (wiek > games.loc[games['game_id'] == rental.iloc[i]['game_id'], 'min_age'].values and
                    df_customers['registration_date'][customer_id - 1] <= rental.iloc[i]['rental_date'].date()):
                cst_id.append(customer_id)
                break
            else:
                continue

    rental['customer_id'] = cst_id

    staff_id['staff_ids'].iloc[staff_id[(staff_id['date'] == "2023-06-11")].index[0]]
    staff_id.loc[:, 'staff_ids'] = staff_id.loc[:, 'staff_ids'].apply(lambda x: literal_eval(x))

    staff_id_ = []
    # choosing randomly who will sell the item
    for i in rental['rental_date']:
        staff_id_.append(random.choice(
            (staff_id['staff_ids'].iloc[staff_id[(staff_id['date'] == i.strftime('%Y-%m-%d'))].index[0]])))
    rental["staff_id"] = staff_id_

    ############################################

    temp = {
        'customer_id': [i + 1 for i in range(n)],
        'count': [0] * n
    }

    df_temp = pd.DataFrame(temp)

    for i in range(len(rental)):
        client_id = rental["customer_id"][i]

        df_temp.at[client_id - 1, "count"] = df_temp["count"][client_id - 1] + 1

        if df_temp["count"][client_id - 1] == 10:
            df_temp.at[client_id - 1, "date"] = rental["return_date"][i]

    df_customers['VIP'] = df_temp['date']

    ###############################################

    main_price = []
    for i in range(0, len(rental)):
        if pd.isnull(df_customers.loc[df_customers['customer_id'] == rental.iloc[i]['customer_id'], 'VIP'].values[0]):
            main_price.append(games_rent_prices.loc[
                                  games_rent_prices['game_id'] == str(rental.iloc[i]['game_id']), 'rent_price'].values[
                                  0])
        elif (df_customers.loc[df_customers['customer_id'] == rental.iloc[i]['customer_id'], 'VIP'].values[0] >
              np.datetime64(rental.iloc[i]['rental_date'])):
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

    return rental, df_customers

