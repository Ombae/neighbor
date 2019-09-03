#### Web clone of the Instagram app
#
#### By **[Seth Ombae](https://github.com/Ombae)**

## Description
This is a simple web clone of the instagram website. A user can create an account and sign into it.
A user can then upload images, and follow other users.
A user can view photos uploaded by other users in the home page of app.

## BEHAVIOUR DRIVEN DEVELOPMENT(BDD)

| Behaviour | Input                     | Output                    |
| --------- | ------------------------- | ------------------------- |
|Navigate to website| Click on a profile | User profile is displayed |
|Adding Comments| Click on add a comment link and type your comment|Comments for that photo is displayed|
|Navigate to search input| Type in a user profile e.g Coates|That searched profile is displayed|
|Adding Images| Click on post image button | User is promted with a form to upload the image |

## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/Ombae/Instagram Clone.git && cd Instagram`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 virtual && source virtual/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE instaclone;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'instaclone'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations app
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
Like and Follow functionality do not work

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql

## Support and contact details
Contact me on ombaejr@gmail.com for any comments, reviews or advice.

### License
Copyright (c) [Ombae](https://github.com/Ombae/neigbor/blob/master/LICENSE)
