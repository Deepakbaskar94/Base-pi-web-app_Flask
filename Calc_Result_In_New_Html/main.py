from flask import Flask , render_template , request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/result1', methods = ['POST', 'GET'])
def result1():
    if request.method == 'POST' :
        num1 = request.form['FN']
        num2 = request.form['SN']
        num1 = int(num1)
        num2 = int(num2)
        sum1 = num1 + num2
        sum1 = str(sum1)
        return render_template('Result.html' , name=sum1)
    
    else:
        num1 = request.args.get('FN')
        return render_template('index.html' , name=num1)
    

    # return render_template('Result.html')

if __name__=="__main__":
    app.run(host ='192.168.129.188', port=80 ,debug=True )