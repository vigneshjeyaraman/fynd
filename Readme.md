## Welcome to IMDB here you can View all movie details and as an admin you can add new movies, update, and delete them.

## Note

I have used Django's in built sqllite DB to run this project so that anyone can clone and run this easily without needing to install other dependencies.
But we can totally use PostgreSQL by replacing DATABASES value in settings.py with below one but we should have postgres setup
on our machine with whatever user, name, password you give in below settings.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER':'',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT': '5433'  # for local host it is not needed since on localhost by default PostgreSQL run on this port.
    }
}
```

# Project setup

1. git clone < REPO >

2. create a virtualenv with below command
    * virtualenv -p < location to python3.8 > venv
    ## if it says virtualenv not found you have to run below commands as per you OS
        - Mac- brew install virtualenv (if you don't have brew then run /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)")
        - Ubuntu- sudo apt-get install python-virtualenv

3. Activate the venv you created by running 
    * source venv/bin/activate

4. Install all the dependencies by running
    * pip install -r requirements.txt

5. Once venv activated go to directory where you have this projects manage.py and run
    * python manage.py migrate -- This will migrate all the tables

6. python3 scripts.py --> to dump movies data in DB

7. Once migration is successfull then run
    * python manage.py runserver --> It will run project by default on port 8000 if you want to change the port then run
        * python manage.py runserver 9000 --> it can be any port of your choice.

8. Now we can test the apis. I have given postman collection for your ease. Since this is deployed on Heroku postman collection will have
its endpoint. If we have to run this on our machine replace https://fyndimdbapi.herokuapp.com/ with http://127.0.0.1:8000/

## Postman Collection
https://www.getpostman.com/collections/86401b7f1b061954434c