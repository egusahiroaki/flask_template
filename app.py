from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html', message="Hello")

@app.route('/hello')
def hello():
	val = request.args.get("msg", "not defined")
	return 'hellow word' + val

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' %  username

if __name__ == "__main__":
	app.run()
