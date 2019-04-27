Introduction
-------------
This is a starter django application for prismic.
The project has been updated to be used with:

- Python 3.6
- Django 2.2
- Prismic 1.5.0


Configuration
-------------
Inside your settings.py, add a dictionary PRISMIC with two keys:

* api - API endpoint
* token - If specified, this token is used for all "guest" requests

Example:

    PRISMIC = {
        "api": "https://your_name.prismic.io/api",
        "token": ""
    }