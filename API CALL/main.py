from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/Result1")
def result1():
    return render_template('Result.html')


if __name__=="__main__":
    app.run(host ='192.168.129.188', port=80 ,debug=True )