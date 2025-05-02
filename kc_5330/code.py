from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app
)
from werkzeug.exceptions import abort
import os

from kc_5330.db import get_db

bp = Blueprint('code', __name__)

@bp.route('/code')
def index():
    db = get_db()
    curs = db.execute(
            'SELECT * FROM codeoverview'
        )
    rows = curs.fetchall()
    cols = [desc[0] for desc in curs.description]
    return render_template('code/index.html', rows=rows, cols=cols, overview=True, tablenm='Code Overview', subdir='code')

@bp.route('/code/viewer/<string:filenm>', methods=['GET'])
def code_viewer(filenm):
    src = os.path.join(current_app.root_path, 'static/code')
    with open(f'{src}/{filenm}', 'r') as f:
        code_content = f.read()
    return render_template('code/code_viewer.html', code_content=code_content, filenm=filenm, subdir='code')