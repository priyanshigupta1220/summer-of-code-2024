from possystem.database import db
from possystem.models.customer import Customer
from possystem.models.staff import Staff
from sqlalchemy import ForeignKeyConstraint
class Transaction(db.Model):
    __tablename__="transaction"
    t_id=db.Column(db.Integer,primary_key=True)
    c_id=db.Column(db.Integer)
    s_id=db.Column(db.Integer)
    t_date=db.Column(db.DateTime,nullable=False)
    t_time=db.Column(db.DateTime,nullable=False)
    t_amount=db.Column(db.Integer,nullable=False)
    

    __table_args__=(
        ForeignKeyConstraint([c_id],[Customer.c_id],ondelete='NO ACTION'),
        ForeignKeyConstraint([s_id],[Staff.s_id],ondelete='NO ACTION'),
    )

    def __init__(self,c_id,s_id,t_date,t_time,t_amount):
        self.c_id=c_id
        self.s_id=s_id
        self.t_amount=t_amount
        self.t_date=t_date
        self.t_time=t_time
        