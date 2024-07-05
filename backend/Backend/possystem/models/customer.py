from possystem.database import db
class Customer(db.Model):
    __tablename__="customer"
    c_ID=db.Column(db.String,primary_key=True)
    c_name=db.Column(db.String(50),nullable=False)
    c_email=db.Column(db.String(255),nullable=False)
    c_contact=db.Column(db.String(10),nullable=False)

    def __init__(self,c_name,c_email,c_contact):
        self.c_name=c_name
        self.c_email=c_email
        self.c_contact=c_contact

    def register_user_if_not_exist(self):        
        cust = Customer.query.filter(Customer.c_contact == self.c_contact).all()
        if not cust:
            db.session.add(self)
            db.session.commit()
        
        return True
    
    def get_by_username(contact):        
        cust =Customer.query.filter(Customer.c_contact ==contact).first()
        return cust

    def __repr__(self):
        return f"<Customer {self.c_name}>"