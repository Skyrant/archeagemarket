##Overview
This is the current progress of my ArcheAge market. For various reasons, I've chosen to stop playing ArcheAge. As this is no longer a passion of mine, I find myself not support this project.
I would hate for the current work to go to waste, therefore I've opensourced the progress I do have.

##What Works

* **Character Creation**
 * Adding Professions
  * Removing Professions
  * Changing Profession Skill Levels

* **Guild Creation**
  * Guild Invites
  * Guild Promotions
  * Guild Deletion
  * Guild Profile

##What Needs To Be Done
* **General**
  * Check out the TODO in the code.
  * Ensure that you're checking for permissions in the templates, especially for /profile requests when the user is not logged in
  * Clean up templates, add error locations for every page.

* **Guilds**
  * Guild Profile Cleanup
  * Clickable Character Names

* **Userprofile**
  * Add option to create "friendly name" instead of just google user name. Useful for viewing profiles other than your own

* **Characters**
  * Character profile page for users other than yourself

* **Market**
  * Pretty much everything, need to create new data model for adding prices.
  * Note: you can find useful things in the resources folder, including the icons, and a mostly up-to-date item DB
  * Note: If you know how to get the sqlite DB from the archeage game_pak file, you can use the resources/add_item_table.py script to create item tables in a DB

* **LFW/WTB**
  * Pretty much everything, I wasn't really sure where I was going with this feature, and others had already written things better than mine.

* **Landtracker**
  * Again, Pretty much everything. I wasn't really sure where I was going with this feature, and others had already written things better than mine.

##Getting Started

###Create A Google AppEngine App

Follow the instructions here for getting google oauth keys: http://www.artandlogic.com/blog/2014/04/tutorial-adding-facebooktwittergoogle-authentication-to-a-django-application/

Copy config.cfg.example to config.cfg and fill in the oauth_key and oauth_secret settings.

###Create a Python virtual environment:

```
virtualenv -p /usr/bin/python3 venv
bin/pip install -r ../requirements.txt
```

###Initialize the Django DB
```
./django.sh syncdb
```

###Start The Service
```
./django.sh runserver
```
