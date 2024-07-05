from flask import Flask,render_template,request,redirect,url_for,session
from possystem.config import Config
from flask_migrate import Migrate
from possystem.database import db
import psycopg2
import os
from .admin import routes
from .products import routes
from .cashier import routes


def create_app():
    app=Flask(__name__,static_folder=r"C:\Users\NARESH CHAND\Desktop\DSoC\Backend\possystem\static")
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:backend@localhost:5432/POSSystem"

    )

    app.register_blueprint(admin.routes.admin_bp)
    app.register_blueprint(products.routes.product_bp)
    app.register_blueprint(cashier.routes.cashier_bp)

    

    db.init_app(app)
    from possystem.models.customer import Customer
    from possystem.models.inventory import InventoryItem
    from possystem.models.staff import Staff
    from possystem.models.transactions import Transaction
    migrate=Migrate(app,db)

   


    return app