from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

import click

bp = Blueprint('welcome', __name__)

from kc_5330.db import list_db


@bp.route('/')
def index():
    return render_template('welcome/index.html', lst=list_db())