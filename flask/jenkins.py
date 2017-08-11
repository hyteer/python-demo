from flask import Flask
from flask import render_template
from flask import request

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

########### Test ###########
@app.route('/test/<name>',methods=['POST', 'GET'])
def test(name):
    #import pdb;pdb.set_trace()
    if request.method == 'GET':
        print('method is get.')
        return render_template('test.html', name=name)
    else:
        print('method is post.')
        name = request.form['name']
        print('Name:',name)
        return 'data...'


