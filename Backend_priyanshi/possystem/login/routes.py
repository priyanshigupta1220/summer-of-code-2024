from flask import Flask,Blueprint,jsonify,request,render_template,make_response,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,IntegerField
from wtforms.validators import InputRequired,Length,Regexp
from possystem.database import db
from possystem.models.staff import Staff


login_bp=Blueprint('login_bp',__name__,template_folder='templates',static_folder='static')

class stafflogin(FlaskForm):
    s_id=IntegerField("Staff ID",validators=[InputRequired(message='cant be blank')])
    password=PasswordField("Password",validators=[InputRequired(message='cant be blank')])
    submit=SubmitField('Submit')

@login_bp.route('/login',methods=['GET','POST'])
def login():
    form=stafflogin()
    if request.method=='POST':
        s_id=request.form["s_id"]
        password=request.form["password"]
        user=Staff.query.filter_by(s_id=s_id).first()
        if user and user.check_password(password):
            session["s_id"]=user.s_id
            session["s_name"]=user.s_name
            session["s_email"]=user.s_email
            session["password"]=user.password
            session["s_isadmin"]=user.s_isadmin
            session["s_isapproved"]=user.s_isapproved
            session["s_contact"]=user.s_contact
            return redirect('/dashboard')
        else :
            return render_template('/login.html',form=form,error="Invalid user")
    return render_template("login.html",form=form)

@login_bp.route('/dashboard',methods=['GET','POST'])
def dashboard():
    print(session)
    if session['s_name']:
        user=Staff.query.filter_by(s_name=session['s_name']).first()
        if(user.s_isadmin==True):return render_template('admindashboard.html',user=user)
        else: return render_template("cashierdashboard.html",user=user)
    return redirect("login.html")

