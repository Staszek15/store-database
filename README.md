# Gamestalgia
# Authors
### Wiktoria Fimińska, Julia Grzegorzewska, Mateusz Stasiak, Karolina Wypych

- ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) `#pink`
- ![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) `#c5f015`
- ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `#1589F0`

  
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
- **knitr**
This tool was applied to generate a report.

# Files 
Every underlined *.csv* file contains a complete dataset that later is used to fill a table of a similar name. 
All underlined *.py* files consist of functions that generate data, process it and return as a dataframe. (e.g. *address.py* provides data for table *address*, *customer_rental.py* for table *customers* and table *rentals*.) 
* **generate_data:**
    -   connection.py
    -   const.py
    -   create_tables.sql
    -   foreign_keys.sql
    -   main_execute.ipynb
    -   main_execute.py
  
    - **address**
      -  <ins>address.py</ins>
      -  <ins>address.csv</ins>
      -   postal_codes.csv
         
    - **analysis**
      -   plots.py
      -   plot_registrations.png
      -   plot_rentals.png
           
    - **create_staff_schedule**
       -  <ins>create_staff_schedule.py<ins>
       -  <ins>staff_schedule.csv</ins> 

    - **customer_rental**
      -  <ins>customer_rental.py</ins>
      -  <ins>customers.csv</ins> 
      -  <ins>rentals.csv</ins> 
 
    - **game**
      -   <ins>game.py</ins>
      -  <ins>game.csv</ins> 
      -   all_games.xlsx
      -   games_dataset.csv
      -   selected_games.xlsx

    - **inventory_buy_purchase**
      -   <ins>inventory_buy_purchase.py</ins>
      -   inventory_buy, purchase.ipynb
      -  <ins>inventory_buy.csv</ins> 
      -  <ins>purchases.csv</ins>
      -   purchases.csv
  
    - **inventory_rent**
      -  <ins>inventory_rent.py</ins>
      -  <ins>inventory_rent.csv</ins>

    - **staff**
      -   <ins>staff.py</ins>
      -  <ins>staff.csv</ins>
          
    - **tournament**
      -   <ins>tournament.py</ins>
      -   tournament.ipynb
      -  <ins>tournaments.csv</ins>
           
    - **tournament_rental_consistency**
      -   tournament_rental_consistency.py
          
    - **tournament_results**
      -   <ins>tournament_results.py</ins>
      -   tournament_results.ipynb
      -  <ins>tournament_results.csv</ins>

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

