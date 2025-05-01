from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app, request
)
from werkzeug.exceptions import abort
import os

from kc_5330.db import get_db

bp = Blueprint('download', __name__)

@bp.route('/download/<string:subdir>/<string:filenm>', methods=['GET'])
def download(filenm, subdir):
    src_folder = os.path.join(current_app.root_path, 'static', subdir)
    ext = ''
    file_name = filenm
    if subdir == 'data' or 'overview' in file_name:
        file_name = ''.join([char for char in filenm.lower() if char.isalnum()])
        ext = '.csv'
    
    return send_from_directory(src_folder, f'{file_name}{ext}', as_attachment=True)