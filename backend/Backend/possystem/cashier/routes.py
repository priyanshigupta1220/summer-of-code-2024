from flask import Blueprint
cashier_bp=Blueprint('cashier_bp',__name__,template_folder='templates',static_folder='static')

@cashier_bp.route('/cashier')
def cashier_login():
    return
