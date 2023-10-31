import duckdb

url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet'
def load_and_process(url_or_path_to_file):    
    df1 = duckdb.query(f"SELECT * FROM read_parquet('{url_or_path_to_file}')")
    return df1



def ingest_to_db(df):
    df = load_and_process('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet')

    conn = duckdb.connect('yellow_taxi.db')
    return conn.query(f'select * from {df}').limit(1000).order_by('trip_distance')

df = load_and_process('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet')

ans = ingest_to_db(df)
print(ans)