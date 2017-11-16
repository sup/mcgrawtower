# mcgrawtower
Big Ben Clock clone for Cornell McGraw Tower

This is the source code for @mcgrawtower. It is a simple Python script that tweets "CHIME" times the current hour. The application is currently running on Heroku.

# Installation
Clone this repo and install dependencies via `pip install -r requirementes.txt` inside a virtualenv. Add Twitter app secrets to your environment and run with `python main.py` to start scheduling tweets. 

Or, install the heroku toolbelt, create a `.env` file containing your Twitter secrets, and run the app with `heroku local`. You can then host the app on Heroku as well.
