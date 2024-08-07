from possystem.database import db
import sqlalchemy as sa
class Customer(db.Model):
    __tablename__="customer"
    c_id=db.Column(db.Integer,primary_key=True)
    c_name=db.Column(db.String(50),nullable=False)
    c_email=db.Column(db.String(255),nullable=False)
    c_contact=db.Column(db.String(10),nullable=False)

    def __init__(self,c_id,c_name,c_email,c_contact):
        self.c_id=c_id
        self.c_name=c_name
        self.c_email=c_email
        self.c_contact=c_contact

    def __repr__(self):
        return f"<Customer {self.c_name}>"