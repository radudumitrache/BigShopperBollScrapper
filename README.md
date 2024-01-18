
# Importing the database schema to your local database in PyCharm:

- After setting up PostgreSQL on your computer, navigate to PyCharm and connect to your local database, which is typically named 'postgres' by default.
- Once connected to your local database, import the schema by right-clicking on the local database, selecting 'SQL Script,' and running the SQL script.
- This process will import all the database tables and data for you.


# Manual

## Introduction

This project is the work of IT2B. It is a web scraper built in order to scrape item information from Bol.com. It works through the command line where the user submits either an EAN or a title of the item. After that the program finds, stores and displays the found item with additional information scraped about the item itself.

## Connecting to the Database in PyCharm

1. Install PostgreSQL
2. Open the Project in PyCharm where the schema.sql file is located.
3. Go to View -> Tool Windows -> Database to open the Database tool window.
4. In the Database tool window, click the + icon to add a new data source.
5. Select Data Source: PostgreSQL.

## Configure the data source with the following details

- Host localhost
- Port 5432
- Database ScraperDB
- User clarissa mitch radu stefan zsombor beyza lorand
- Password clarissa mitch radu stefan zsombor beyza lorand

Test the Connection Verify the database connection to ensure that your credentials are correct, and the database server is accessible.

## Updating the schema.sql File for GitHub

1. SQL Script The schema.sql file must be run before pushing

## Running the software

1. Clone the repository into your local folder using the following command

```
git clone [repo_url]
```

2. Change directory to the root directory of the project
3. Create a new Virtual Environment using the following commands

```
python -m venv .venv
```

4. Enable the virtual environment

MacOS/Linux

```
source .venv/bin/activate
```

Windows

```
.venv\Scripts\activate.bat In CMD
.venv\Scripts\Activate.ps1 In Powershel
```

5. Install the dependencies from the requirements.txt

```
pip install -r requirements.txt
```

6. Change directory to src

```
cd src
```

7. Example command to start the scraper

```
python manage.py command --search 'example1', 'example2', 'example3' --region NL
```

This command will take the items named example1, example2, example3 and will search the the Dutch bol.com for the best matching item. If it finds the item it gets saved in the database.

## Command line options

```--search```

The --search flag is mandatory. It allows you to specify one or multiple items to search for.

```--region```

The --region flag is mandatory. It allows you to select which region to search in. Currently NL (Netherlands) and BE (Belgium) are supported.

## Special Thanks to

- Arjen Zijlstra
- Seitse Rijpstra
- Victor Zwart

For assisting us throughout this project and allowing us to collaborate with Bigshopper
>>>>>>> a255370c6aa780bd48ba1881884520af4bf0ae03
