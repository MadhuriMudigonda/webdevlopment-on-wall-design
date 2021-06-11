from flask import Flask,render_template,request,url_for,request

from twilio.rest import Client
import random
import os
app = Flask(__name__)

otp=1232
print(otp)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/iop")
def iop():
    return render_template('iop.html')

@app.route("/nsol")
def nsol():
    return render_template('nsol.html')

@app.route("/submit",methods=['POST'])
def submit():
    if request.method =='POST':
        user=request.form['nm']
        print(user)
        client = Client('ACc34f26972a083619defee0d3c91af669', '57f9da64bfdf8d991994af266bcece42')
        message = client.messages \
                .create(
                     body=1232,
                     from_='+12133221433',
                     to=user
                 )
        print(message)
        
        return '''
        <head><style>
        *{
        align-items:center;
        justify-content:center;
        text-align:center;
        }
        body h1{
        color:red;
        }
        </style>
        </head>
        <body>
        <h1>we will contact you soon<h1><form action="/otp" method='POST'>
        <input type="text" name="ot"/>
        <input type="submit" value="submit"/></form>
        </body>'''
        
    else:
        return 'sorry'
@app.route('/otp',methods=['POST'])
def otp():
    if request.method=='POST':
        ot=request.form['ot']
        apo=int(ot)
        print(apo)
        if apo==int(1232):
           
               
            return 'We will connect u soon'
        else:
            return 'wrong otp'
    else:
        return 'something went wrong'
if __name__==('__main__'):
    app.run()