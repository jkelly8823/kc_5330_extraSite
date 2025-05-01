import sqlite3
from datetime import datetime

import click
from flask import current_app, g

import csv


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def populate_db(db):
    with current_app.open_resource('static/data/datasetoverview.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO datasetoverview (tool, ver, src, aim) VALUES (?, ?, ?, ?)',
                (row['tool'], row['ver'], row['src'], row['aim'])
            )

    with current_app.open_resource('static/code/codeoverview.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO codeoverview (filenm, purpose) VALUES (?, ?)',
                (row['filenm'], row['purpose'])
            )

    db.commit()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    
    populate_db(db)


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)