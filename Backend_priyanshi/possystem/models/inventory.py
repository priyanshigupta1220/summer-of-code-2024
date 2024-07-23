from possystem.database import db


class InventoryItem(db.Model):
    __tablename__="inventoryitem"
    item_sku=db.Column(db.Integer,primary_key=True)
    item_name=db.Column(db.String(100),unique=True,nullable=False)
    item_desc=db.Column(db.String(255))
    item_price=db.Column(db.Integer,nullable=False)
    item_qty=db.Column(db.Integer,nullable=False)

    
    def __init__(self,item_sku,item_name,item_desc,item_price,item_qty):
        self.item_sku=item_sku
        self.item_name=item_name
        self.item_desc=item_desc
        self.item_price=item_price
        self.item_qty=item_qty

    def __repr__(self):
        return f"<InventoryItem {self.item_sku,self.item_name}>"