



class PostgresqlBase:
    """
    This database is a palantir database
    """
    credential = ""
    secret = ""
    def connect(self)-> any:
        print("connect to", self.credential)
        return "connected"
        
    def connect_orm(self, isPoolConnection: bool):
        return "connected"    

    def sql(self, query) -> any:
        print("query", query)
        return {}

    def get_info(self) -> str:
        return ""

