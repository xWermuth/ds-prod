import numpy as np
from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Gauge


start_http_server(9000)
app = Flask(__name__)
gauge = Gauge('rmse', 'rmse for predicted rating')

rmses = {}
@app.route('/',  methods=['GET'])
def index():
    global rmses
    userid = int(float(request.args.get("userid")))
    itemid = request.args.get("itemid")
    rating = float(request.args.get("rating"))
    estimated_rating = float(request.args.get("estimated_rating"))
    rmse = np.sqrt(np.mean((estimated_rating-rating)**2))
    print("----------------------------------------------------------------------")
    print(f"userId: {userid}")
    print(f"rating: {rating}")
    print(f"estimated_rating: {estimated_rating}")
    print(f"rmse: {rmse}")

    if userid not in rmses:
        rmses[userid] = []
    rmses[userid].append(rmse)

    avg = np.average(rmses[userid])
    print(f"Average rmse: {avg}")
    print("----------------------------------------------------------------------")
    gauge.set(rmse)
    return rmses

@app.route('/rmse',  methods=['GET'])
def get_rmses():
    global rmses
    userid = int(float(request.args.get("userid")))
    avg = np.average(rmses[userid])
    return jsonify(rmse=avg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)


