from google.cloud.bigquery.client import Client
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'projectig.json'
bq_client = Client()
query = """SELECT DISTINCT *  FROM `projectig-247222.projectig.historical`"""
df = bq_client.query(query).to_dataframe()