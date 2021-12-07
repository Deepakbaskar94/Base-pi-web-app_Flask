
from flask import Flask, render_template, request

app = Flask(__name__)
	
@app.route("/")
def index():

	return render_template('try1.html')

if __name__ == "__main__":
   app.run(host='192.168.137.1', port=80, debug=True)
