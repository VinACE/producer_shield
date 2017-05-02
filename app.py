"""

Kafka consumer that does sentiment analysis of Chatter data. It identifies the most
polarizing threads and then posts to them via Heroku Connect.
"""

import psycopg2
import os
import sys
import urllib

from flask import Flask, abort, request
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from ihealthdata.persistence.pgsql_connector import PostgresConnector
import ihealthdata.utils.loggerutils as logger
from ihealthdata.producer.ihealth_demo_simulator import Producer


app = Flask(__name__)

db_con = None

# @app.route('/sf-data', methods=['GET'])
@app.route('/')
def sf_data():

    if request.method == 'GET':

        try:
            print("Trying to connect to database $$$$$$$$$$$$$$$$$$$$")

            # cc = PostgresConnector()
            # rows = cc.data_access_producer(101,101)

            # Calling the demo simulator script............

            callProducer = Producer()

            print("print callProducer type", type(callProducer))

            callProducer.start_rolling()

            print("connection success")
            return "Success"
        except Exception as ex:
                logger.error('Exception Received while trying to connect to postgres')
                # raise OSError:


if __name__ == '__main__':
    # cc = PostgresConnector()
    app.run(debug=True)
