from flask import Blueprint, request

from . import db
from .models import Product

create_product_blueprint = Blueprint("create_product", __name__)
list_products_blueprint = Blueprint("list_products", __name__)
order_product_blueprint = Blueprint("order_product", __name__)


@create_product_blueprint.route("/products", methods=["POST"])
def create_product():
    data = request.json
    name = data.get("name")
    amount = data.get("amount_in_stock", 0)

    if not name:
        return jsonify({"message": "Name is required"}), 400  # noqa

    product = Product.query.filter_by(name=name).first()
    if product:
        product.amount_in_stock += amount
    else:
        product = Product(name=name, amount_in_stock=amount)
        db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product created/updated successfully"}), 201  # noqa


@list_products_blueprint.route("/products", methods=["GET"])
def list_products():
    products = Product.query.all()
    output = []
    for product in products:
        product_data = {
            "id": product.id,
            "name": product.name,
            "amount_in_stock": product.amount_in_stock,
        }
        output.append(product_data)
    return jsonify({"products": output})  # noqa


@order_product_blueprint.route("/order", methods=["POST"])
def order_product():
    data = request.json
    product_id = data.get("id")
    quantity = data.get("quantity", 1)

    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404  # noqa

    if product.amount_in_stock < quantity:
        return jsonify({"message": "Not enough stock available"}), 400  # noqa

    product.amount_in_stock -= quantity
    db.session.commit()

    return jsonify({"message": "Order placed successfully"}), 200  # noqa
