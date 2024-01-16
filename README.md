# Manual

## Introduction
This project is the work of IT2B. It is a webscraper built in order to scrape item information from Bol.com. It works through the command line where the user submits either an EAN or a title of the item. After that the program finds, stores and displays the found item with additional information scraped about the item itself.

## Connecting to the Database in PyCharm
1. Install PostgreSQL 
2. Open the Project in PyCharm where the schema.sql file is located.
3. Go to View  Tool Windows  Database to open the Database tool window.
4. In the Database tool window, click the + icon to add a new data source.
5. Select Data Source  PostgreSQL.

   
## Configure the data source with the following details
- Host localhost
- Port usually 5432
- Database ScraperDB
- User clarissa mitch radu stefan zsombor beyza lorand
- Password clarissa mitch radu stefan zsombor beyza lorand

## Test the Connection Verify the database connection to ensure that your credentials are correct, and the database server is accessible.

   
## Updating the schema.sql File for GitHub
1. SQL Script The schema.sql file must be run before pushing 

## Running the software
1. Clone the repository into your local folder using the following command
```
git clone https_code_link
```
2. Go to the rootdirectory of the project
3. Create a Virtual Enviroment using the following commands


```
python -m venv pathtonewvirtualenvironment
```
4. Enable the virtual enviroment with the following command 

MacOs  Linux
```
source envbinactivate
```

Windows 

````
envScriptsactivate.bat In CMD
envScriptsActivate.ps1 In Powershel
````

5. Install the dependencies from the requirements.txt using the following command

```
pip install -r requirements.txt
```

## Command Line Start Program and Options
1. Use the following command to start the project
```
python manage.py command --search 'example1', 'example2', 'example3'
```
This command will take the items named example1, example2, example3 and will search bol.com for the best matching item. If it finds the item it gets saved in the database.

2. Additional flags

```
 --region
```
the --region flag allows the user to choose between a country in which bol.com  is avaliable. Currently these choices are nl or be. 

an example request using the --region flag would be
 ```
 python manage.py command --region 'bl' --search 'item1', 'item2', 'item 3'
 ```

## Special Thanks to

- Arjen Zijlstra
- Seitse Rijpstra
- Victor Zwart

For assisting us throughout this project and allowing us to collaborate with Bigshopper
