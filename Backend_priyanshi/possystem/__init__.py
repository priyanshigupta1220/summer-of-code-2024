from flask import Flask,render_template,request,redirect,url_for,session
from possystem.config import Config
from flask_migrate import Migrate
from possystem.database import db
import psycopg2
import os
from .staff import routes
from .login import routes
from .products import routes
from .customer import routes
from .transaction import routes
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user


def create_app():
    app=Flask(__name__,static_folder=r"C:\Users\NARESH CHAND\Desktop\DSoC\Backend\possystem\static")
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:backend@localhost:5432/POSSystem"

    )

    app.register_blueprint(staff.routes.staff_bp)
    app.register_blueprint(products.routes.product_bp)
    app.register_blueprint(customer.routes.customer_bp)
    app.register_blueprint(transaction.routes.transaction_bp)
    app.register_blueprint(login.routes.login_bp)

    db.init_app(app)
    from possystem.models.customer import Customer
    from possystem.models.inventory import InventoryItem
    from possystem.models.staff import Staff
    from possystem.models.transactions import Transaction
    migrate=Migrate(app,db)

    return app