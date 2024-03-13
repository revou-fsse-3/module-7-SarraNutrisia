from flask import Blueprint, render_template

product_routes = Blueprint('product_routes',__name__)

@product_routes.route("/product", methods=['GET'])
def base_home():
    return render_template("products/product_home.html")
