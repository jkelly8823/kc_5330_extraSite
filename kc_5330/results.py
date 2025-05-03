from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort
import os

from kc_5330.db import get_db

import click

bp = Blueprint('results', __name__)

@bp.route('/results')
def index():
    db = get_db()
    curs = db.execute(
            'SELECT * FROM resultsoverview'
        )
    rows = curs.fetchall()
    cols = [desc[0] for desc in curs.description]
    cols = cols[:-1]
    return render_template('results/index.html',rows=rows, cols=cols, overview=True, tablenm='Results Overview', subdir='results')

@bp.route('/results/viewer/<string:filenm>', methods=['GET'])
def result_viewer(filenm):
    rows, cols = (None, None)
    db = get_db()

    caption = db.execute(
        f'SELECT caption FROM resultsoverview WHERE filenm==?',(filenm,)
    ).fetchone()[0]
    if caption == None:
        caption = ""
    
    if '.csv' in filenm:
        dataset = filenm[:filenm.find('.')]
        curs = db.execute(
            f'SELECT * FROM {dataset}'
        )
        rows = curs.fetchall()
        cols = [desc[0] for desc in curs.description]

    return render_template('results/result_viewer.html', rows=rows, cols=cols, overview=False, tablenm=filenm, subdir='results', caption=caption)
