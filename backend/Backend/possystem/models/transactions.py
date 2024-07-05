from possystem.database import db
from possystem.models.customer import Customer
from sqlalchemy import ForeignKeyConstraint
class Transaction(db.Model):
    __tablename__="transaction"
    t_ID=db.Column(db.String,primary_key=True)
    c_ID=db.Column(db.String,nullable=False)
    t_date=db.Column(db.DateTime,nullable=False)
    t_amount=db.Column(db.Integer,nullable=False)
    t_category=db.Column(db.String,nullable=False)

    __table_args__=(
        ForeignKeyConstraint([c_ID],[Customer.c_ID],ondelete='NO ACTION'),
    )

    def __init__(self,c_ID,t_data,t_amount,t_category):
        self.c_ID=c_ID
        self.t_amount=t_amount
        self.t_date=t_data
        self.t_category=t_category