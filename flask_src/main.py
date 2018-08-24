import flask
from openpyxl import load_workbook

app = flask.Flask(__name__)

@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def index():
	if flask.request.method == 'GET':
		return flask.render_template('test_ABLLS.html')
	else:
		return 'Ваши ответы сохранены'

app.run()
