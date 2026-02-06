from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({"message": "welcome"}), 200
    pass  # TODO: Return a welcome message

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
    stuff = [product for product in products]
    return jsonify(stuff), 200
    pass  # TODO: Return all products or filter by ?category=

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    thing = [item["name"] for item in products if item["id"] == id]
    if thing == []:
        return jsonify({"message": "Item not found"}), 404
    return jsonify("name", thing), 200
    pass  # TODO: Return product by ID or 404

if __name__ == "__main__":
    app.run(debug=True)
