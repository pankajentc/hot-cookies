import pandas as pd
import sys


def get_hot_cookie(f_name, date):
    df = pd.read_csv(f_name, sep=',', index_col=0)
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')
    df = df.loc[df['timestamp'] == date].groupby('cookie').size().reset_index(name='Size')
    return df[df.Size == df.Size.max()].cookie.to_string(index=False).strip()


def e_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


if __name__ == "__main__":

    file_name = sys.argv[1]
    date = sys.argv[2]
    e_print("Processing start...",file_name,date)
    print(get_hot_cookie(file_name, date))

