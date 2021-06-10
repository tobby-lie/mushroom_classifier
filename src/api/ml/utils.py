import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import wget
from pickle import load
import os


def predict_edibility(model, data, file_name='ml/model/mushrooms.csv'):

    print('in here')

    # df = pd.read_csv(file_name)

    # df.drop(['veil-type'], axis=1, inplace=True)

    # df = df.append(data, ignore_index=True)

    try:

        print(data)
        df = pd.DataFrame(data, index=[0])

        df = df.drop(columns=['class'])

        print('new df')
        print(df)

        for i in df.columns:
            file = open("./ml/model/{}_le.pkl".format(i), "rb")
            le = load(file)
            file.close()
            df[i] = le.transform(df[i])

        x = df

        input = np.array(x.iloc[len(df.index) - 1].tolist())

        print('input')
        print(input.reshape(1, len(data) - 1))
        print(input.reshape(1, len(data) - 1).shape)

        # model = tf.keras.models.load_model(model_file)
        prediction = model.predict(input.reshape(1, len(data) - 1))
        print(prediction)
        prediction = (prediction > 0.5)

        print(f'prediction {prediction}')

        if prediction == True:
            return 'poisonous'
        else:
            return 'edible'
    except:
        print('in except')
        return None


# if __name__ == '__main__':
#     data = {'class': 'p', 'cap-shape': 'x', 'cap-surface': 's',
#             'cap-color': 'n', 'bruises': 't', 'odor': 'a',
#             'gill-attachment': 'f', 'gill-spacing': 'c',
#             'gill-size': 'n', 'gill-color': 'k', 'stalk-shape': 'e',
#             'stalk-root': 'e', 'stalk-surface-above-ring': 's',
#             'stalk-surface-below-ring': 's', 'stalk-color-above-ring': 'w',
#             'stalk-color-below-ring': 'w', 'veil-color': 'w', 'ring-number': 'o',
#             'ring-type': 'p', 'spore-print-color': 'k', 'population': 's',
#             'habitat': 'u'}

#     parser = argparse.ArgumentParser('Data loader test')
#     parser.add_argument('--data_path', type=str,
#                         default='./ml/model/mushrooms.csv')
#     parser.add_argument('--chunksize', type=int, default=100)
#     parser.add_argument('--encoding', type=str, default='utf-8')
#     parser.add_argument('--max_rows', type=int, default=None)
#     parser.add_argument('--sep', type=str, default=',')
#     parser.add_argument('--epochs', type=int, default=100)
#     parser.add_argument('--batch_size', type=int, default=64)

#     args = parser.parse_args()

#     data_loader = DataLoader(args)

#     x_train, x_test, y_train, y_test, number_of_classes = data_loader.load_data()

#     model_name = 'model_30.h5'
#     model_path = f'./model/{model_name}'
#     model = MushroomClassifier(number_of_classes, args)

#     if model_name not in os.listdir('./ml/model/'):
#         print(f'downloading the trained model {model_name}')
#         wget.download(
#             "https://github.com/tobby-lie/mushroom_classifier/blob/main/mushroom_classification_app/src/api/ml/model/model_30.h5",
#             out=model_path
#         )
#     else:
#         print("model already saved to api/ml/models")

#     model = tf.keras.models.load_model(model_path)

#     print(predict_edibility('model/model_30.h5', data, '/model/mushrooms.csv'))
