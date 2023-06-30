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
Every bolded *.csv* file contains a complete dataset that later is used to fill a table of the same name. 
All <span style="color:yellow">yellow</span> *.py* files consist of functions that generate data, process it and return as a dataframe. (e.g. *address.py* provides data for table *address*, *customer_rental.py* for table *customers* and table *rentals*.) 
* **generate_data:**
    -   connection.py
    -   const.py
    -   create_tables.sql
    -   foreign_keys.sql
    -   main_execute.ipynb
    -   main_execute.py
  
    - **address**
      -   <ins>address.py</ins>
      -  <span style="color:pink">address.csv</span>
      -   postal_codes.csv
         
    - **analysis**
      -   plots.py
      -   plot_registrations.png
      -   plot_rentals.png
           
    - **create_staff_schedule**
       -  create_staff_schedule.py
       -  <span style="color:pink">staff_schedule.csv</span> 

    - **customer_rental**
      -  <span style="color:yellow">customer_rental.py</span>
      -  <span style="color:pink">customers.csv</span> 
      -  <span style="color:pink">rentals.csv</span> 
 
    - **game**
      -   <span style="color:yellow">game.py</span>
      -  <span style="color:pink">game.csv</span> 
      -   all_games.xlsx
      -   games_dataset.csv
      -   selected_games.xlsx

    - **inventory_buy_purchase**
      -   <span style="color:yellow">inventory_buy_purchase.py</span>
      -   inventory_buy, purchase.ipynb
      -  <span style="color:pink">inventory_buy.csv</span> 
      -  <span style="color:pink">purchases.csv</span>
      -   purchases.csv
  
    - **inventory_rent**
      -  <span style="color:yellow">inventory_rent.py</span>
      -  <span style="color:pink">inventory_rent.csv</span>

    - **staff**
      -   <span style="color:yellow">staff.py</span>
      -  <span style="color:pink">staff.csv</span>
          
    - **tournament**
      -   <span style="color:yellow">tournament.py</span>
      -   tournament.ipynb
      -  <span style="color:pink">tournaments.csv</span>
           
    - **tournament_rental_consistency**
      -   tournament_rental_consistency.py
          
    - **tournament_results**
      -   <span style="color:yellow">tournament_results.py</span>
      -   tournament_results.ipynb
      -  <span style="color:pink">tournament_results.csv</span>

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

