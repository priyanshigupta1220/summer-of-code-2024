
from possystem.database import db
import bcrypt

class Staff(db.Model):
    __tablename__="staff"
    s_id=db.Column(db.Integer,primary_key=True)
    s_name=db.Column(db.String(50),nullable=False)
    s_email=db.Column(db.String(255),nullable=False)
    password=db.Column(db.String,nullable=False)
    s_isadmin=db.Column(db.Boolean,nullable=False)
    s_isapproved=db.Column(db.Boolean,nullable=False)
    s_contact=db.Column(db.String(10),nullable=False)
    s_isdeleted=db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self,s_id,s_name,s_email,password,s_isadmin,s_isapproved,s_contact,s_isdeleted):
        self.s_id=s_id
        self.s_name=s_name
        self.s_email=s_email
        self.password=password#bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode
        self.s_isadmin=s_isadmin
        self.s_isapproved=s_isapproved
        self.s_contact=s_contact
        self.s_isdeleted=s_isdeleted

    def check_password(self,password):
            return password==password#bcrypt.checkpw(password.encode('utf-8',self.password.encode('utf-8')))
    def __repr__(self):
        return f"<Staff {self.s_id,self.s_name}>"