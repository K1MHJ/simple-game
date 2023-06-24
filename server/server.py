from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

# /app/home
@app.route("/api/home",methods=['GET'])
def return_home():
    return jsonify({
        'message':"This is test!!!"
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)
