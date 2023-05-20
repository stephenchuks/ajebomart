# AjeboMart

AjeboMart is an online shopping platform that is being developed to meet the requirements necessary to acquire the ALX-SE program for the award of a Nano Degree.

# Requirements

```
Python 3.9 or higher
PostgreSQL 13.* or higher - recommended
```

# Setup

## Development Environment

To ensure consistency in your coding style with others, it is recommended that you install the Python extension from Microsoft on your code editor, such as VS Code or any other equivalent editor you use. Additionally, you should set up your linter to follow pycodestyle and your formatter to follow autopep8. This will help you maintain a standardized coding style and improve the overall readability of your code.
## Virtual environment

How to setup a python virtual environment

- Create the virtual environment,

  ```
  python -m venv venv
  ```

- create virtual enviroment for LINUX

```
# install pip if not installed
sudo apt install python3-pip

# install virtualenv
sudo apt install python3-venv

# check version
virtualenv --version

# create virtual enviroment
virtualenv venv

# activate virtual enviroment
source venv/bin/activate
```

- Activate the virtual environment
  - for windows
  ```
  . venv/Scripts/activate
  ```
  - for Linux / macOS
  ```
  source .venv/bin/activate
  ```
- Deactivate the virtual environment when you need to,

  ```
  deactivate
  ```

## Install requirements

For local development

```
pip install -r requirements.txt
```

## Set environment variables

- Make a copy of the `sample.env` file, and rename it to `.env`

- Update the values of the variables in the `.env` file to suite your system environment.

- Create a folder named `logs` in the root directory, if it does not exist

## Datebase setup

### Create databases

Create an SQL database with the name matching what you have on the `.env` file for `DB_NAME` and `TEST_DB_NAME`. For example:

```
createdb ajebomart
```

### Export your flask app

In order to run your migrations and app using the `flask` command, expose your flask app:

- for Linux / macOS

```
export FLASK_APP=src/server.py
```

- On BASH

```
export FLASK_APP="src/server.py"
```

- On POWERSHELL

```
$env:FLASK_APP="src/server.py"
```

### **Create database tables from migrations**

To add the existing database schema run:

```
flask db upgrade
```

Make your database changes accessible to others using migrations

```
flask db migrate
```

### **Run server application**

From the root folder, run

```
python src/server.py
```

The application will run at the specified port `APPLICATION_PORT` in `.env` file

The local URL to access the API should be `http://localhost:5000/`
