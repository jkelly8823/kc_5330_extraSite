from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('welcome', __name__)

from kc_5330.db import get_db
def list_db():
    db = get_db()
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    for table in tables:
        print(table['name'])  # if you're using Row factory


@bp.route('/')
def index():
    return render_template('welcome/index.html', lst=list_db())