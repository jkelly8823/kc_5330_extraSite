from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

import click

bp = Blueprint('methods', __name__)

@bp.route('/methods')
def index():
    return render_template('methods/index.html')