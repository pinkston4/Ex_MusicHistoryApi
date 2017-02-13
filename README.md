# Music History API 

A school exercise for the django-rest framework

##Steps to Install

The API uses the Django_REST framework, running on Python 3.6

To install the project locally:

1. Clone the repository to desired location
1. Migrate the database tables. In the main project directory `~/Music_History/music_history_api` (where `manage.py` is located), run the command `python manage.py migrate`
1. Create a superuser for testing purposes: `python manage.py createsuperuser`.
1. Start the development server. Run the command `python manage.py runserver`. Take note of the IP address and host port given.
1. Start a browser, and navigate to the IP and port,  followed by `/api/`. i.e. ```127.0.0.1:8000/api/```.


