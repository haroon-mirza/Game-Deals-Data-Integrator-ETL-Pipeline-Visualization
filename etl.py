import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine
from prefect import task, Flow


@task
def extract_transform(url):
    global df
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.drop(labels=['releaseDate','lastChange'], axis=1, inplace=True)
        df.to_csv("cheapshark.csv", index=False)
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d")
        df['lastUpdated'] = now_str
        df.to_csv('cheapshark.csv', index=False)
        return df

@task
def load_to_postgres(df):
    engine = create_engine('postgresql://root:root@localhost:5432/gamedeals') 
    try:
        df.head(n=0).to_sql(name='cheapshark', con=engine, if_exists='fail')
    except ValueError:
        pass
    df.to_sql(name='cheapshark', con=engine, if_exists='append')
    


@Flow
def etl(url):
    extract_transform(url)
    load_to_postgres(df)

etl('https://www.cheapshark.com/api/1.0/deals')