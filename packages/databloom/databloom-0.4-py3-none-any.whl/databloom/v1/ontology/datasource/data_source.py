import os
from databloom.v1.ontology.datasource.mysql import Mysql
from databloom.v1.ontology.datasource.postgresql import Postgres

class Datasource:
    def __init__(self):
        # read env here
        domain = os.environ.get("SDK_SERVER_USERNAME")
        token = os.environ.get("SDK_SERVER_PASSWORD")        
        self.mysql = Mysql(domain, token)
        self.postgres = Postgres(domain, token)
        pass

    
