import pandas as pd

def dataset(csv_file):

    col = ['q01', 'q02', 'q03', 'q04', 'd', 'x', 'y', 'z', '1', 'null']

    df = pd.read_csv(csv_file, names=col)
    for i in col:
        df['null'] = 0

    X_cols = df.columns[5:10]
    Y_cols = df.columns[0:5]

    train_X = df[X_cols].to_numpy()
    train_Y = df[Y_cols].to_numpy()

    train = []
    for i in range(len(train_X)):
        train.append([train_X[i], train_Y[i]])

    return train

