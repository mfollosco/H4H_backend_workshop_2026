from flask import Flask, jsonify, request
import os

from dotenv import load_dotenv
load_dotenv()
# firebase import
import firebase_admin
from firebase_admin import credentials, firestore

cred_path = os.environ.get("FIREBASE_CREDENTIALS")

if not firebase_admin._apps: #if firebase has not been initialized yet

    cred = credentials.Certificate(cred_path) #load credentials
    firebase_admin.initialize_app(cred) #python app connects to firebase with the credentials

db = firestore.client()


app = Flask(__name__)
# method to get users from firestore
@app.route("/firebase/get" , methods=["GET"])
def firebase_get():
    docs = db.collection("users").get()  # returns a list of documents
    if not docs:
        return jsonify({"error": "No documents found"}), 404
    return jsonify([doc.to_dict() for doc in docs])

if __name__ == "__main__":
    app.run(port=8080,debug=True)