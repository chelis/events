# This file provided by Facebook is for non-commercial testing and evaluation
# purposes only. Facebook reserves all rights not expressly granted.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# FACEBOOK BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
import os
import time
from flask import Flask, Response, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import simplejson as json
from  flask.json import jsonify

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import EventType, Event

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html', event_types=json.dumps(list(EventType.query.all())))

@app.route('/api/events', methods=['GET', 'POST'])
def comments_handler():

    if request.method == 'POST':
        newComment = request.form.to_dict()
        print newComment
        del newComment['id']
        db.session.add(Event(**newComment))
        db.session.commit()

    events = Event.query.all()
    # return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})
    return jsonify(results=list(events))

@app.route('/api/events/delete/<int:comment_id>', methods=['POST'])
def comments_delete_handler(comment_id):
    if request.method == 'POST':
        Event.query.filter_by(id=comment_id).delete()
        db.session.commit()

    events = Event.query.all()
    return jsonify(results=list(events))


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",3000)))
