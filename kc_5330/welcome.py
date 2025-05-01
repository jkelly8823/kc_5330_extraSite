from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

import click

bp = Blueprint('welcome', __name__)

from kc_5330.db import get_db

@click.command('list-db')
def list_db():
    db = get_db()
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    nms = ['NAMES ARE:']
    for table in tables:
        nms.append(table['name'])
    click.echo(nms)
    return nms


@bp.route('/')
def index():
    return render_template('welcome/index.html', lst=list_db())