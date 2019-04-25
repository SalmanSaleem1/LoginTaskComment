from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from flaskface.Models import Post
from textblob import TextBlob
from pusher import Pusher


main = Blueprint('main', __name__)

pusher = Pusher(
    app_id='769023',
    key='ca189d0b5f1bd4510daa',
    secret='2a010d904a0188b43368',
    cluster='ap2',
    ssl=True)


@main.route('/', methods=['POST', 'GET'])
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.create_at.desc()).paginate(page=page, per_page=5, error_out=False)
    return render_template('Home.html', title='Home', posts=posts)


@main.route('/add_comment', methods=["POST"])
def add_comment():
    # Extract the request data
    print('Add Comment')
    request_data = request.get_json()
    id = request_data.get('id', '')
    username = request_data.get('username', '')
    comment = request_data.get('comment', '')
    socket_id = request_data.get('socket_id', '')

    # Get the sentiment of a comment
    text = TextBlob(comment)
    sentiment = text.polarity

    comment_data = {
        "id": id,
        "username": username,
        "comment": comment,
        "sentiment": sentiment,
    }

    #  Trigger an event to Pusher
    pusher.trigger(
        "table", 'new-comment', comment_data, socket_id
    )

    return jsonify(comment_data)
