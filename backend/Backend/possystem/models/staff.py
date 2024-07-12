
from possystem.database import db
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user
class Staff(db.Model,UserMixin):
    __tablename__="staff"
    s_id=db.Column(db.Integer,primary_key=True)
    s_name=db.Column(db.String(50),nullable=False)
    s_email=db.Column(db.String(255),nullable=False)
    password=db.Column(db.String,nullable=False)
    s_isadmin=db.Column(db.Boolean,nullable=False)
    s_isapproved=db.Column(db.Boolean,nullable=False)
    s_contact=db.Column(db.String(10),nullable=False)
    s_isdeleted=db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self,s_name,s_email,password,s_isadmin,s_isapproved,s_contact,s_isdeleted):
        self.s_name=s_name
        self.s_email=s_email
        self.password=password
        self.s_isadmin=s_isadmin
        self.s_isapproved=s_isapproved
        self.s_contact=s_contact
        self.s_isdeleted=s_isdeleted

    def __repr__(self):
        return f"<Staff {self.s_id,self.s_name}>"