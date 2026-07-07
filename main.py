from flask import Flask, jsonify, request

app = Flask(__name__)

inventory=[]

@app.route("/inventory", method=["GET"])
def get_inventory():

@app.route("/inventory/<int:id>", method=["GET"])
def get_inventory(id):

@app.route("/inventory", methods=["POST"])
def add_inventory():

@app.route("/inventory/<int:id>", method=["PATCH"])
def update_inventory(id):

@app.route("/inventory/<int:id>", method=["DELETE"])
def delete_inventory(id):
    
if __name__=="__main__":
    app.run(debug=True)