import pandas as pd

"""
Any resemblance to real persons or names is coincidental.
"""

def generate_staff():
    data = {'staff_id': [1, 2, 3, 4, 5],
            'first_name': ['Tomasz', 'Wiktoria', 'Karolina', 'Julia', 'Mateusz'],
            'last_name': ['Stroiński', 'Fimińska', 'Wypych', 'Grzegorzewska', 'Stasiak'],
            'salary': [5000, 3500, 3500, 3500, 3500],
            'birthdate': ['1995-01-01', '2001-02-02', '2001-09-03', '2001-09-03', '2001-10-15'],
            'start': ['2021-01-04', '2021-01-20', '2021-04-08', '2021-11-26', '2022-02-07'],
            'phone': ['923128647', '756837957', '567938928', '566552356', '666555827'],
            'address_id': [1, 2, 3, 4, 5],
            'email': ['t.stroinski@geeksdragons.com', 'w.fiminska@geeksdragons.com', 'k.wypych@geeksdragons.com',
                      'j.grzegorzewska@geeksdragons.com', 'm.stasiak@geeksdragons.com']
            }

    staff = pd.DataFrame(data)
    return staff

