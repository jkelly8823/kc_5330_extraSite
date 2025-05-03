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

    with current_app.open_resource('static/data/gwascatalog.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO gwascatalog (chromosome, start_loc, stop_loc, rsid, phenotype, gene) VALUES (?, ?, ?, ?, ?, ?)',
                (row[None][0], row[None][1], row[None][2], row[None][3], row[None][9], row[None][13])
            )

    with current_app.open_resource('static/data/encodeccre.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO encodeccre (chromosome, start_loc, stop_loc, regulatory_element) VALUES (?, ?, ?, ?)',
                (row[None][0], row[None][1], row[None][2], row[None][11])
            )

    with current_app.open_resource('static/code/codeoverview.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO codeoverview (filenm, purpose) VALUES (?, ?)',
                (row['filenm'], row['purpose'])
            )

    with current_app.open_resource('static/results/resultsoverview.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO resultsoverview (filenm, title, caption) VALUES (?, ?, ?)',
                (row['filenm'], row['title'], row['caption'])
            )
    with current_app.open_resource('static/results/table1.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO table1 (rsid,phenotype,genes) VALUES (?, ?, ?)',
                (row['rsid'], row['phenotype'], row['genes'])
            )

    with current_app.open_resource('static/results/table2.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO table2 (rsid,phenotype,genes,exon_location) VALUES (?, ?, ?, ?)',
                (row['rsid'], row['phenotype'], row['genes'], row['exon_location'])
            )

    with current_app.open_resource('static/results/table3.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO table3 (gene,variantId,chr_bp,alleles,class) VALUES (?, ?, ?, ?, ?)',
                (row['gene'], row['variantId'], row['chr_bp'], row['alleles'], row['class'])
            )

    with current_app.open_resource('static/results/table4.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.execute(
                'INSERT INTO table4 (rsid,phenotype,genes,regulatory_element) VALUES (?, ?, ?, ?)',
                (row['rsid'], row['phenotype'], row['genes'], row['regulatory_element'])
            )

    db.commit()

def list_db():
    db = get_db()
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    nms = ['NAMES ARE:']
    for table in tables:
        nms.append(table['name'])
    click.echo(nms)
    return nms

@click.command('list-db')
def list_db_command():
    list_db()
    click.echo('Listed database')

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
    app.cli.add_command(list_db_command)