from flask import Flask,Blueprint,jsonify,request,render_template,make_response,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Length,Regexp
from possystem.database import cursor
staff_bp=Blueprint('staff_bp',__name__,template_folder='templates',static_folder='static')

class createstaff(FlaskForm):
    s_name=StringField("Full Name",validators=[InputRequired(message='cant be blank')])
    s_email=StringField("Email",validators=[InputRequired(message='cant be blank')])
    password=PasswordField("Password",validators=[InputRequired(message='cant be blank')])
    s_isadmin=BooleanField("Admin")
    s_isapproved=BooleanField("Approved")
    s_contact=StringField("Contact Number",validators=[InputRequired(),Length(min=10, max=10)])
    submit=SubmitField('Submit')


@staff_bp.route('/staffs',methods=['GET'])
def all_staff():
    q="SELECT * FROM staff "
    cursor.execute(q)
    staff=cursor.fetchall()
    return staff

@staff_bp.route('/staff/<int:s_id>',methods=['GET'])
def search_staff(s_id):
    q="SELECT * FROM staff"
    cursor.execute(q)
    staff=cursor.fetchall()
    print(f'{staff}')
    for row in staff:
        if row['s_id']==s_id:
            return row
        
    return "Not found"
@staff_bp.route('/staff',methods=['GET','POST'])
def create_staff():
    form=createstaff()
   
    if request.method=='POST' and form.validate_on_submit():
        name=form.s_name.data
        email=form.s_email.data
        pwd=form.password.data
        adm=form.s_isadmin.data
        approve=form.s_isapproved.data
        contact=form.s_contact.data
        session["s_name"]=form.s_name.data
        session["s_email"]=form.s_email.data
        session["password"]=form.password.data
        session["s_isadmin"]=form.s_isadmin.data
        session["s_isapproved"]=form.s_isapproved.data
        session["s_contact"]=form.s_contact.data
        q="INSERT INTO staff(s_name,s_email,password,s_isadmin,s_isapproved,s_contact) VALUES (name,email,pwd,adm,approve,contact)"   
        return "Staff Created"
    return render_template('create_staff.html',form=form)

        
    
@staff_bp.route('/staff/<int:s_id>',methods=['PATCH'])
def approve_staff():
    q="UPDATE staff SET is_admin=True WHERE request.s_id=s_id"
    cursor.execute(q)
    return "Admin Updated"
@staff_bp.route('/staff',methods=['PUT'])
def update_staff():
    q="UPDATE staff SET WHERE"
    cursor.execute(q)
    return "Updated"

@staff_bp.route('/staff',methods=['PATCH'])
def delete_staff():
    user=request.json()
    q="UPDATE staff SET is_deleted=True WHERE s_id=user "
    cursor.execute(q)
    return "Staff Deleted"