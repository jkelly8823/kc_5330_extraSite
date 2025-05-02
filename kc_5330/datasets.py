from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app
)
from werkzeug.exceptions import abort

from kc_5330.db import get_db

bp = Blueprint('datasets', __name__)

@bp.route('/datasets')
def index():
    db = get_db()
    curs = db.execute(
            'SELECT * FROM datasetoverview'
        )
    rows = curs.fetchall()
    cols = [desc[0] for desc in curs.description]
    return render_template('datasets/index.html', rows=rows, cols=cols, overview=True, tablenm='Dataset Overview', subdir='data')

@bp.route('/datasets/viewer/<int:id>', methods=['GET'])
def dataset_viewer(id):
    db = get_db()

    columns = db.execute(f"PRAGMA table_info(datasetoverview)").fetchall()
    target = columns[1]['name']

    table_nm = db.execute(
        f'SELECT {target} FROM datasetoverview WHERE id==?', (id,)
    ).fetchone()[target]
    dataset = ''.join([char for char in table_nm.lower() if char.isalnum()])

    curs = db.execute(
        f'SELECT * FROM {dataset}'
    )
    rows = curs.fetchall()
    cols = [desc[0] for desc in curs.description]

    return render_template('datasets/dataset_viewer.html', rows=rows, cols=cols, overview=False, tablenm=table_nm, subdir='data')
