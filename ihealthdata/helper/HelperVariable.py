from ihealthdata.utils.configmanager import ConfigManager
import ihealthdata.utils.loggerutils as logger
from datetime import datetime

class HelperVariable(object):

    def __init__(self):

        try:
            self.config_manager = ConfigManager()

        except Exception as ex:
            logger.error('Exception Received while trying to set-up config-manager')

        self.SPARK_APP_NAME = str(self.config_manager.config_item \
                                            ('Spark_Configs_Kafka_Consumer', 'SPARK_APP_NAME'))
        self.MESOS_MASTER = str(self.config_manager.config_item \
                                        ('Spark_Configs_Kafka_Consumer', 'MESOS_MASTER'))
        self.SPARK_EXECUTOR_MEMORY = str(self.config_manager.config_item \
                                        ('Spark_Configs_Kafka_Consumer', 'SPARK_EXECUTOR_MEMORY'))
        self.SPARK_CASSANDRA_CONNECTION_HOST = str(self.config_manager.config_item \
                                        ('Spark_Configs_Kafka_Consumer', 'SPARK_CASSANDRA_CONNECTION_HOST'))
        ##############################################################################################
        self.CASSANDRA_SERVER_IP1 = str(self.config_manager.config_item \
                        ('Cassandra_Cluster', 'CASSANDRA_SERVER_IP1'))
        self.CASSANDRA_SERVER_IP2 = str(self.config_manager.config_item \
                        ('Cassandra_Cluster', 'CASSANDRA_SERVER_IP2'))
        self.CASSANDRA_SERVER_IP3 = str(self.config_manager.config_item \
                        ('Cassandra_Cluster', 'CASSANDRA_SERVER_IP3'))
        self.CASSANDRA_SERVER_IP4 = str(self.config_manager.config_item \
                        ('Cassandra_Cluster', 'CASSANDRA_SERVER_IP4'))

        self.CASSANDRA_CLUSTER_KEYSPACE = \
                      str(self.config_manager.config_item('Cassandra_Cluster_KeySpace', 'CASSANDRA_CLUSTER_KEYSPACE'))

        self.KAFKA_TOPIC_QUEUE = \
                      str(self.config_manager.config_item('Kafka_Topic_Queue', 'KAFKA_TOPIC_QUEUE'))

        self.KAFKA_SCHEDULER = \
                      str(self.config_manager.config_item('Bootstrap_Servers', 'KAFKA_SCHEDULER'))
        ###############################################################################################
        self.ACTIVITY_MODEL_PATH_101 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_101'))
        self.ACTIVITY_MODEL_PATH_102 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_102'))
        self.ACTIVITY_MODEL_PATH_103 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_103'))
        self.ACTIVITY_MODEL_PATH_104 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_104'))
        self.ACTIVITY_MODEL_PATH_105 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_105'))
        self.ACTIVITY_MODEL_PATH_106 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_106'))
        self.ACTIVITY_MODEL_PATH_107 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_107'))
        self.ACTIVITY_MODEL_PATH_108 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_108'))
        self.ACTIVITY_MODEL_PATH_109 = str(self.config_manager.config_item \
                                        ('Model_Paths', 'ACTIVITY_MODEL_PATH_109'))

        ####################################################################################
        self.SUMMARY_POLLING_DURATION = int(self.config_manager.config_item \
                                        ('Summary_Polling_Duration', 'SUMMARY_POLLING_DURATION'))
        ####################################################################################

        self.PEOPLE_TABLE = str(self.config_manager.config_item \
                                        ('Cassandra_Table_Names', 'PEOPLE_TABLE'))
        self.CARDIAC_EXCEPTION_SUMMARY_TABLE = str(self.config_manager.config_item \
                                        ('Cassandra_Table_Names', 'CARDIAC_EXCEPTION_SUMMARY_TABLE'))
        self.CARDIAC_EXCEPTION_TABLE = str(self.config_manager.config_item \
                                        ('Cassandra_Table_Names', 'CARDIAC_EXCEPTION_TABLE'))
        self.ACTIVITY_PREDICTION_TABLE = str(self.config_manager.config_item \
                                        ('Cassandra_Table_Names', 'ACTIVITY_PREDICTION_TABLE'))
        self.ACTIVITY_PREDICTION_SUMMARY_TABLE = str(self.config_manager.config_item \
                                        ('Cassandra_Table_Names', 'ACTIVITY_PREDICTION_SUMMARY_TABLE'))
        ############################################################################################

        self.START_ACTIVITY_101 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_101'))
        self.START_ACTIVITY_102 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_102'))
        self.START_ACTIVITY_103 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_103'))
        self.START_ACTIVITY_104 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_104'))
        self.START_ACTIVITY_105 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_105'))
        self.START_ACTIVITY_106 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_106'))
        self.START_ACTIVITY_107 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_107'))
        self.START_ACTIVITY_108 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_108'))
        self.START_ACTIVITY_109 = str(self.config_manager.config_item \
                                        ('Starting_Activity_Initializer', 'START_ACTIVITY_109'))
# Need to check data and put exact activity-ids because different patients now have different activities
        #############################################################################################

        self.SUMMARY_TRANSITION_INDICATOR_FLAG_101 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_101'))
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_102 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_102'))
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_103 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_103'))
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_104 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_104'))
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_105 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_105'))
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_106 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_106'))
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_107 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_107'))
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_108 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_108'))
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_109 = int(self.config_manager.config_item \
                                     ('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_109'))

        ############################################################################################
        self.ACTIVITY_PERSISTENCE_101 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_101'))
        self.ACTIVITY_PERSISTENCE_102 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_102'))
        self.ACTIVITY_PERSISTENCE_103 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_103'))
        self.ACTIVITY_PERSISTENCE_104 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_104'))
        self.ACTIVITY_PERSISTENCE_105 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_105'))
        self.ACTIVITY_PERSISTENCE_106 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_106'))
        self.ACTIVITY_PERSISTENCE_107 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_107'))
        self.ACTIVITY_PERSISTENCE_108 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_108'))
        self.ACTIVITY_PERSISTENCE_109 = int(self.config_manager.config_item \
                                     ('Activity_Persistence', 'ACTIVITY_PERSISTENCE_109'))

        ###########################################################################################
        self.ACTIVITY_PERSISTENCE_COUNTER_101 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_101'))
        self.ACTIVITY_PERSISTENCE_COUNTER_102 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_102'))
        self.ACTIVITY_PERSISTENCE_COUNTER_103 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_103'))
        self.ACTIVITY_PERSISTENCE_COUNTER_104 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_104'))
        self.ACTIVITY_PERSISTENCE_COUNTER_105 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_105'))
        self.ACTIVITY_PERSISTENCE_COUNTER_106 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_106'))
        self.ACTIVITY_PERSISTENCE_COUNTER_107 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_107'))
        self.ACTIVITY_PERSISTENCE_COUNTER_108 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_108'))
        self.ACTIVITY_PERSISTENCE_COUNTER_109 = int(self.config_manager.config_item \
                                     ('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_109'))

        ####################################################################################################
        self.AVERAGE_HEARTRATE_101 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_101'))
        self.AVERAGE_HEARTRATE_102 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_102'))
        self.AVERAGE_HEARTRATE_103 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_103'))
        self.AVERAGE_HEARTRATE_104 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_104'))
        self.AVERAGE_HEARTRATE_105 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_105'))
        self.AVERAGE_HEARTRATE_106 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_106'))
        self.AVERAGE_HEARTRATE_107 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_107'))
        self.AVERAGE_HEARTRATE_108 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_108'))
        self.AVERAGE_HEARTRATE_109 = float(self.config_manager.config_item \
                                     ('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_109'))

        ###############################################################################################
        self.SUM_HEARTRATE_101 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_101'))
        self.SUM_HEARTRATE_102 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_102'))
        self.SUM_HEARTRATE_103 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_103'))
        self.SUM_HEARTRATE_104 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_104'))
        self.SUM_HEARTRATE_105 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_105'))
        self.SUM_HEARTRATE_106 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_106'))
        self.SUM_HEARTRATE_107 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_107'))
        self.SUM_HEARTRATE_108 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_108'))
        self.SUM_HEARTRATE_109 = float(self.config_manager.config_item \
                                     ('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_109'))

        ###################################################################################
        self.MIN_HEARTRATE_101 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_101'))
        self.MIN_HEARTRATE_102 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_102'))
        self.MIN_HEARTRATE_103 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_103'))
        self.MIN_HEARTRATE_104 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_104'))
        self.MIN_HEARTRATE_105 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_105'))
        self.MIN_HEARTRATE_106 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_106'))
        self.MIN_HEARTRATE_107 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_107'))
        self.MIN_HEARTRATE_108 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_108'))
        self.MIN_HEARTRATE_109 = int(self.config_manager.config_item \
                                     ('Min_HeartRate_Initializer', 'MIN_HEARTRATE_109'))
        ###############################################################################
        self.MAX_HEARTRATE_101 = int(self.config_manager.config_item \
                                     ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_101'))
        self.MAX_HEARTRATE_102 = int(self.config_manager.config_item \
                                     ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_102'))
        self.MAX_HEARTRATE_103 = int(self.config_manager.config_item \
                                     ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_103'))
        self.MAX_HEARTRATE_104 = int(self.config_manager.config_item \
                                     ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_104'))
        self.MAX_HEARTRATE_105 = int(self.config_manager.config_item \
                                     ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_105'))
        self.MAX_HEARTRATE_106 = int(self.config_manager.config_item \
                                     ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_106'))
        self.MAX_HEARTRATE_107 = int(self.config_manager.config_item \
                                     ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_107'))
        self.MAX_HEARTRATE_108 = int(self.config_manager.config_item \
                                     ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_108'))
        self.MAX_HEARTRATE_109 = int(self.config_manager.config_item \
                             ('Max_HeartRate_Initializer', 'MAX_HEARTRATE_109'))

        ##################################################################################
        self.AVG_RISK_SCORE_101 = float(self.config_manager.config_item \
                                     ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_101'))
        self.AVG_RISK_SCORE_102 = float(self.config_manager.config_item \
                                     ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_102'))
        self.AVG_RISK_SCORE_103 = float(self.config_manager.config_item \
                                            ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_103'))
        self.AVG_RISK_SCORE_104 = float(self.config_manager.config_item \
                                            ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_104'))
        self.AVG_RISK_SCORE_105 = float(self.config_manager.config_item \
                                            ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_105'))
        self.AVG_RISK_SCORE_106 = float(self.config_manager.config_item \
                                            ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_106'))
        self.AVG_RISK_SCORE_107 = float(self.config_manager.config_item \
                                            ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_107'))
        self.AVG_RISK_SCORE_108 = float(self.config_manager.config_item \
                                            ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_108'))
        self.AVG_RISK_SCORE_109 = float(self.config_manager.config_item \
                                            ('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_109'))

        ##################################################################################
        self.SUM_RISK_SCORE_101 = float(self.config_manager.config_item \
                                     ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_101'))
        self.SUM_RISK_SCORE_102 = float(self.config_manager.config_item \
                                     ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_102'))
        self.SUM_RISK_SCORE_103 = float(self.config_manager.config_item \
                                            ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_103'))
        self.SUM_RISK_SCORE_104 = float(self.config_manager.config_item \
                                            ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_104'))
        self.SUM_RISK_SCORE_105 = float(self.config_manager.config_item \
                                            ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_105'))
        self.SUM_RISK_SCORE_106 = float(self.config_manager.config_item \
                                            ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_106'))
        self.SUM_RISK_SCORE_107 = float(self.config_manager.config_item \
                                            ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_107'))
        self.SUM_RISK_SCORE_108 = float(self.config_manager.config_item \
                                            ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_108'))
        self.SUM_RISK_SCORE_109 = float(self.config_manager.config_item \
                                            ('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_109'))

        ##############################################################################
        self.ANOMALY_SCORE_MAX_101 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_101'))
        self.ANOMALY_SCORE_MAX_102 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_102'))
        self.ANOMALY_SCORE_MAX_103 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_103'))
        self.ANOMALY_SCORE_MAX_104 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_104'))
        self.ANOMALY_SCORE_MAX_105 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_105'))
        self.ANOMALY_SCORE_MAX_106 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_106'))
        self.ANOMALY_SCORE_MAX_107 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_107'))
        self.ANOMALY_SCORE_MAX_108 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_108'))
        self.ANOMALY_SCORE_MAX_109 = float(self.config_manager.config_item \
                                     ('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_109'))
        ####################################################################################
        self.CORRECT_PREDICTED_ACTIVITY_COUNTER = int(self.config_manager.config_item \
                                     ('Prediction_Parameters', 'CORRECT_PREDICTED_ACTIVITY_COUNTER'))
        self.PREDICTION_ACCURACY = float(self.config_manager.config_item \
                                     ('Prediction_Parameters', 'PREDICTION_ACCURACY'))
        #######################################################################################
        self.PREDICTION_ACCURACY_SUB_INTERVAL_101 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_101'))
        self.PREDICTION_ACCURACY_SUB_INTERVAL_102 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_102'))
        self.PREDICTION_ACCURACY_SUB_INTERVAL_103 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_103'))
        self.PREDICTION_ACCURACY_SUB_INTERVAL_104 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_104'))
        self.PREDICTION_ACCURACY_SUB_INTERVAL_105 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_105'))
        self.PREDICTION_ACCURACY_SUB_INTERVAL_106 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_106'))
        self.PREDICTION_ACCURACY_SUB_INTERVAL_107 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_107'))
        self.PREDICTION_ACCURACY_SUB_INTERVAL_108 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_108'))
        self.PREDICTION_ACCURACY_SUB_INTERVAL_109 = float(self.config_manager.config_item \
                                     ('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_109'))
        ####################################################################################################
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_101 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_101'))
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_102 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_102'))
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_103 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_103'))
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_104 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_104'))
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_105 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_105'))
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_106 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_106'))
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_107 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_107'))
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_108 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_108'))
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_109 = int(self.config_manager.config_item \
                              ('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_109'))
        #######################################################################################################
        ## Starting Time of new Summary when there is transition of activity or poll duration time-out
        self.START_TIME_NEW_SUMMARY_101 = datetime.now()
        self.START_TIME_NEW_SUMMARY_102 = datetime.now()
        self.START_TIME_NEW_SUMMARY_103 = datetime.now()
        self.START_TIME_NEW_SUMMARY_104 = datetime.now()
        self.START_TIME_NEW_SUMMARY_105 = datetime.now()
        self.START_TIME_NEW_SUMMARY_106 = datetime.now()
        self.START_TIME_NEW_SUMMARY_107 = datetime.now()
        self.START_TIME_NEW_SUMMARY_108 = datetime.now()
        self.START_TIME_NEW_SUMMARY_109 = datetime.now()
        #################################################################################################
        ## In practicality every-model should have its own set of the parameters
        self.NUM_CLASSES = int(self.config_manager.config_item('Machine_Learning_Parameters', 'NUM_CLASSES'))
        self.IMPURITY = str(self.config_manager.config_item('Machine_Learning_Parameters', 'IMPURITY'))
        self.MAX_DEPTH = int(self.config_manager.config_item('Machine_Learning_Parameters', 'MAX_DEPTH'))
        self.MAX_BINS = int(self.config_manager.config_item('Machine_Learning_Parameters', 'MAX_BINS'))
        ###################################################################################################
        self.ACTIVITY_ENCODER_DICTIONARY_INITIALIZER = {  \
	        1.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_1')), \
		2.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_2')), \
		3.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_3')), \
		4.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_4')), \
		5.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_5')), \
		6.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_6')), \
		7.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_7')), \
		9.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_9')), \
		10.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_10')), \
		11.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_11')), \
		12.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_12')), \
		13.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_13')), \
		16.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_16')), \
		17.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_17')), \
		18.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_18')), \
		19.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_19')), \
		20.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_20')), \
		24.0 : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_24')), \
		0.0  : float(self.config_manager.config_item('Encoder_Mapping', 'ENCODED_0'))    \
                                           }

	###########################################################################################################
        self.TOTAL_DICTIONARY = { 									       \
		101:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_101')), \
	        102:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_102')), \
		103:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_103')), \
	        104:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_104')), \
	        105:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_105')), \
	        106:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_106')), \
		107:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_107')), \
		108:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_108')), \
		109:int(self.config_manager.config_item('Total_Testing_Data_Points_per_Patient', 'TOTAL_109')) \
				}
	######################################################################################################
        self.INDEX_DICTIONARY_INITIALIZER = { 							\
		101:int(self.config_manager.config_item('Index_Initializer', 'INDEX_101')),     \
		102:int(self.config_manager.config_item('Index_Initializer', 'INDEX_102')),	\
		103:int(self.config_manager.config_item('Index_Initializer', 'INDEX_103')),	\
		104:int(self.config_manager.config_item('Index_Initializer', 'INDEX_104')),	\
		105:int(self.config_manager.config_item('Index_Initializer', 'INDEX_105')),	\
		106:int(self.config_manager.config_item('Index_Initializer', 'INDEX_106')),	\
		107:int(self.config_manager.config_item('Index_Initializer', 'INDEX_107')),	\
		108:int(self.config_manager.config_item('Index_Initializer', 'INDEX_108')),	\
		109:int(self.config_manager.config_item('Index_Initializer', 'INDEX_109'))	\
                           		    }
	####################################################################################################
        self.MAX_HEARTRATE_DICTIONARY = {                                                       \
                101:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_101')),     \
		102:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_102')),     \
		103:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_103')),     \
		104:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_104')),     \
		105:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_105')),     \
		106:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_106')),     \
		107:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_107')),     \
		108:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_108')),     \
		109:int(self.config_manager.config_item('Max_HeartRate_Initializer', 'MAX_HEARTRATE_109')),     \
                                            }
	#####################################################################################################

        self.MIN_HEARTRATE_DICTIONARY = {                                                       \
                101:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_101')),     \
		102:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_102')),     \
		103:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_103')),     \
		104:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_104')),     \
		105:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_105')),     \
		106:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_106')),     \
		107:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_107')),     \
		108:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_108')),     \
		109:int(self.config_manager.config_item('Min_HeartRate_Initializer', 'MIN_HEARTRATE_109')),     \
                                            }
	#####################################################################################################
        self.ANOMALY_SCORE_MAX_DICTIONARY = {                                                       \
                101:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_101')),     \
		102:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_102')),     \
		103:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_103')),     \
		104:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_104')),     \
		105:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_105')),     \
		106:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_106')),     \
		107:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_107')),     \
		108:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_108')),     \
		109:int(self.config_manager.config_item('Anomaly_Score_Max_Initializer', 'ANOMALY_SCORE_MAX_109')),     \
                                            }

	###################################################################################################################
        self.SUM_HEARTRATE_DICTIONARY = {                                                       \
                101:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_101')),     \
		102:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_102')),     \
		103:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_103')),     \
		104:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_104')),     \
		105:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_105')),     \
		106:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_106')),     \
		107:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_107')),     \
		108:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_108')),     \
		109:int(self.config_manager.config_item('Sum_HeartRate_Initializer', 'SUM_HEARTRATE_109')),     \
                                            }

	#####################################################################################################################
        self.SUM_RISK_SCORE_DICTIONARY = {                                                       \
                101:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_101')),     \
		102:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_102')),     \
		103:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_103')),     \
		104:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_104')),     \
		105:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_105')),     \
		106:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_106')),     \
		107:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_107')),     \
		108:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_108')),     \
		109:int(self.config_manager.config_item('Sum_RiskScore_Initializer', 'SUM_RISK_SCORE_109')),     \
                                            }
	
	####################################################################################################################
        self.SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_DICTIONARY = {                                                       \
                101:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_101')),   \
		102:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_102')),   \
		103:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_103')),   \
		104:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_104')),   \
		105:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_105')),   \
		106:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_106')),   \
		107:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_107')),   \
		108:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_108')),   \
		109:int(self.config_manager.config_item('Sum_Correct_Predicted_Activity_Counter', 'SUM_CORRECT_PREDICTED_ACTIVITY_COUNTER_109')),   \
                                            }

	####################################################################################################################
        self.START_ACTIVITY_DICTIONARY = {                                                       \
                101:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_101')),   \
		102:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_102')),   \
		103:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_103')),   \
		104:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_104')),   \
		105:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_105')),   \
		106:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_106')),   \
		107:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_107')),   \
		108:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_108')),   \
		109:(self.config_manager.config_item('Starting_Activity_Initializer', 'START_ACTIVITY_109')),   \
                                            }

	##################################################################################################################
        self.ACTIVITY_PERSISTENCE_DICTIONARY = {                                                        \
                101:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_101')),   \
		102:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_102')),   \
		103:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_103')),   \
		104:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_104')),   \
		105:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_105')),   \
		106:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_106')),   \
		107:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_107')),   \
		108:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_108')),   \
		109:int(self.config_manager.config_item('Activity_Persistence', 'ACTIVITY_PERSISTENCE_109')),   \
                                            }

	############################################################################################################
        self.SUMMARY_TRANSITION_INDICATOR_FLAG_DICTIONARY = {                                                        \
                101:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_101')),   \
		102:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_102')),   \
		103:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_103')),   \
		104:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_104')),   \
		105:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_105')),   \
		106:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_106')),   \
		107:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_107')),   \
		108:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_108')),   \
		109:int(self.config_manager.config_item('Summary_Transition_Indicator_Flags', 'SUMMARY_TRANSITION_INDICATOR_FLAG_109')),   \
                                            }

	##############################################################################################################
        self.ACTIVITY_PERSISTENCE_COUNTER_DICTIONARY = {                                                              \
                101:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_101')),   \
		102:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_102')),   \
		103:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_103')),   \
		104:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_104')),   \
		105:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_105')),   \
		106:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_106')),   \
		107:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_107')),   \
		108:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_108')),   \
		109:int(self.config_manager.config_item('Activity_Persistence_Counter', 'ACTIVITY_PERSISTENCE_COUNTER_109')),   \
                                            }

	#######################################################################################################################
        self.AVERAGE_HEARTRATE_DICTIONARY = {                                                              \
                101:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_101')),   \
		102:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_102')),   \
		103:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_103')),   \
		104:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_104')),   \
		105:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_105')),   \
		106:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_106')),   \
		107:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_107')),   \
		108:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_108')),   \
		109:int(self.config_manager.config_item('Average_HeartRate_Initializer', 'AVERAGE_HEARTRATE_109')),   \
                                            }

	######################################################################################################################
        self.PREDICTION_ACCURACY_SUB_INTERVAL_DICTIONARY = {                                                              \
                101:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_101')),   \
		102:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_102')),   \
		103:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_103')),   \
		104:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_104')),   \
		105:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_105')),   \
		106:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_106')),   \
		107:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_107')),   \
		108:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_108')),   \
		109:int(self.config_manager.config_item('Prediction_Accuracy_Sub_Intervals', 'PREDICTION_ACCURACY_SUB_INTERVAL_109')),   \
                                            }

	###########################################################################################################################
        self.AVG_RISK_SCORE_DICTIONARY = {                                                              \
                101:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_101')),   \
		102:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_102')),   \
		103:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_103')),   \
		104:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_104')),   \
		105:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_105')),   \
		106:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_106')),   \
		107:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_107')),   \
		108:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_108')),   \
		109:int(self.config_manager.config_item('Average_RiskScore_Initializer', 'AVG_RISK_SCORE_109')),   \
                                            }

	###########################################################################################################
        self.START_TIME_NEW_SUMMARY_DICTIONARY_INITIALIZER = {                                     \
                101:datetime.now(),   \
		102:datetime.now(),   \
		103:datetime.now(),   \
		104:datetime.now(),   \
		105:datetime.now(),   \
		106:datetime.now(),   \
		107:datetime.now(),   \
		108:datetime.now(),   \
		109:datetime.now(),   \
                	}
	############################################################################################################
        self.SUBJECT_LIST_ID = [ \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_101')) , \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_102')) , \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_103')) , \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_104')) , \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_105')) , \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_106')) , \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_107')) , \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_108')) , \
			int(self.config_manager.config_item('Subject_ID', 'SUBJECT_109'))   \
			      ]

        self.SPARK_STREAMING_CONTEXT_DURATION = \
	    int(self.config_manager.config_item('Spark_Streaming_Context_Duration', 'SPARK_STREAMING_CONTEXT_DURATION'))

        self.TOTAL_ITERATIONS = int(self.config_manager.config_item('Total_Iterations', 'TOTAL_ITERATIONS'))

        self.TIME_DURATION_BETWEEN_SUCCESSIVE_SEQNO = \
	    int(self.config_manager.config_item('Time_Interval_Successive_Seqno', 'TIME_DURATION_BETWEEN_SUCCESSIVE_SEQNO'))
#################Is it End of Constant values #####################################
## Constructor Initialization is fine ?
'''
if __name__ == '__main__':
    HelperVariable()
'''

########################### EOF ################################################################
