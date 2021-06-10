import pandas as pd
from tqdm import tqdm
import argparse
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


class DataLoader():

    def __init__(self, args):
        self.data_path = args.data_path
        self.chunksize = args.chunksize
        self.encoding = args.encoding
        self.max_rows = args.max_rows
        self.sep = args.sep

    def load_data(self):
        df = pd.read_csv(self.data_path)

        le = LabelEncoder()
        for i in df.columns:
            df[i] = le.fit_transform(df[i])

        df.drop(['veil-type'], axis=1, inplace=True)

        x = df.drop('class', axis=1)
        y = df['class']

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=0)

        number_of_classes = 1

        return x_train, x_test, y_train, y_test, number_of_classes


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Data loader test')
    parser.add_argument('--data_path', type=str,
                        default='./ml/model/mushrooms.csv')
    parser.add_argument('--chunksize', type=int, default=500)
    parser.add_argument('--encoding', type=str, default='utf-8')
    parser.add_argument('--max_rows', type=int, default=None)
    parser.add_argument('--sep', type=str, default=',')

    args = parser.parse_args()

    data_loader = DataLoader(args)
    x_train, x_test, y_train, y_test, number_of_classes = data_loader.load_data()

    print('Dimensions of data')
    print(f'x_train: {x_train.shape}')
    print(f'x_test: {x_test.shape}')
    print(f'y_train: {y_train.shape}')
    print(f'y_test: {y_test.shape}')
