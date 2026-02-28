from flask import Flask, jsonify, request
# firebase import
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../backend-workshop-2026-serviceaccountkey.json")
firebase_admin.initialize_app(cred)

# intialize database
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
# method to get users from firestore
@app.route("/firebase/get" , methods=["GET"])
def firebase_get():
    db = firestore.client()
    doc = db.collection("users").get()
    if doc.exists:
        return jsonify(doc.to_dict())
    return jsonify({"error": "Document not found"}), 404

if __name__ == "__main__":
    app.run(port=8080,debug=True)