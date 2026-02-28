from flask import Flask, jsonify, request
# firebase import
import firebase_admin
from firebase_admin import credentials, firestore

cred_path = os.environ.get("FIREBASE_CREDENTIALS")

if not firebase_admin._apps: #if firebase has not been initialized yet

    cred = credentials.Certificate(cred_path) #load credentials
    firebase_admin.initialize_app(cred) #python app connects to firebase with the credentials

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