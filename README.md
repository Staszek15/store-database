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

