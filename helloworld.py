from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello world!'


@app.route('/hello')
def hello():
	return 'hello'


@app.route('/world')
def world():
	return 'world'


if __name__ == '__main__':
	app.run()
