from flask import Flask,Blueprint,jsonify,request
from possystem.database import cursor
transaction_bp=Blueprint('transaction_bp',__name__,template_folder='templates',static_folder='static')

