
### This is the Producer Code

from kafka import KafkaProducer
import time
 
import sys

#sys.path.insert(0, '/home/centos/frontier-healthdata-services/ihealthdata/persistence')

# from ihealthdata.persistence.cassandra_connector import CassandraConnector

# from .ihealthdata.persistence.pgsql_connector import PostgresConnector

# from ihealthdata.persistence.cassandra_connector import CassandraConnector 
# from ihealthdata.utils.SwitchCase import SwitchCase
from   ihealthdata.helper.HelperVariable import HelperVariable
# from ihealthdata.messaging.kafka_producer import Kafka_Producer

#hv = HelperVariable()

class Producer(object):

	def __init__(self):

		self.flag = True # Flag controlling the rolling window
		self.iteration_index = 1 # First Iteration Index

		## Index Initializers
		self.INDEX_DICTIONARY = hv.INDEX_DICTIONARY_INITIALIZER

		## Instantiating Kafka-Producer
		self.kp = Kafka_Producer()

		self.conn = PostgresConnector()
		###########################################################################

	def index_incrementor(self,peopleid,index):

		#########################################################################################
		## Ganapathy - Do we want more functional way for this if-else
		if(index > hv.TOTAL_DICTIONARY[peopleid]):

			self.INDEX_DICTIONARY[peopleid] = 1
		else:
			self.INDEX_DICTIONARY[peopleid] += 1

	##########################################################################################
	## Writes to the Kafka-Topic-Queue
	def rolling_window(self,peopleid,index):

		data_point = self.conn.data_access_producer(peopleid,index)

		## Transmitting to Kafka-Producer
		## There is a case where there are malformed partitions, (partitions in cassandra are per seqno)
		## We only generate messages when seqno can be retrieved back
		if(len(data_point)):
			self.kp.produce(data_point)
			index = index + 1 # Increasing Seqno
			self.index_incrementor(peopleid,index)
		
	## This function is called from start_rolling
	def keep_rolling(self):

		map(lambda x,y: self.rolling_window(x,y), hv.SUBJECT_LIST_ID, self.INDEX_DICTIONARY.values())

	## This is essentially what triggers the entire thing
		## This is essentially what triggers the entire thing
	def start_rolling(self):

		while self.flag:

			self.keep_rolling()
			if (self.iteration_index >= hv.TOTAL_ITERATIONS):
				self.flag = False

			self.iteration_index += 1
			time.sleep(hv.TIME_DURATION_BETWEEN_SUCCESSIVE_SEQNO)


if __name__ == '__main__':
	hv = HelperVariable()
	Producer().start_rolling()

#################################### EOF ########################################################################
