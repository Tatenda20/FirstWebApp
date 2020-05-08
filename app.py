from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return '<p>Hello World!</p>'


@app.route('/about')
def about_page():
    return '<p>This is the about us page</p>'


@app.route('/status')
def status_page():
    return '<p>Everything is working as expected</p>'


if __name__ == '__main__':
    app.run()
