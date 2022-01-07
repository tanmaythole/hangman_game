# Hangman Game

Created Hangman Game in Django.

# Features
- Responsive to all devices
- User Friendly

# Technologies Used
- Django (Python framework)
- Bottstrap
- JavaScript
- Ajax

# Screenshots
<p align="center">
    <img src="https://raw.githubusercontent.com/tanmaythole/hangman_game/master/game/static/images/screenshot-1.png" />
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/tanmaythole/hangman_game/master/game/static/images/screenshot-2.png" />
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/tanmaythole/hangman_game/master/game/static/images/screenshot-3.png" />
</p>

# How to Run Locally
Run the below command to clone the repository locally
```
git clone https://github.com/tanmaythole/hangman_game.git
```

Then create virtual environment
```
sudo apt install python3-venv
```

```
python3 -m venv env
```

To start using this virtual environment, activate it by running the activate script:
```
source env/bin/activate
```

Then install requirements.txt
```
pip3 install -r requirements.txt
```

After applying above steps, run following commands:
```
python manage.py makemigrations
```

```
python manage.py migrate
```

And, finally run the server by using
```
python manage.py runserver
```
Now, this will run your application in http://127.0.0.1:8000
<br />
<br />


# Future Scope
- User Authentication
- Add time limit for game
