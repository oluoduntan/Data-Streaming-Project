from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import json
from kafka import KafkaProducer, KafkaConsumer
import time
import logging

default_args = {
    "owner": "OluOduntan",
    "start_date": datetime(2024, 3, 30, 10, 00)
}

def get_data():
    response = requests.get("https://randomuser.me/api/")
    response = response.json()['results'][0]
    return response

def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    data['address'] = f"{location['street']['number']} {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']

    return data

def stream_data():
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    #producer.send('users_created', json.dumps(format_data(get_data())).encode('utf-8'))
    curr_time = time.time()

    while time.time() <= curr_time+30:
        try:
            producer.send('users_created', json.dumps(format_data(get_data())).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

with DAG(
    dag_id="user_automation",
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
    ):

    streaming_task = PythonOperator(
        task_id="stream_data_from_api",
        python_callable=stream_data
    )