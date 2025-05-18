this is version 2
import pandas as pd
import sqlalchemy

def extract():
    data = pd.read_csv("sample_data.csv")  # simulate API/db extract
    return data

def transform(df):
    df = df.dropna()
    df['score'] = df['value'] * 10
    return df

def load(df):
    engine = sqlalchemy.create_engine('mysql+pymysql://user:pass@host/db')
    df.to_sql('model_scores', engine, if_exists='append', index=False)

def main():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL completed successfully.")

if __name__ == "__main__":
    main()
