from flask import Flask, render_template, request, jsonify, request
from surprise.model_selection import train_test_split
from surprise import accuracy
from surprise import SVD
from surprise import Reader
from surprise import Dataset
import pandas as pd

directory = '/data/movielens/ml-latest-small'
df_ratings = pd.read_csv(f'{directory}/ratings.csv')

# initialize a data reader
reader = Reader(rating_scale=(1, 5))
# provide a dataset with userid, itemtid, and rating in order
data = Dataset.load_from_df(df_ratings[['userId','movieId','rating']], reader)

# Train
trainset, testset = train_test_split(data, test_size=.25)
algo = SVD()
algo.fit(trainset)
predictions = algo.test(testset)
accuracy.rmse(predictions)


app = Flask(__name__)


@app.route('/',  methods=['GET'])
def index():
    global algo
    target_userId = request.args.get("userid")
    movieId = request.args.get("itemid")
    print(f"Finding recommendations for user {target_userId} and movieId {movieId}")
    estimated_rating = algo.predict(target_userId, movieId).est
    print(f"Estimated rating: {estimated_rating}")
    return jsonify(estimated_rating=estimated_rating)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)


