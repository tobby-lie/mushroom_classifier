import tensorflow as tf
from tensorflow.python.keras.backend import categorical_crossentropy
from tensorflow.python.keras.layers.core import Dense, Dropout
from data_loader import DataLoader
import argparse
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score


class MushroomClassifier():

    def __init__(self, number_of_classes, args):
        self.model = tf.keras.models.Sequential([
            # tf.keras.layers.Input(shape=(2,)),
            tf.keras.layers.Dense(
                units=16, input_dim=21, activation='relu'),
            tf.keras.layers.Dense(
                units=12, activation='relu'),
            tf.keras.layers.Dense(
                units=10, activation='relu'),
            tf.keras.layers.Dense(
                units=8, activation='relu'),
            tf.keras.layers.Dense(units=number_of_classes,
                                  activation='sigmoid')
        ])

        self.epochs = args.epochs
        self.batch_size = args.batch_size

    def compile_and_fit(self, train_data, val_data, train_labels, val_labels):

        self.model.compile(loss='binary_crossentropy',
                           optimizer='adam', metrics=['accuracy'])
        history = self.model.fit(
            train_data, train_labels, validation_data=(val_data, val_labels), epochs=self.epochs, batch_size=self.batch_size)

        # summarize history for accuracy and loss for train/test
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model train/test metrics')
        plt.ylabel('accuracy/loss')
        plt.xlabel('epoch')
        plt.legend(['train accuracy', 'test accuracy',
                   'train loss', 'test loss'], loc='upper left')
        plt.show()

        self.model.save('../models/model_{}.h5'.format(self.epochs))

        print('Model saved!')

        predictions = self.model.predict(val_data)
        predictions = (predictions > 0.5)

        cm = confusion_matrix(val_labels, predictions)
        print('confusion matrix: \n', cm)

        print(classification_report(val_labels, predictions))

        return history

    def svm_fit(self, train_data, val_data, train_labels, val_labels):
        svc = SVC(kernel='linear')
        svc.fit(train_data, train_labels)

        predictions = svc.predict(val_data)
        cm = confusion_matrix(val_labels, predictions)
        print('confusion matrix: \n', cm)

        sva = accuracy_score(val_labels, predictions)
        print('accuracy score = ', accuracy_score(val_labels, predictions))
        print("Classification Report",
              classification_report(val_labels, predictions))


if __name__ == '__main__':

    parser = argparse.ArgumentParser('Data loader test')
    parser.add_argument('--data_path', type=str,
                        default='../data/mushrooms.csv')
    parser.add_argument('--chunksize', type=int, default=100)
    parser.add_argument('--encoding', type=str, default='utf-8')
    parser.add_argument('--max_rows', type=int, default=None)
    parser.add_argument('--sep', type=str, default=',')
    parser.add_argument('--epochs', type=int, default=30)
    parser.add_argument('--batch_size', type=int, default=10)

    args = parser.parse_args()

    data_loader = DataLoader(args)
    x_train, x_test, y_train, y_test, number_of_classes = data_loader.load_data()

    print('Dimensions of data')
    print(f'x_train: {x_train.shape}')
    print(f'x_test: {x_test.shape}')
    print(f'y_train: {y_train.shape}')
    print(f'y_test: {y_test.shape}')

    mushroom_classifier = MushroomClassifier(number_of_classes, args)
    mushroom_classifier.compile_and_fit(
        x_train, x_test, y_train, y_test)

    mushroom_classifier = MushroomClassifier(number_of_classes, args)
    mushroom_classifier.svm_fit(
        x_train, x_test, y_train, y_test)
