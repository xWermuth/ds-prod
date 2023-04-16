import numpy as np
from flask import Flask, request


app = Flask(__name__)


rmses = {}
@app.route('/',  methods=['GET'])
def index():
    global rmses
    userid = request.args.get("userid")
    itemid = request.args.get("itemid")
    rating = request.args.get("rating")
    estimated_rating = request.args.get("estimated_rating")
    print(f"userId: {userid}")
    print(f"rating: {rating}")
    print(f"estimated_rating: {estimated_rating}")

    if userid not in rmses:
        rmses[userid] = ([], [])

    # Append to actual 
    rmses[userid][0].append(rating)
    # Append to estimated 
    rmses[userid][1].append(estimated_rating)

    return rmses

@app.route('/rmse',  methods=['GET'])
def get_rmses():
    userid = request.args.get("userid")
    user = rmses[userid]
    return np.sqrt(np.mean((np.array(user[1])-np.array(user[0]))**2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)


