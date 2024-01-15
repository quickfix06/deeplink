import flask

app = flask.Flask(__name__)

@app.route("/deeplink/<assignment_id>")
def index(assignment_id):
	return flask.render_template('index.html', key=assignment_id)


if __name__ == "__main__":
	app.debug = True
	app.run()
