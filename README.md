# Gamestalgia
# Authors
### Wiktoria Fimińska, Julia Grzegorzewska, Mateusz Stasiak, Karolina Wypych

# Table of contents
* [Introduction](#introduction)
* [Description](#description)
* [Technologies](#technologies)
* [How to run a program](#running)

# Introduction <a name="introduction"></a>
These days in the fast changing world we are inundated with big volumes of data. It provokes higher demand for people specialized in processing it. A vast majority of companies and institutions could not work without efficient databases systems what makes an ability of creating and maintaining them a valuable skill. To gain it we developed a project during databases course at Wroclaw University of Science and Technology.

<p align="center">
  <img src="https://github.com/Staszek15/store-database/blob/main/logo_store.png" width=80%>
</p>

# Description <a name=description></a>
The project generally consists of generating a database and a report for Gamestalgia - a fictional board games rental store. Gamestalgia is a unique place. Not only does it rent games but also sells them and organize tournaments. Moreover, the most active customers are rewarded with a VIP status and hence extra discounts on rentals and purchases.

<p align="center">
  <img src="https://github.com/Staszek15/store-database/blob/main/database_schema.png" width=80%>
</p>

# Technologies <a name=technnologies></a>
Making this project involved using following technologies:
- **Python**
It was applied to generate data for all tables. All dependencies between them were taken into consideration to provide a data integrity. Then Python was used for filling the database with valules generated previously.
- **MySQL**
It was used for creating the database schema and analysing data.
- ** rmd **
This tool was applied to generate a report.

# Files       
* **generate_data:**
    -   connection.py
    -   const.py
    -   create_tables.sql
    -   foreign_keys.sql
    -   main_execute.ipynb
    -   main_execute.py
    -   
    - **address**
       -   address.csv
       -   address.py
       -   postal_codes.csv
       -   
         
    - **analysis**
      -   plots.py
      -   plot_registrations.png
      -   plot_rentals.png
           
    - **create_staff_schedule**
       -   create_staff_schedule.py
       -   staff_schedule.csv
        
    - **customer_rental**
      -   customers.csv
      -   customer_rental.py
      -   rentals.csv
          
    - **game**
      -   all_games.xlsx
      -   game.csv
      -   game.py
      -   games_dataset.csv
      -   selected_games.xlsx

    - **inventory_buy_purchase**
      -   inventory_buy, purchase.ipynb
      -   inventory_buy.csv
      -   inventory_buy_purchase.py
      -   purchase.csv
      -   purchases.csv
  
    - **inventory_rent***
      -   inventory_rent.csv
      -   inventory_rent.py
      -   

    - **staff**
      -   staff.csv
      -   staff.py
          
    - **tournament**
      -   tournament.ipynb
      -   tournament.py
      -   tournaments.csv
           
    - **tournament_rental_consistency**
      -   tournament_rental_consistency.py
    -       
    - **tournament_results**
      -   tournament_results.csv
      -   tournament_results.ipynb
      -   tournament_results.py

# How to run a program <a name=running></a>
**on Windows** 
1. clone repository
` git clone https://github.com/Staszek15/store-database.git`
2. using console move to repository directory on your device and install necessary packages e.g in a virtual environment
 `python -m venv venv` 
 `venv\Scripts\activate.bat` 
 `pip install -r requirements.txt`
3. run a program
`python main_execute.py`

