import string
import random
from flask import Flask, render_template, request

lower_latter=string.ascii_lowercase
upper_latter=string.ascii_uppercase
digit=string.digits
punctuation=string.punctuation

s=[]
s.extend(list(lower_latter))
s.extend(list(upper_latter))
s.extend(list(digit))
s.extend(list(punctuation))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shortenurl')
def shortenurl():
    temp=int(request.args['password_length'])
    finalPassword=("".join(random.sample(s,temp)))
    return render_template('shortenurl.html', shortcode=temp,test_pass=finalPassword) 

app.run(debug=True)

