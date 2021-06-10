import sys
import os
import random

from flask import Blueprint, request, jsonify, Flask
import tensorflow as tf
import wget

import db
import config

from ml.model import MushroomClassifier
from ml.utils import predict_edibility

import argparse

from data_loader import DataLoader

app = Flask(__name__)
api = Blueprint('api', __name__)

parser = argparse.ArgumentParser('Data loader test')
parser.add_argument('--data_path', type=str,
                    default='./ml/model/mushrooms.csv')
parser.add_argument('--chunksize', type=int, default=100)
parser.add_argument('--encoding', type=str, default='utf-8')
parser.add_argument('--max_rows', type=int, default=None)
parser.add_argument('--sep', type=str, default=',')
parser.add_argument('--epochs', type=int, default=100)
parser.add_argument('--batch_size', type=int, default=64)

args = parser.parse_args()

data_loader = DataLoader(args)

x_train, x_test, y_train, y_test, number_of_classes = data_loader.load_data()

model_name = 'model_30.h5'
model_path = f'./ml/model/{model_name}'
model = MushroomClassifier(number_of_classes, args)

if model_name not in os.listdir('./ml/model/'):
    print(f'downloading the trained model {model_name}')
    wget.download(
        "https://github.com/tobby-lie/mushroom_classifier/blob/main/mushroom_classification_app/src/api/ml/model/model_30.h5",
        out=model_path
    )
else:
    print("model already saved to api/ml/models")

model = tf.keras.models.load_model(model_path)

print("Tensorflow model loaded!")


@api.route('/predict', methods=['POST'])
def predict_mushroom():
    if request.method == 'POST':

        expected_fields = [
            'class',
            'cap-shape',
            'cap-surface',
            'cap-color',
            'bruises',
            'odor',
            'gill-attachment',
            'gill-spacing',
            'gill-size',
            'gill-color',
            'stalk-shape',
            'stalk-root',
            'stalk-surface-above-ring',
            'stalk-surface-below-ring',
            'stalk-color-above-ring',
            'stalk-color-below-ring',
            'veil-color',
            'ring-number',
            'ring-type',
            'spore-print-color',
            'population',
            'habitat'
        ]
        print('here')
        print(request.form)
        if any(field not in request.form for field in expected_fields):
            return jsonify({'error': 'Missing field in body'}), 400
        else:
            data = {"class": request.form["class"], "cap-shape": request.form["cap-shape"],
                    "cap-surface": request.form["cap-surface"],
                    "cap-color": request.form["cap-color"], "bruises": request.form["bruises"],
                    "odor": request.form["odor"],
                    "gill-attachment": request.form["gill-attachment"], "gill-spacing": request.form["gill-spacing"],
                    "gill-size": request.form["gill-size"], "gill-color": request.form["gill-color"],
                    "stalk-shape": request.form["stalk-shape"],
                    "stalk-root": request.form["stalk-root"],
                    "stalk-surface-above-ring": request.form["stalk-surface-above-ring"],
                    "stalk-surface-below-ring": request.form["stalk-surface-below-ring"],
                    "stalk-color-above-ring": request.form["stalk-color-above-ring"],
                    "stalk-color-below-ring": request.form["stalk-color-below-ring"],
                    "veil-color": request.form["veil-color"], "ring-number": request.form["ring-number"],
                    "ring-type": request.form["ring-type"], "spore-print-color": request.form["spore-print-color"],
                    "population": request.form["population"],
                    "habitat": request.form["habitat"]}
            print(data)
            output = predict_edibility(model, data)
            return jsonify(output)


@api.route('/mushroom', methods=['POST'])
def post_mushroom():
    if request.method == 'POST':
        expected_fields = [
            'cap_shape',
            'cap_surface',
            'cap_color',
            'bruses',
            'odor',
            'gill_attachement',
            'gill_spacing',
            'gill_size',
            'gill_color',
            'label'
        ]
        if any(field not in request.form for field in expected_fields):
            return jsonify({'error': 'Missing field in body'}), 400

        query = db.Review.create(**request.form)
        return jsonify(query.serialize())


@api.route('/mushrooms', methods=['GET'])
def get_mushrooms():
    if request.method == 'GET':
        query = db.Mushroom.select()
        return jsonify([r.serialize() for r in query])


app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.HOST)
