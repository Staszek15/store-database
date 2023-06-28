import pandas as pd
from datetime import datetime, timedelta
import random


def generate_dates():
    """
    Generate daily dates during the store's working period.
    """
    dates = []
    start_date = datetime(2021, 1, 4)
    end_date = datetime(2023, 6, 15)
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    df_dates = pd.DataFrame({'dates': dates})
    return df_dates


def create_staff_schedule(free_days):
    """
    Generate staff schedule for all dates during store's working period.
    """
    days = generate_dates()['dates']
    staff_id = []
    for day in days:
        # in non-working days only manager can work
        if day.weekday() == 6 or day < datetime(2021, 1, 20) or str(day) in free_days:
            ids = [1]
            staff_id.append({'date': day, 'staff_ids': ids})
        # consider employee's start date and from available employees draw some of them
        elif datetime(2021, 4, 8) > day >= datetime(2021, 1, 20):
            ids = random.sample([1, 2], random.choice([1, 2]))
            staff_id.append({'date': day, 'staff_ids': ids})
        elif datetime(2021, 11, 26) > day >= datetime(2021, 4, 8):
            ids = random.sample([1, 2, 3], random.choice([1, 2]))
            staff_id.append({'date': day, 'staff_ids': ids})
        elif datetime(2022, 2, 7) > day >= datetime(2021, 11, 26):
            ids = random.sample([1, 2, 3, 4], random.choice([1, 2, 3]))
            staff_id.append({'date': day, 'staff_ids': ids})
        elif day >= datetime(2022, 2, 7):
            ids = random.sample([1, 2, 3, 4, 5], random.choice([1, 2, 3]))
            staff_id.append({'date': day, 'staff_ids': ids})
    staff_schedule = pd.DataFrame(staff_id)
    return staff_schedule
