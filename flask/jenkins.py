from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'index...'

@app.route('/build/<jobname>')
def build(jobname):
    # show the user profile for that user
    return 'Job %s' % jobname

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

