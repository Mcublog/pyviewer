#!/usr/bin/env python

import logging

from flask import (Blueprint, flash, redirect, render_template, request,
                   send_file, url_for)
from flask_login import login_required
from werkzeug.utils import secure_filename

from .version import VERSION

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

ALLOWED_EXTENSIONS = set(['json'])

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', version=VERSION)

# @main.route('/upload')
# def uploading():
#     return render_template('upload.html')

@main.route('/upload', methods=['POST'])
def uploading_post():
    return redirect(url_for('main.index'))

