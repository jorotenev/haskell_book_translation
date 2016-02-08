from flask import Flask, render_template, send_from_directory
app = Flask(__name__,static_url_path='/static',template_folder=".")

tutorial_name = "asd"
@app.route("/")
def a():
    return render_template('introduction', tut_name = tutorial_name)

@app.route("/<file>")
def index(file):
     return render_template(file, tut_name = tutorial_name)

@app.route("/static/<path>")
def boo(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
	app.run(debug=True)