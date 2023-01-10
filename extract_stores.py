import pandas as pd
import requests
from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@localhost:5432/gamedeals')


def extract_transform():
    response = requests.get("https://www.cheapshark.com/api/1.0/stores")
    if response.status_code == 200:
        global df
        data = response.json()
        df = pd.DataFrame(data)
        df.drop(labels=['images'], axis=1, inplace=True)
        df.to_csv('stores.csv', index=False)

def load():
    try:
        df.head(n=0).to_sql(name='stores', con=engine, if_exists='fail')
    except ValueError:
        pass
    df.to_sql(name='stores', con=engine, if_exists='append')


extract_transform()
