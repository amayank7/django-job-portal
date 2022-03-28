# django-job-portal

## Recommended Installation

## cd to Project Directory, enter a new virtual environment, install all the dependencies:

```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Migrate the Database:

```
python manage.py makemigrations
python manage.py migrate
```

## Run Server:

```
python manage.py runserver
```

This should start a development server, Go to the link output by the terminal in response to above command. ("127.0.0.1:8000" unless you've made changes.)

A superuser can be created to access the Django admin site at "127.0.0.1:8000/admin" using create superuser command.
```
python manage.py create superuser
```

# In order to provide updation of Tailwind CSS classes on the server, while in development:

Make sure you have NodeJS / npm installed on the system, change the "NPM_BIN_PATH" variable in the settings.py file to the npm installation location.
Open another terminal, cd to project directory:

```
python manage.py tailwind install
python manage.py tailwind start
```

Run the development server and the the browser will now provide automatic reloads for any saved changes to Tailwind classes.
