from flask import Flask,Blueprint,jsonify,request,render_template,make_response,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,TextAreaField,PasswordField,BooleanField,FloatField
from wtforms.validators import InputRequired,Length,Regexp
from possystem.database import cursor

product_bp=Blueprint('product_bp',__name__,template_folder='templates',static_folder='static')

class createproduct(FlaskForm):
    item_name=StringField("Item Name",validators=[InputRequired()])
    item_desc=TextAreaField("Description")
    item_price=FloatField("Price",validators=[InputRequired()])
    item_qty=IntegerField("Quantity",validators=[InputRequired()])
    submit=SubmitField('Submit')
    
@product_bp.route('/products',methods=['GET'])
def all_products():
    q="SELECT * FROM inventoryitem "
    cursor.execute(q)
    prod=cursor.fetchall()
    return prod
@product_bp.route('/product/<int:item_sku>',methods=['GET'])
def product(item_sku):
    q="SELECT * FROM inventoryitem"
    cursor.execute(q)
    prod=cursor.fetchall()
    print(f'{prod}')
    for row in prod:
        if row['item_sku']==item_sku:
            return row
        
    return "Not found"
                  
@product_bp.route('/product',methods=['GET','POST'])
def add_product():
    form=createproduct()
    if request.method=='POST' and form.validate_on_submit():
        name=form.item_name.data
        desc=form.item_desc.data
        price=form.item_price.data
        qty=form.item_qty.data
        q="INSERT INTO inventoryitem(item_name,item_desc,item_price,item_qty) VALUES (name,desc,price,qty)"   
        cursor.execute(q)
        cursor.commit()
        return "Product Added"
    return render_template('create_product.html',form=form)

  
@product_bp.route('/product/<int:item_sku>',methods=['PUT'])
def update_product():
    return "Product Updated"
    

@product_bp.route('/product/<int:item_sku>',methods=['PUT'])
def delete_product():
    q="DELETE FROM inventoryitem WHERE item_SKU=item_SKU"
    cursor.execute(q)
    return "Deleted Product"
