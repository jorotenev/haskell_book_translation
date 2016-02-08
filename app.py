from flask import Flask, render_template, send_from_directory
app = Flask(__name__,static_url_path='/static',template_folder=".")


@app.route("/")
def a():
    return render_template('introduction')

@app.route("/<file>")
def index(file):
     return render_template(file)

@app.route("/<path>")
def boo(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
	app.run(debug=True)