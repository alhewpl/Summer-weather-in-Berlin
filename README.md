## Python script to fetch historical summer data in Berlin & other german cities using DarkSky API

### How to use it

##### 1) Create the virtualenv
```bash
$ mkvirtualenv darksky
```

##### 2) Activate the virtualenv
```bash
$ source /Virtualenvs/darksky/bin/activate

##### 3) Install dependencies
```bash
$ pip install requirements.txt
```

##### 4) Before running the server, create the database. Schema is provided as a mysql dump
```bash
$ mysql -u username -p database_name < weather.sql
```

##### 5) Run the app
```bash
$ python forecast.py
```