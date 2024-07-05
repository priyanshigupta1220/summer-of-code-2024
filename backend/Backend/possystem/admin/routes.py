from flask import Blueprint

admin_bp=Blueprint('admin_bp',__name__,template_folder='templates',static_folder='static')

@admin_bp.route('/admin')
@admin_bp.route('/<page>')
def admin_login():
    return 