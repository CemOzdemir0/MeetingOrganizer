from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route

@app.route('/meetings', methods=['GET', 'POST'])
def all_meetings():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        MEETINGS.append({
            'id': uuid.uuid4().hex,
            'subject': post_data.get('subject'),
            'date': post_data.get('date'),
            'stime': post_data.get('stime'),
            'ftime': post_data.get('ftime'),
            'subs': post_data.get('subs'),

        })
        response_object['message'] = 'Toplanti Eklendi!'
    else:
        response_object['meetings'] = MEETINGS
    return jsonify(response_object)
@app.route('/meetings/<meeting_id>', methods=['PUT', 'DELETE'])
def single_meeting(meeting_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_meeting(meeting_id)
        MEETINGS.append({
            'id': uuid.uuid4().hex,
            'subject': post_data.get('subject'),
            'date': post_data.get('date'),
            'stime': post_data.get('stime'),
            'ftime': post_data.get('ftime'),
            'subs': post_data.get('subs'),

        })
        response_object['message'] = 'Toplanti Guncellendi!'
    if request.method == 'DELETE':
        remove_meeting(meeting_id)
        response_object['message'] = 'Toplanti Silindi!'
    return jsonify(response_object)

def remove_meeting(meeting_id):
    for meeting in MEETINGS:
        if meeting['id'] == meeting_id:
            MEETINGS.remove(meeting)
            return True
    return False

MEETINGS = [
    {
        'id': uuid.uuid4().hex,
        'subject': 'Tanisma',
        'date': '2022-01-14',
        'stime': '13:00',
        'ftime': '14:00',
        'subs': ['Cem Ozdemir ', 'Ergin Dogan'],
    },
    {
        'id': uuid.uuid4().hex,
        'subject': 'Proje1',
        'date': '2022-02-19',
        'stime': '14:00',
        'ftime': '15:00',
        'subs': ['Cem Ozdemir ', 'Emre Bedir'],
    },
    {
        'id': uuid.uuid4().hex,
        'subject': 'Proje2',
        'date': '2022-03-24',
        'stime': '15:00',
        'ftime': '16:00',
        'subs': ['Ergin Dogan ', 'Emre Bedir'],
    }
]
if __name__ == '__main__':
    app.run()