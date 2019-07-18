from google.cloud import bigquery

def insert_data(data1, data2):
    """[summary]
    
    Arguments:
        phone_number {[type]} -- [description]
        target {[type]} -- [description]
    """
    bigquery_client = bigquery.Client()
    query_job = bigquery_client.query("""
        INSERT INTO `qoala-217505.recommender_system.phonenumber_target`#path database (variable1 ,variable2)
        VALUES ('%s', %d)""" %(data1, data2))
    query_job.result()

def update_data(data):


def delete_data(data):

