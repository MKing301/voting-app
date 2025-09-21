
Meeting Voting (Django) — README
================================

Project overview
----------------

This is a small Django project that implements a simple meeting voting/polling application. It includes:

- A `votes` app with models for polls and choices.
- Templates for listing polls, viewing details, and showing results.
- Basic authentication (login) using Django's built-in auth views.

Repository structure
--------------------

- `meeting_voting/` — Django project settings and templates.
- `votes/` — Django app containing models, views, templates, and urls.
- `db.sqlite3` — SQLite database (for local development).
- `manage.py` — Django management script.

Quickstart (local development)
-----------------------------

Prerequisites
- Python 3.10+ (project appears to be using Python 3.12 bytecode; Python 3.10+ recommended)
- pip

Create and activate a virtual environment, install dependencies, and run the development server:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # create this file if missing (see notes below)
python manage.py migrate
python manage.py createsuperuser  # optional: create admin user to manage polls
python manage.py runserver
```

Open `http://127.0.0.1:8000/votes` in your browser. The app includes pages for listing polls, viewing a poll and voting, and viewing results.

Running tests
-------------

Run Django's test suite for the project:

```bash
python manage.py test
```

Project notes and TODOs
----------------------

- `requirements.txt` is not included in the repository: add one with pinned Django version (e.g. `Django>=4.2,<5`).
- Consider adding Docker support and an explicit development/prod settings split.
- Add more tests covering views and models.

Contact
-------

If you need help or want to contribute, open an issue or pull request in the repository.

License
-------

Project includes a `LICENSE` file in the repo root.
