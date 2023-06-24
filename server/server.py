from flask import Flask, jsonify
from flask_cors import CORS
import json

w, h = 8, 8
tbl = [[['-',0] for x in range(w)] for y in range(h)]

tbl[3][3] = ['A',1]
tbl[4][3] = ['B',5]
tbl[3][4] = ['B',10]
tbl[4][4] = ['A',50]

lst = [[{
        'X': x,
        'Y': y,
        'Player': tbl[y][x][0],
        'Coin': tbl[y][x][1]} for x in range(len(tbl[y]))] for y in range(len(tbl))]

json_text = json.dumps(lst)

# app instance
app = Flask(__name__)
CORS(app)

# /app/start
@app.route("/api/start",methods=['GET'])
def return_home():
    return jsonify({
        'board_size':{"width": 8,"height":8},
        'coin_arr':json_text
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)
