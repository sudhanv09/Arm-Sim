import pandas as pd

def dataset(csv_file):

    col = ['q01', 'q02', 'q03', 'q04', 'd', 'x', 'y', 'z', '1']    
    df = pd.read_csv(csv_file, names=col)

    X_cols = df.columns[5:8]
    Y_cols = df.columns[0:5]
    
    train_X = df[X_cols].values.tolist()
    train_Y = df[Y_cols].values.tolist()

    return train_X, train_Y    