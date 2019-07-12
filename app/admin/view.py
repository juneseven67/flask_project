# . >> 代表此層 
from . import admin

# from flask import Blueprint
# admin = Blueprint('admin',__name__) 

@admin.route('/')
def admin_index():
    return "admin's index ~~~~"