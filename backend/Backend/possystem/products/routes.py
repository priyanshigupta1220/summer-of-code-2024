from flask import Flask,Blueprint,jsonify,request
from possystem.database import cursor


product_bp=Blueprint('product_bp',__name__,template_folder='templates',static_folder='static')

@product_bp.route('/products',methods=['GET'])
def all_products():
    q="SELECT * FROM inventoryitem "
    cursor.execute(q)
    prod=cursor.fetchall()
    return prod
@product_bp.route('/product/<string:item_SKU>',methods=['GET'])
def product(item_SKU):
    q="SELECT * FROM inventoryitem"
    cursor.execute(q)
    prod=cursor.fetchall()
    print(f'{prod}')
    for row in prod:
        if row['item_SKU']==item_SKU:
            return row
        
    return "Not found"
                  
@product_bp.route('/product',methods=['POST'])
def add_product():
    q="INSERT INTO inventoryitem VALUES('item_SKU'=,'item_name':request.json['item_name',''])"
    cursor.execute(q)
    return "Product Added"
@product_bp.route('/product/string:item_SKU>',methods=['PUT'])
def update_product():
    return "Product Updated"
    

@product_bp.route('/product/<string:item_SKU>',methods=['DELETE'])
def delete_product():
    q="DELETE FROM inventoryitem WHERE item_SKU=item_SKU"
    cursor.execute(q)
    return "Deleted Product"
