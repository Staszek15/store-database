import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.dates as mdates


def generate_registrations_plot():
    sns.set(rc={'figure.figsize':(12,7)})

    customers = pd.read_csv('../generate_data/customer_rental/customers.csv')
    registrations = pd.to_datetime(customers['registration_date'], format = '%Y-%m-%d')

    sns.histplot(registrations, stat="count", kde=True, bins=50)
    plt.xlabel("date")
    plt.xticks(rotation=45)
    plt.ylabel("number of registrations")
    plt.tight_layout()
    plt.savefig("analysis/plot_registrations.png")
    plt.clf()



def generate_rentals_plot():
    sns.set(rc={'figure.figsize':(12,7)})

    df_rentals = pd.read_csv('../generate_data/customer_rental/rentals.csv')
    dates = pd.to_datetime(df_rentals['rental_date'], format = '%Y-%m-%d')

    sns.histplot(dates, stat="count", kde=True, bins=50)
    plt.xlabel("date")
    plt.xticks(rotation=45)
    plt.ylabel("number of rentals")
    plt.tight_layout()
    plt.savefig("analysis/plot_rentals.png")
    plt.clf()



if __name__ == "__main__":
    generate_registrations_plot()
    generate_rentals_plot()
