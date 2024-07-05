from possystem.database import db

class Staff(db.Model):
    __tablename__="staff"
    s_ID=db.Column(db.String,primary_key=True)
    s_name=db.Column(db.String(50),nullable=False)
    s_email=db.Column(db.String(255),nullable=False)
    password=db.Column(db.String,nullable=False)
    s_isAdmin=db.Column(db.Boolean,nullable=False)
    s_contact=db.Column(db.String(10),nullable=False)

    def __init__(self,s_name,s_email,s_isAdmin,s_contact):
        self.s_name=s_name
        self.s_email=s_email
        self.s_isAdmin=s_isAdmin
        self.s_contact=s_contact

    def __repr__(self):
        return f"<Staff {self.s_ID,self.s_name}>"