from flask import Flask, jsonify
from flask_cors import CORS
import json
from game import Game

game_inst = Game()
w = game_inst.w
h = game_inst.h

tbl = [['-',0] for i in range(w*h)]

tbl[3 * w + 3] = ['A',1]
tbl[4 * w + 3] = ['B',5]
tbl[3 * w + 4] = ['B',10]
tbl[4 * w + 4] = ['A',50]

lst = [{
        'X': i % w,
        'Y': i // w,
        'Player': tbl[i][0],
        'Coin': tbl[i][1]} for i in range(len(tbl))]

game_inst.start()
if(False == game_inst.doAction('A')):
    print("Failed!")
print(game_inst.PointA)

def readyToPlay():
    return 1;

# json_text = json.dumps(lst)
def playOneStep():
    return 1;

# app instance
app = Flask(__name__)
CORS(app)

# /app/start
@app.route("/api/start",methods=['GET'])
def return_home():
    return jsonify({
        'status':"running",
        'board_size':{"width": 8,"height":8},
        'coins':lst
    })

# /app/next
@app.route("/api/next",methods=['GET'])
def step_next():
    playOneStep();
    return jsonify({
        'status':"",
        'coins':lst
    })
if __name__ == "__main__":
    app.run(debug=True, port=8080)
