from flask import Flask,Blueprint,jsonify,request,render_template,make_response,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Length,Regexp
from possystem.database import cursor
customer_bp=Blueprint('customer_bp',__name__,template_folder='templates',static_folder='static')

class createcustomer(FlaskForm):
    c_name=StringField("Full Name",validators=[InputRequired(message='cant be blank')])
    c_email=StringField("Email",validators=[InputRequired(message='cant be blank')])
    c_contact=StringField("Contact Number",validators=[InputRequired(message='cant be blank'),Length(min=10, max=10)])
    submit=SubmitField('Submit')




@customer_bp.route('/customers',methods=['GET'])
def all_customers():
    q="SELECT * FROM customer "
    cursor.execute(q)
    cust=cursor.fetchall()
    return cust

@customer_bp.route('/customer/<int:c_id>',methods=['GET'])
def search_customer(c_id):
    q="SELECT * FROM staff"
    cursor.execute(q)
    cust=cursor.fetchall()
    print(f'{cust}')
    for row in cust:
        if row['c_id']==c_id:
            return row
        
    return "Not found"
@customer_bp.route('/customer',methods=['GET','POST'])
def create_customer():
    form=createcustomer()
   
    if request.method=='POST' and form.validate_on_submit():
        name=form.c_name.data
        email=form.c_email.data
        contact=form.c_contact.data
        
        q="INSERT INTO customer(c_name,c_email,c_contact) VALUES (1,2,3)" 
        cursor.execute(q)  
        
        return redirect(url_for(""))
    return render_template('create_customer.html',form=form)

