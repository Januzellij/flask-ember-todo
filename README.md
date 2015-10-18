# Flask-Ember-Todo
=
The Ember version of the TodoMVC application found <a href="http://emberjs.com/guides/getting-started/planning-the-application/">here</a>, backed by a Flask JSON API.

Most of the code in this app is from the above mentioned tutorial. I only added the API to interface with the database. Ember expects JSON in a specific format, so this can be a template for that, as it took me a bit to figure out the specifics.

### Installation
Clone this repository, navigate to that directory and use virtualenv:

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python app.py`

And your server should be up and running.
