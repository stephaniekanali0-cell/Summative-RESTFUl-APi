from flask import Flask, jsonify, request

app = Flask(__name__)

inventory=[]

@app.route("/inventory", method=["GET"])
def get_inventory():

    return jsonify("Inventory found"), 200


@app.route("/inventory/<int:inventory_id>", method=["GET"])
def get_inventory(inventory_id):

    inventory = next ((inventory for inventory in inventory if inventory.id == inventory_id), None)

    data = request.get_json

    if not inventory:
        return jsonify("Inventory not found"), 401

    if inventory_id in data:
        return jsonify("inventory found"), 200


@app.route("/inventory", methods=["POST"])
def add_inventory():

    data = request.get_json()

    new_inventory = inventory(len(inventory) +1, data["product_name"])

    inventory.append(new_inventory)

    return jsonify("new_inventory.to_dict()"),201


@app.route("/inventory/<int:inventory_id>", method=["PATCH"])
def update_inventory(inventory_id):

    inventory = next ((inventory for inventory in inventory if inventory.id == inventory_id), None)

    data = request.get_json()

    if not inventory:
        return jsonify("Inventory not found"),401

    if "product_name" in data:
        inventory.product_name = data["product_name"]
        return jsonify("inventory.to_dict()"),200


@app.route("/inventory/<int:inventory_id>", method=["DELETE"])
def delete_inventory(inventory_id):

    inventory = next ((inventory for inventory in inventory if inventory.id == inventory_id), None)

    if not inventory:
        return jsonify("Inventory not found"),404

    inventory[:] = [inventory for inventory in inventory if inventory.id != inventory_id]

    return jsonify(""),204


if __name__=="__main__":
    app.run(debug=True)