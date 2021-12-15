from os import name
from flask import Flask , render_template , request,redirect , url_for

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
        #sum1 = str(sum1)
        return redirect (url_for('success', name=sum1)) 

    else:
        num1 = request.args.get('FN') 
        num2 = request.args.get('SN')
        res  = str("Entered numer is " + num1 +" and "  + num2)
        return render_template ("result.html", name = res)

@app.route('/success/<name>')
def success(name):
    num3 = int(name)
    FinalR = num3 +100
    # FinalR = str(FinalR)
    return render_template ("success.html", name =FinalR )


   

if __name__=="__main__":
    app.run(host ='192.168.129.188', port=80 ,debug=True )