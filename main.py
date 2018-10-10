# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
from __future__ import print_function
import logging
import sys

from flask import Flask, send_file, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route('/static/<path:fname>')
def download_file(fname):
    return send_from_directory('static', fname)

@app.route('/console')
def console():
	return render_template('console.html')

@app.route('/api')
def api_call():
    print('API!', file=sys.stderr)
    return 'foo'

@app.route('/')
def home():
    print('ROOT!', file=sys.stderr)
    return render_template('index.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
