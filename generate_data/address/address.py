import random
import pandas as pd
import numpy as np
from faker import Faker
from bs4 import BeautifulSoup
import requests


def generate_address(df_all, n=605):
    """
    Generate data for address table.
    """
    #setting address region
    fake = Faker('pl_PL')

    # data scrapping for dolnoslaskie region
    url = 'https://www.kody-pocztowe.dokladnie.com/okreg5.php'
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    scrapped = soup.select('#page-table td:nth-child(1) , #page-table td:nth-child(3)')

    # cleaning tags
    clean_data = [d.text.lstrip('<td>').rstrip('</td>') for d in scrapped]

    # getting city name and postal code
    postal = []
    city = []
    for idx, element in enumerate(clean_data[2:]):
        if idx % 2 == 0:
            postal.append(element)
        else:
            city.append(element)

    df = pd.DataFrame({'postal_code': postal, 'city': city})
    df_dolnoslaskie = df[df['city'] != 'Wrocław']
    df_wro = df[df['city'] == 'Wrocław']

    # not dolnoslaskie region
    df_rest = df_all[['KOD POCZTOWY', 'MIEJSCOWOŚĆ']]
    df_rest[df_rest['KOD POCZTOWY'].str[0] != "5"]

    arr = np.random.choice((1,2,3), (n,), p=(0.6, 0.3, 0.1))
    postal = []
    for i in arr:
        if i == 1:
            postal_code = random.choice(df_wro['postal_code'])
        elif i == 2:
            postal_code = random.choice(df_dolnoslaskie['postal_code'].values)
        else:
            postal_code = random.choice(df_rest['KOD POCZTOWY'].values)
        postal.append(postal_code)

    # generated data
    temp = pd.DataFrame({'KOD POCZTOWY': postal})
    temp = temp.merge(df_all[['KOD POCZTOWY', 'MIEJSCOWOŚĆ']].drop_duplicates(subset="KOD POCZTOWY"), how='left', on='KOD POCZTOWY')

    temp['ADRES'] = [fake.street_name() + " " + fake.building_number() for _ in range(len(temp))]
    temp = temp.sort_values('KOD POCZTOWY')
    temp = temp.sample(frac=1).reset_index(drop=True)
    temp['address_id'] = [i for i in range(1, n + 1)]

    temp.columns = ['postal_code', 'city', 'address', 'address_id']
    temp[['address_id', 'address', 'city', 'postal_code']]

    return temp

