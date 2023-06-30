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
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) address.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) address.csv
      -   postal_codes.csv
    - **analysis**
      -   plots.py
      -   plot_registrations.png
      -   plot_rentals.png
           
    - **create_staff_schedule**
       -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) create_staff_schedule.py
       -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) staff_schedule.csv

    - **customer_rental**
      -  -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) customer_rental.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) customers.csv 
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) rentals.csv
    - **game**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) game.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) game.csv
      -   all_games.xlsx
      -   games_dataset.csv
      -   selected_games.xlsx

    - **inventory_buy_purchase**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) inventory_buy_purchase.py
      -   inventory_buy, purchase.ipynb
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) inventory_buy.csv
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) purchases.csv
      -   purchases.csv
  
    - **inventory_rent**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) inventory_rent.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) inventory_rent.csv

    - **staff**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) satff.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) staff.csv
          
    - **tournament**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) tournament.py
      -   tournament.ipynb
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) tournaments.csv
           
    - **tournament_rental_consistency**
      -   tournament_rental_consistency.py
          
    - **tournament_results**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) tournament_results.py
      -   tournament_results.ipynb
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) tournament_results.csv

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


