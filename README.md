# Gamestalgia
## Authors
### Julia Grzegorzewska, Karolina Wypych, Wiktoria Fimińska, Mateusz Stasiak
  
## Table of contents
* [Introduction](#introduction)
* [Description](#description)
* [Technologies](#technologies)
* [Files](#files)
* [How to run a program](#running)
* [The greatest challenges](#challenges)
* [EKNF](#eknf)

# Introduction <a name="introduction"></a>
These days in the fast changing world we are inundated with big volumes of data. It provokes higher demand for people specialized in processing it. A vast majority of companies and institutions could not work without efficient databases systems what makes an ability of creating and maintaining them a valuable skill. To gain it we developed a project during databases course at Wroclaw University of Science and Technology.

<p align="center">
  <img src="https://github.com/Staszek15/store-database/blob/main/images/logo_store.png" width=80%>
</p>

# Description <a name=description></a>
The project generally consists of generating a database and a report for Gamestalgia - a fictional board games rental store. Gamestalgia is a unique place. Not only does it rent games but also sells them and organize tournaments. Moreover, the most active customers are rewarded with a VIP status and hence extra discounts on rentals and purchases.

<p align="center">
  <img src="https://github.com/Staszek15/store-database/blob/main/images/database_schema.png" width=80%>
</p>

Above schema presents tables included in Gamestalgia's database and relations between them.     
Types of relations are symbolized by endings of lines connecting tables with each other:
* two vertical lines - **one and only one**
* circle and three branched lines - **zero or many**
* one vertical and three branched lines - **one or many**


# Technologies <a name=technnologies></a>
Making this project involved using following technologies:
- **Python**
It was applied to generate data for all tables. All dependencies between them were taken into consideration to provide a data integrity. Then Python was used for filling the database with valules generated previously.
- **MySQL**
It was used for creating the database schema and analysing data.
- **knitr**
This tool was applied to generate a report.

# Files <a name='files'></a>
Every underlined *.csv* file contains a complete dataset that later is used to fill a table of a similar name. 
All underlined *.py* files consist of functions that generate data, process it and return as a dataframe. (e.g. *address.py* provides data for table *address*, *customer_rental.py* for table *customers* and table *rentals*.) 
* **generate_data:**
    -   connection.py \
    It connects to the database by SQLAlchemy, reads the create_tables.sql and runs all the queries stored in this file. Then it inserts data from saved csv files.
    -   const.py \
        In this file constants are stored.
    -   create_tables.sql \
        Here sql code responsible for creating tables is stored.
    -   main_execute.py \
        Main function of the program. It run programs that generate data then writes results to csv and run programs responsible for linking to the database by SQLAlchemy and inserting data to tables.
    - **address**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) address.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) address.csv
      -   postal_codes.csv \
          Auxiliary csv file which store generated postal codes.
           
    - **create_staff_schedule**
       -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) create_staff_schedule.py
       -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) staff_schedule.csv

    - **customer_rental**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) customer_rental.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) customers.csv 
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) rentals.csv
    - **game**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) game.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) game.csv
      -   all_games.xlsx
      -   games_dataset.csv \
          Initial dataset that was downloaded from the Internet and modified. Results of the modifications were written to game.csv.
      -   selected_games.xlsx

    - **inventory_buy_purchase**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) inventory_buy_purchase.py
      -   inventory_buy, purchase.ipynb
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) inventory_buy.csv
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) purchases.csv
  
    - **inventory_rent**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) inventory_rent.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) inventory_rent.csv

    - **staff**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) satff.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) staff.csv
          
    - **tournament**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) tournament.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) tournaments.csv
           
    - **tournament_rental_consistency**
      -   tournament_rental_consistency.py \
      It prevents from lack of games during a tournament
          
    - **tournament_results**
      -  ![#cce6ff](https://placehold.co/15x15/cce6ff/cce6ff.png) tournament_results.py
      -  ![#ffcccc](https://placehold.co/15x15/ffcccc/ffcccc.png) tournament_results.csv

# How to run a program (on Windows)<a name=running></a>
1. clone repository
` git clone https://github.com/Staszek15/store-database.git` or download its zip file instead.
3. Open the console/terminal.
4. Navigate to generate_data folder.
5. Run the main_execute.py file to create database
6. Open report.Rmd (e.g. in RStudio).
7. Change the user in python path according to the hints provided close to this line of code. 
8. Knitr the report.
9. The saved report is located in store-database folder.


# EKNF <a name="eknf"></a>
1NF:
- every table has its own primary key
- every cell contains only one number, one date or one string
- every cell describes only one object
- order of row does not matter

2NF:
- database is 1NF
- all non-key attributes in any table depend on the entire primary key

3NF:
- databaase is 2NF
- none non-key attribute depend on another non-key attribute within the same table

EKNF:
- database is 3NF

# The greatest challenges <a name='challenges'></a>
This project is complex and combines the knowledge from various areas. That's why encountering some problems was unavoidable. Generally there were easy to solve so there's no point in elaborating on them. But there were some difficulties that consumed a lot of time and involved doing extensive research. 
1. Providing data integrity \
It was a priority to prepare a correct dataset. Taking care of consistency between tables and keeping them realistic enabled discussions and modifying tables not only at the beginning of working but also during further work. Some contradictions in seemingly proper datasets were noticed during generating other dependent tables. Sometimes it forced changes in schema of more than one table and modifications of code.
2. Connecting to server and filling the database in \

