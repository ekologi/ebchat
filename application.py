from flask import Flask, render_template, redirect, url_for
from wtform_fields import *
from models import * 
app = Flask(__name__)
app.secret_key = 'Ganti Nanti'

app.config['SQLALCHEMY_DATABASE_URI']='postgres://mbkdwzmhazkgjg:b95fdd499bf81bf5702c74a11ba8d413bb303b9a8758f9678d7e85414b4a4d63@ec2-3-95-124-37.compute-1.amazonaws.com:5432/dbjmvda6dn3rtc'
db=SQLAlchemy(app)
@app.route("/",methods=['GET','POST'])

def index():
    #return("Saya sudah idup")
    #return render_template("index.html")
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        #return "Mantab sukses!"
        # user_object = User.query.filter_by(username=username).first()
        # if user_object:
        #     return "Seseorang sudah menggunakan nama ini"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        #return "Simpan ke DB sukses"
        return redirect(url_for('Login'))

    return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET','POST'])
def login():

    login_form = LoginForm()

    if loginForm.validate_on_submit():
        return "logged in, finally"
    
    return render_template("login.html",form=login_form)    

if __name__ == "__main__":
    app.run(debug=True)